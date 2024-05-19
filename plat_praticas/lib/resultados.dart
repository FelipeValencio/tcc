import 'package:flutter/material.dart';
import 'package:plat_praticas/util.dart';
import 'package:url_launcher/url_launcher.dart';

import 'mensagemErro.dart';

class ResultPage extends StatelessWidget {

  late List<String> recomendacoes;

  late List<List<String>> tabelaRecomendacoes;

  ResultPage({super.key, required this.recomendacoes});

  Future<List<ResultItem>> buildResults() async {
    tabelaRecomendacoes = await Util.lerTabela("tabela_recomendacoes.csv");

    List<ResultItem> results = [];

    for (String r in recomendacoes){
      int indiceRec = Util.encontrarIndicePorId(tabelaRecomendacoes, r);
      results.add(ResultItem(
        recomendacao: tabelaRecomendacoes[indiceRec][0],
        prioridade: tabelaRecomendacoes[indiceRec][3],
        descricao: tabelaRecomendacoes[indiceRec][2],
        link: tabelaRecomendacoes[indiceRec][1]),
      );
    }

    return results;
  }

  Widget customExpansionTile(ResultItem item, BuildContext context) {
    return Column(
      children: [
        SizedBox(
          width: MediaQuery.of(context).size.width * 0.80,
          child: Card(
            elevation: 2, // Adjust elevation to match the card
            margin: EdgeInsets.zero, // Remove default card margin
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(4), // Adjust border radius to match the card
              side: BorderSide(color: Colors.grey.shade200), // Match the card's border color
            ),
            child: IntrinsicHeight(
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Container(
                    width: 5,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(4),
                      color: definirCor(item.prioridade),
                    ),
                  ),
                  Flexible(
                    child: Theme(
                      data: ThemeData().copyWith(dividerColor: Colors.transparent),
                      child: ExpansionTile(
                        iconColor: definirCor(item.prioridade),
                        title: Text(
                          item.recomendacao,
                          overflow: TextOverflow.ellipsis,
                        ),
                        collapsedIconColor: definirCor(item.prioridade),
                        children: [
                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 16.0),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  'Descrição: ${item.descricao}',
                                  style: const TextStyle(fontSize: 16),
                                ),
                                const SizedBox(height: 8),
                                InkWell(
                                  onTap: () => launchUrl(Uri.parse(item.link)),
                                  child: Text(
                                    item.link,
                                    style: const TextStyle(
                                      fontSize: 16,
                                      color: Colors.blueAccent,
                                      decoration: TextDecoration.underline,
                                    ),
                                  ),
                                ),
                                Row(
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  children: [
                                    const Text(
                                      'Prioridade de implementação: ',
                                      style: TextStyle(
                                          fontSize: 16,
                                          fontWeight: FontWeight.bold
                                      ),
                                    ),
                                    Text(
                                      item.prioridade.trim(),
                                      style: TextStyle(
                                          fontSize: 16,
                                          color: definirCor(item.prioridade)
                                      ),
                                    ),
                                  ],
                                )
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
        const SizedBox(height: 10),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Resultados'),
      ),
      body: FutureBuilder<List<ResultItem>>(
        future: buildResults(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            WidgetsBinding.instance.addPostFrameCallback((_) {
              showDialog(
                context: context,
                builder: (context) => ErrorMessageDialog(
                  errorMessage: snapshot.error.toString(),
                ),
              );
            });
            return const SizedBox.shrink();
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            WidgetsBinding.instance.addPostFrameCallback((_) {
              showDialog(
                context: context,
                builder: (context) => const ErrorMessageDialog(
                  errorMessage: "Falha ao carregar os dados de resultado",
                ),
              );
            });
            return const SizedBox.shrink();
          }

          // Ordena os dados por prioridade
          snapshot.data!.sort((a, b) {
            // Define a ordem de prioridade: Alta > Média > Baixa
            Map<String, int> priorityOrder = {'Alta': 3, 'Média': 2, 'Baixa': 1};

            return priorityOrder[b.prioridade.trim()]!.compareTo(priorityOrder[a.prioridade.trim()]!);
          });

          return ListView.builder(
            itemCount: snapshot.data!.length,
            itemBuilder: (context, index) {
              return customExpansionTile(snapshot.data![index], context);
            },
          );
        },
      ),
    );
  }

  Color definirCor(String prioridade) {
    switch (prioridade.trim()) {
      case 'Alta':
        return Colors.redAccent.shade200; // You can change this color according to your preference
      case 'Média':
        return Colors.amber; // You can change this color according to your preference
      case 'Baixa':
        return Colors.lightGreen.shade200; // You can change this color according to your preference
      default:
        return Colors.black; // Default color
    }
  }

}

class ResultItem {
  final String recomendacao;
  final String descricao;
  final String link;
  final String prioridade;

  ResultItem({required this.recomendacao,
    required this.descricao, required this.link,
    required this.prioridade});
}
