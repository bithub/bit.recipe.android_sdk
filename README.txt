

With this package you can add a part like the following to your buildout.

This will install a script bit/my_android_sdk, which can be used for installing the android sdk, like so:

./bin/my_android_sdk install

[my_android_sdk]
recipe = bit.recipe.android_sdk
apis = 8
sdk = http://dl.google.com/android/android-sdk_r14-linux.tgz


