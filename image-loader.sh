echo "image loader"
echo "what image you loaded"
#if statement
if [ "$1" == "win11" ]; then
    echo "you loaded win11"
elif [ "$1" == "win10" ]; then
    echo "you loaded win10"
elif ["$1" == "macos"]; then
    echo "image not loaded"
else
    echo "you loaded something else"
fi