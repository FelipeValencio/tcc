import 'package:flutter/material.dart';
import 'package:plat_praticas/maquina_estado.dart';
import 'package:plat_praticas/resultados.dart';

import 'mensagem_erro.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Questionário de práticas para ambientes cloud AWS',
      theme: ThemeData(

        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Questionário de práticas para ambientes cloud AWS'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late MaquinaEstado maquinaEstado = MaquinaEstado();

  late String perguntaAtual = "";

  @override
  void initState() {
    WidgetsBinding.instance.addPostFrameCallback((_){
      carregarTabela();
    });

    super.initState();
  }

  void carregarTabela() async {
    try {
      await maquinaEstado.validarTabela();
      maquinaEstado.listarControlesPadroes();

      setState(() {
        perguntaAtual = maquinaEstado.getPergunta();
      });
    } catch (e) {
      showDialog(
        context: context,
        builder: (context) => ErrorMessageDialog(
          errorMessage: e.toString(),
        ),
      );
    }
  }

  void respondeuSim() {
    try {
      maquinaEstado.respostaSim();
      getPergunta();
    } on StateError catch (e) {
      print("Erro de Estado: ${e.toString()}");
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => ResultPage(
          recomendacoes: maquinaEstado.controles,
          recomendacoesPadrao: maquinaEstado.controlesPadrao,)),
      );
    } catch (e) {
      showDialog(
        context: context,
        builder: (context) => ErrorMessageDialog(
          errorMessage: e.toString(),
        ),
      );
    }
  }

  void respondeuNao() {
    try {
      maquinaEstado.respostaNao();
      getPergunta();
    } on StateError catch (e) {
      print("Erro de Estado: ${e.toString()}");
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => ResultPage(
          recomendacoes: maquinaEstado.controles, recomendacoesPadrao: maquinaEstado.controlesPadrao)),
      );
    } catch (e) {
      showDialog(
        context: context,
        builder: (context) => ErrorMessageDialog(
          errorMessage: e.toString(),
        ),
      );
    }
  }

  void getPergunta() {
    try {
      setState(() {
        perguntaAtual = maquinaEstado.getPergunta();
      });
    } catch (e) {
      showDialog(
        context: context,
        builder: (context) => ErrorMessageDialog(
          errorMessage: e.toString(),
        ),
      );
    }
  }

  void voltar() {
    try {
      maquinaEstado.voltar();
      getPergunta();
    } catch (e) {
      showDialog(
        context: context,
        builder: (context) => ErrorMessageDialog(
          errorMessage: e.toString(),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            SizedBox(
              height: 150,
              width: MediaQuery.of(context).size.width * 0.75,
              child: Text(
                perguntaAtual,
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.headlineMedium,
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: () => respondeuSim(),
                  style: ElevatedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                  ),
                  child: const Text(
                    "Sim",
                    style: TextStyle(fontSize: 30),
                  ),
                ),
                const SizedBox(width: 50),
                ElevatedButton(
                  onPressed: () => respondeuNao(),
                  style: ElevatedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                  ),
                  child: const Text(
                    "Não",
                    style: TextStyle(fontSize: 30),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 50,),
            ElevatedButton.icon(
              onPressed: () => voltar(),
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                elevation: 0
              ),
              icon: const Icon(Icons.arrow_back),
              label: const Text(
                "Voltar",
                style: TextStyle(fontSize: 30),
              ),
            ),
          ],
        ),
      ),
    );
  }

}
