import 'package:csv/csv.dart';
import 'package:flutter/services.dart';

class Util {

  static Future<List<List<String>>> lerTabela(String nomeArquivo) async {
    String content = await rootBundle.loadString("/assets/$nomeArquivo");
    List<List<String>> tabela = const CsvToListConverter(
        shouldParseNumbers: false,
        fieldDelimiter: ",",
        eol: "\n"
    ).convert(content);

    return tabela;
  }

  static int encontrarIndicePorId(List<List<String>> tabela, String idDesejado) {
    for (var indice = 1; indice < tabela.length; indice++) {
      if (idDesejado.trim().isEmpty) {
        throw StateError("Não há mais perguntas no estado atual.");
      }
      else if (tabela[indice][0].trim().contains(idDesejado.trim())) {
        return indice;
      }
    }
    throw StateError("Não há mais perguntas no estado atual.");
  }

}