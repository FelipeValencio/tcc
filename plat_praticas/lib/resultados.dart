import 'package:flutter/material.dart';
import 'package:plat_praticas/util.dart';
import 'package:url_launcher/url_launcher.dart';

class ResultPage extends StatelessWidget {

  late List<String> recomendacoes;

  late List<List<String>> tabelaRecomendacoes;

  ResultPage({super.key, required this.recomendacoes});

  Future<List<ResultItem>> buildResults() async {
    tabelaRecomendacoes = await Util.lerTabela("/tabela_recomendacoes.csv");

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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Resultados'),
      ),
      body: FutureBuilder<List<ResultItem>>(
        future: buildResults(),
        builder: (context, snapshot) {
          if(!snapshot.hasData) {
            return const Center(child: CircularProgressIndicator());
          }

          // Sort the snapshot.data list based on priority
          snapshot.data!.sort((a, b) {
            // Define priority order: High > Medium > Low
            Map<String, int> priorityOrder = {'Alta': 3, 'Média': 2, 'Baixa': 1};

            return priorityOrder[b.prioridade.trim()]!.compareTo(priorityOrder[a.prioridade.trim()]!);
          });

          return ListView.builder(
            itemCount: snapshot.data!.length,
            itemBuilder: (context, index) {
              return Column(
                children: [
                  ExpansionTile(
                    iconColor: definirCor(snapshot.data![index].prioridade),
                    title: Text(snapshot.data![index].recomendacao),
                    collapsedIconColor: definirCor(snapshot.data![index].prioridade),
                    children: [
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 16.0),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              'Descrição: ${snapshot.data![index].descricao}',
                              style: const TextStyle(fontSize: 16),
                            ),
                            const SizedBox(height: 8),
                            InkWell(
                              onTap: () => launchUrl(Uri.parse(snapshot.data![index].link)),
                              child: Text(
                                snapshot.data![index].link,
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
                                  snapshot.data![index].prioridade.trim(),
                                  style: TextStyle(
                                    fontSize: 16,
                                    color: definirCor(snapshot.data![index].prioridade)
                                  ),
                                ),
                              ],
                            )
                          ],
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),
                ],
              );
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
