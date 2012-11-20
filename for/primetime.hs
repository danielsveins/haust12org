--Notkun: isPrimeUsingPrimeList primelist n
--Fyrir: n er heiltala, n >= 2
--        primelist er eithva hali af óendanlega lista 
--       [2,3,5,7..]
--Gildi: True ef n er prímtala, annars False

let isPrimeUsingPrimeList (k:ks) n =
    if k*k > n then
        True
    else if (mod n k) == 0 then
        False
    else
        isPrimeUsingPrimeList  ks n

let primeList =
    [2,3]++(filter (\n -> isPrimeUsingPrimeList PrimeList n) [5,7..]

--Notkun: isPrime n
--Notkun: n er heiltala
--Gildi: True ef n er prímtala, annars False
let isPrime n =
     if n<2 then
        False
     else
        isPrimeUsingPrimeList primeList n

