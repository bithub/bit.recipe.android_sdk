
bit.recipe.android_sdk
======================

With this package you can add a part like the following to your buildout.

[my_android_sdk]
recipe = bit.recipe.android_sdk
apis = 8
sdk = http://dl.google.com/android/android-sdk_r14-linux.tgz

This will install the android sdk into the folder parts/my_android_sdk within your buildout

It will also download android platform-tools and the apis listed in the buildout


