import 'dart:mirrors';

void main() {
  final DateTime startDate = DateTime.parse('1901-01-01');
  final DateTime endDate = DateTime.parse('2000-12-31');
  DateTime currrentDate = startDate;
  int numberOfSundays = 0;

  // While `currentDate` is before or on endDate
  while (currrentDate.compareTo(endDate) <= 0) {
    if ((currrentDate.weekday == 6) && (currrentDate.day == 1)) {
      numberOfSundays += 1;
    }
    currrentDate = currrentDate.add(Duration(days: 1));
  }

  print(numberOfSundays);
}
