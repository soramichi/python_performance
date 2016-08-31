for p in `seq 1 8`; do
    echo $p
    sed -i -e "s/###/(((${p})))/" gemv.py
    /home/soramichi/anaconda3/bin/python ./gemv.py
    sed -i -e "s/(((${p})))/###/" gemv.py
done
