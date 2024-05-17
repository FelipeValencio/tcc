import 'package:flutter/material.dart';

class ResultPage extends StatelessWidget {

  List<String> resultados;

  late List<ResultItem> results = [];

  ResultPage({super.key, required this.resultados}) {
    buildResults();
  }

  void buildResults() {
    results.clear();
    for (String r in resultados){
      results.add(ResultItem(description: r, link: 'Link 1'));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Resultados'),
      ),
      body: ListView.builder(
        itemCount: results.length,
        itemBuilder: (context, index) {
          return ExpansionTile(
            title: Text(results[index].description),
            children: [
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Description: ${results[index].description}',
                      style: const TextStyle(fontSize: 16),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      'Link: ${results[index].link}',
                      style: const TextStyle(fontSize: 16),
                    ),
                  ],
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}

class ResultItem {
  final String description;
  final String link;

  ResultItem({required this.description, required this.link});
}
