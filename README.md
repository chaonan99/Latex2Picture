# Latex to Picture (or image if you like...)
This is a plug-in for sublime3 (Just 3 now!!!) to convert a formula in latex grammar to an url, which will show the picture of your equation. This is useful when markdown don't support latex equation, like in a GitHub README.

## How to install
Of cource you can't install via package control. You should copy this repo to your sublime package folder. To find where the folder is, open default key binding file in `Preferences -> Key Bindings - Default` and hover your mouse pointer on the item bar of that file. You may see something like `xxx\xxx\Packages\` stop at Packages! Put the repo there.

## Usage
> This code is a complement for [this](https://chaonan99.github.io/2016/how-to-add-equation-on-github-markdown-file/) blog post which tells you more principles.

1. Write equation in latex grammar, like `gain = talent + \sum_{n=today}^{\infty}\sigma(work)`.
2. Select the equation and press <kbd>ctrl</kbd>+<kbd>alt</kbd>+<kbd>shift</kbd>+<kbd>u</kbd> (no conflict ... god bless me ...).
3. It change the equation into `![equation](http://latex.codecogs.com/svg.latex?gain%20%3D%20talent%20%2B%20%5Csum_%7Bn%3Dtoday%7D%5E%7B%5Cinfty%7D%5Csigma%28work%29)`. Picture looks like this:

![equation](http://latex.codecogs.com/svg.latex?gain%20%3D%20talent%20%2B%20%5Csum_%7Bn%3Dtoday%7D%5E%7B%5Cinfty%7D%5Csigma%28work%29)

## Acknowledge
This code referred [this](https://github.com/mastahyeti/URLEncode) repo, which is a usable URL encoder-decoder plug-in for sublime 2&3.

## License
MIT license.