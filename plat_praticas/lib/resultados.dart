import 'package:flutter/material.dart';

class ResultPage extends StatelessWidget {
  final List<ResultItem> results;

  const ResultPage({super.key, required this.results});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Results'),
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
                      style: TextStyle(fontSize: 16),
                    ),
                    SizedBox(height: 8),
                    Text(
                      'Link: ${results[index].link}',
                      style: TextStyle(fontSize: 16),
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

void main() {
  runApp(MaterialApp(
    home: ResultPage(
      results: [
        ResultItem(description: 'Description 1', link: 'Link 1'),
        ResultItem(description: 'Description 2', link: 'Link 2'),
        ResultItem(description: 'Description 3', link: 'Link 3'),
        // Add more ResultItems here as needed
      ],
    ),
  ));
}
