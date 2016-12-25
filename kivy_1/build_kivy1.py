# builds the kivy application using python-for-android

__author__ = 'sidmishraw'

# Adjust the paths!
# export ANDROIDSDK="$HOME/Documents/android-sdk-21"
# export ANDROIDNDK="$HOME/Documents/android-ndk-r10e"
# export ANDROIDAPI="14"  # Minimum API version your application require
# export ANDROIDNDKVER="r10e"  # Version of the NDK you installed
def main():
  'this is the main entry point for the script'
  '''p4a apk --private $HOME/code/myapp --package=org.example.myapp \
  --name "My application" --version 0.1 --bootstrap=sdl2 \
  --requirements=python2,kivy --sdk_dir $ANDROIDSDK --ndk_dir $ANDROIDNDK \
  --android_api $ANDROIDAPI --ndk_ver $ANDROIDNDKVER'''

  pass



if __name__ == '__main__':
  main()