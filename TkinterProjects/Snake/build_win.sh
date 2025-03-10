BUILD_DIR="build"
DIST_DIR="dist"
APP_SPEC="app.spec"

if [ -d "$BUILD_DIR" ]; then
  rm -rf "$BUILD_DIR"
fi
if [ -d "$DIST_DIR" ]; then
  rm -rf "$DIST_DIR"
fi

if [ -f "$APP_SPEC" ]; then
  rm "$APP_SPEC"
fi


pyinstaller app.py --add-data "assets;assets" --windowed