import 'dart:convert';
import 'dart:io';

void part_1() async {
  List<String> file_contents = [];
  int packet_start_index = 0;
  int start_index = 0;
  int end_index = 4;

  // Read the input file
  var file_path = "./input.txt";
  final file = File(file_path);

  if (await file.exists()) {
    final linesStream = file.openRead();
    await for (var line
        in linesStream.transform(Utf8Decoder()).transform(LineSplitter())) {
      file_contents.add(line);
    }
  }

  String input_string = file_contents[0];

  while (packet_start_index == 0) {
    var current_substring = input_string.substring(start_index, end_index);
    List<String> current_substring_as_array = current_substring.split("");
    Set<String> current_substring_as_set = current_substring_as_array.toSet();

    if (current_substring_as_array.length == current_substring_as_set.length) {
      packet_start_index = end_index;
      break;
    } else {
      start_index += 1;
      end_index += 1;
    }
  }

  print(packet_start_index);
}

void part_2() async {
  List<String> file_contents = [];
  int packet_start_index = 0;
  int start_index = 0;
  int end_index = 14;

  // Read the input file
  var file_path = "./input.txt";
  final file = File(file_path);

  if (await file.exists()) {
    final linesStream = file.openRead();
    await for (var line
        in linesStream.transform(Utf8Decoder()).transform(LineSplitter())) {
      file_contents.add(line);
    }
  }

  String input_string = file_contents[0];

  while (packet_start_index == 0) {
    var current_substring = input_string.substring(start_index, end_index);
    List<String> current_substring_as_array = current_substring.split("");
    Set<String> current_substring_as_set = current_substring_as_array.toSet();

    if (current_substring_as_array.length == current_substring_as_set.length) {
      packet_start_index = end_index;
      break;
    } else {
      start_index += 1;
      end_index += 1;
    }
  }

  print(packet_start_index);
}

void main() {
  part_1();
  part_2();
}
