for i in macOS/*.iconset/ ; do
  iconutils --convert  "$i"
done
rm -R macOS/*.iconset/
