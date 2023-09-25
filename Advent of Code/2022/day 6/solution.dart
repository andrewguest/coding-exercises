import 'dart:convert';
import 'dart:io';

Future<List<String>> read_input_file({String filename = "./input.txt"}) async {
  /*
    Read `filename` and return an array containing each line of the file. Each line
      in the file is returned as an entry in the array.
  */
  List<String> file_contents = [];
  final file = File(filename);

  if (await file.exists()) {
    final linesStream = file.openRead();
    await for (var line
        in linesStream.transform(Utf8Decoder()).transform(LineSplitter())) {
      file_contents.add(line);
    }
  }

  return file_contents;
}

void part_1() async {
  // Read the input file
  var file_contents = await read_input_file();
  String input_string = file_contents[0];

  // Define variables
  int packet_start_index = 0;
  int start_index = 0;
  int end_index = 4;

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
  // Read the input file
  var file_contents = await read_input_file();
  String input_string = file_contents[0];

  // Define variables
  int packet_start_index = 0;
  int start_index = 0;
  int end_index = 14;

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
