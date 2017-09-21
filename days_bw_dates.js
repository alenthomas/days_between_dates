let daysBetDays = (d1, m1, y1, d2, m2, y2) => {
  if (y1 === y2 && m1 === m2) {
    return d2 - d1;
  }
  return null;
};

//let days = daysBetDays(26, 8, 1993, 21, 9, 2017);
let days = daysBetDays(21, 8, 1993, 21, 8, 1993);
console.log(days);
