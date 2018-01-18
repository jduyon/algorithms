unsorted_integers=../files/IntegerArray.txt
f(){
  sort ${unsorted_integers} > /dev/null
}

g(){
  python ../sorts/quicksort.py -i ${unsorted_integers} > /dev/null
}

h(){
  python ../sorts/merge_sort.py -i  ${unsorted_integers} > /dev/null
}

randomselection(){
  for i in `seq -w 100`;
    do
      python randomselection.py
    done
}

echo "Bash sort"
time f
echo "Quick Sort"
time g
Echo "Merge Sort"
time h

#time randomselection
