import 'dart:convert';
import 'package:csv/csv.dart';
import 'package:flutter/services.dart' show rootBundle;

class MaquinaEstado {

  int estadoAtual = 1;

  late List<List<String>> tabelaEstado;

  late List<int> estadosPassados = [];

  List<String> controles = [];

  Future<List<List<String>>> lerTabela(String nomeArquivo) async {
    String content = await rootBundle.loadString(nomeArquivo);
    List<List<String>> tabela = const CsvToListConverter(
      shouldParseNumbers: false,
      fieldDelimiter: ",",
      eol: "\n"
    ).convert(content);

    validarTabela(tabela);

    return tabela;
  }

  bool validarTabela(List<List<String>> tabela) {
    var idsEncontrados = <String>{};
    var perguntasEncontradas = <String>{};

    for (var numLinha = 1; numLinha < tabela.length; numLinha++) {
      var linha = tabela[numLinha];
      if (linha[0].isEmpty) {
        throw("Erro: O campo ID é obrigatório e está vazio (Erro na linha "
            "${numLinha + 1}).");
      } else {
        // Verificar IDs duplicados
        var idAtual = linha[0];
        if (idsEncontrados.contains(idAtual)) {
          throw("Erro: ID '$idAtual' duplicado encontrado na linha ${numLinha +
              1}.");
        } else {
          idsEncontrados.add(idAtual);
        }
      }

      if (linha[1].isEmpty) {
        throw("Erro: O campo Perguntas é obrigatório e está vazio (Erro na linha "
                "${numLinha + 1}).");
      } else {
        // Verificar perguntas duplicados
        var perguntaAtual = linha[1];
        if (perguntasEncontradas.contains(perguntaAtual)) {
          throw("Erro: Pergunta '$perguntaAtual' duplicada encontrada na linha "
                  "${numLinha + 1}.");
        } else {
          perguntasEncontradas.add(perguntaAtual);
        }
      }

      if (linha[2].isEmpty && linha[3].isEmpty) {
        throw("Erro: O campo Recomendações é obrigatório e está vazio (Erro na linha "
            "${numLinha + 1}).");
      }
    }

    tabelaEstado = tabela;

    return true;
  }

  String getPergunta() {
    return tabelaEstado[estadoAtual][1];
  }

  void respostaSim() {
    var controlesSim = tabelaEstado[estadoAtual][2];

    controles.addAll(controlesSim.split("\n").where((c) =>
    c.trim().isNotEmpty));
    estadoAtual =
        encontrarIndicePorId(tabelaEstado, tabelaEstado[estadoAtual][4]);
  }

  void respostaNao() {
    var controlesNao = tabelaEstado[estadoAtual][3];

    controles.addAll(controlesNao.split("\n").where((c) =>
      c.trim().isNotEmpty));
    estadoAtual =
        encontrarIndicePorId(tabelaEstado, tabelaEstado[estadoAtual][5]);
  }

  // void maquinaDeEstado(List<List<String>> tabelaEstado) {
  //   // while (estadoAtual < tabelaEstado.length) {
  //   print("Estado atual: $estadoAtual");
  //   var pergunta = tabelaEstado[estadoAtual][1];
  //   var controlesSim = tabelaEstado[estadoAtual][2];
  //   var controlesNao = tabelaEstado[estadoAtual][3];
  //   print("Pergunta: $pergunta");
  //   var resposta = "sim";
  //
  //   if (resposta == 'sim') {
  //     controles.addAll(controlesSim.split("\n").where((c) =>
  //       c.trim().isNotEmpty));
  //     estadoAtual =
  //         encontrarIndicePorId(tabelaEstado, tabelaEstado[estadoAtual][4]);
  //   } else if (resposta == 'não' || resposta == 'nao') {
  //     controles.addAll(controlesNao.split("\n").where((c) =>
  //       c.trim().isNotEmpty));
  //     estadoAtual =
  //         encontrarIndicePorId(tabelaEstado, tabelaEstado[estadoAtual][5]);
  //   } else {
  //     print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.");
  //     // continue;
  //   }
  //
  //   print("Controles aplicáveis:\n $controles\n");
  // // }
  //
  //   controles.removeWhere((control) => control.isEmpty);
  //
  //   // var output = webFile.File('output.txt');
  //   // output.writeAsStringSync(controles.join('\n'));
  // }

  int encontrarIndicePorId(List<List<String>> tabela, String idDesejado) {
    for (var indice = 0; indice < tabela.length; indice++) {
      if (tabela[indice][0] == idDesejado) {
        return indice;
      }
    }
    throw StateError("Não há mais perguntas no estado atual.");
  }
}
