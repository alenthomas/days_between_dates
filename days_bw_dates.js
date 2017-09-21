const daysInMonth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31};

let isLeapYear = (year) => {
  return (year%4 === 0 && year%100 !== 0) ||
         (year%400 === 0) ? true : false;
};

let getDaysInMonth = (month, year) => {
  if (month === 2)
    return isLeapYear(year) ? 29 : 28;
  return daysInMonth[month];
};

let daysBetDays = (d1, m1, y1, d2, m2, y2, accumulator) => {
  if (y1 === y2 && m1 === m2)
   return accumulator + d2 - d1;
  accumulator += getDaysInMonth(m1, y1) - d1 + 1;
  if (m1 == 12)
    m1 = 1, y1 += 1;
  else
    m1 += 1;
  return daysBetDays(1, m1, y1, d2, m2, y2, accumulator);
};

let days = daysBetDays(24, 11, 1986, 21, 9, 2017, 0);
//let days = daysBetDays(1, 11, 1992, 5, 1, 1993, 0);
//let days = daysBetDays(1, 1, 1993, 1, 1, 1993, 0);
console.log(days);
