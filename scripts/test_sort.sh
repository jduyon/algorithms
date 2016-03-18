unsorted_integers=../files/IntegerArray.txt
f(){
  sort ${unsorted_integers} > /dev/null
}

g(){
  python ../sorts/quicksort2.py -i ${unsorted_integers} > /dev/null
}

h(){
  python ../sorts/mergesort_count_inversions.py > /dev/null
}

randomselection(){
  for i in `seq -w 100`;
    do
      python randomselection.py
    done
}

time f
time g
time h

#time randomselection
