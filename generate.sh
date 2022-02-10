#!/bin/bash
function random() {
    s='A-Za-z0-9!"#$%&'\''()*+,-./:;<=>?@[\]^_`{|}~'
    p=$((RANDOM % ${#s}))
    echo -n ${s:$p:1}
}

for i in $(eval echo {0..$1}); do
    echo -n `random`
done
