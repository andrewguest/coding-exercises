import 'dart:convert';
import 'dart:io';

void part_1() async {
  List<String> file_contents = [];
  int max_elf_calories = 0;

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

  int current_calories_total = 0;

  // Loop through the calories until we reach a blank line
  for (var i = 0; i < file_contents.length; i++) {
    if (file_contents[i].length == 0) {
      if (current_calories_total > max_elf_calories) {
        max_elf_calories = current_calories_total;
      }
      current_calories_total = 0;
    } else {
      current_calories_total += int.parse(file_contents[i]);
    }
  }

  print(max_elf_calories);
}

void part_2() async {
  List<String> file_contents = [];

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

  List<int> elf_calories = [];
  int current_calories_total = 0;

  // Loop through the calories until we reach a blank line
  for (var i = 0; i < file_contents.length; i++) {
    if (file_contents[i].length == 0) {
      elf_calories.add(current_calories_total);
      current_calories_total = 0;
    } else {
      current_calories_total += int.parse(file_contents[i]);
    }
  }

  elf_calories.sort((b, a) => a.compareTo(b));
  print(elf_calories.sublist(0, 3).reduce((a, b) => a + b));
}

void main() {
  part_1();
  part_2();
}
