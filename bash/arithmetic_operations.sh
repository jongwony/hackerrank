read N
echo $N | bc -l | awk '{ printf "%.3f\n'

# Tester's code "<<<: man heredoc"
read a
printf "%.3f\n" $(bc -l <<< $a)

