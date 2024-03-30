wget --spider --quiet http://example.com

if [ "$?" != 0 ]; then
    echo -n "NC"
else
    out=$(curl http://hotspot.sbu.ac.ir/status 2>/dev/null | grep "خوش آمدید" | awk '{print $5}')
    user=${out%"</div><br>"}
    echo -n $user
fi