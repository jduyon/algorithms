f(){
  sort ~/Desktop/Projects/Algorithms/IntegerArray.txt > test1.txt
}

g(){
  python quicksort2.py -i ~/Desktop/Projects/Algorithms/IntegerArray.txt > test.txt
}

h(){
  python mergesort_count_inversions.py > test.txt
}

randomselection(){
  for i in `seq -w 100`;
    do
      python randomselection.py
    done
}

#time f
#time g
#time h

time randomselection
