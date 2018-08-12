read N
a=0
for ((i=0;i<N;i++))
do
    read I
    a=$(bc -l <<< $a+$I)
done
printf "%.3f" $(bc -l <<< $a/$N)

# Testers code
# arithmetic $(())
read n
sum=0
for ((i=0;i<$n;i++))
do
    read temp
    sum=`$(($`sum+$temp))
done
printf "%.3f\n" `$(bc -l <<< "$`sum/$n")
