# FullScreenStatus

_FullScreenStatus_ is a Sublime Text plugin that is designed to be used by other plugins. It helps to detect if Sublime Text is running on __full screen__ mode, __distraction free__ mode or normal mode. Current Sublime Text version (ST 3 Build 3047) does _not_ provide this information via its API.

## Overview

* [Installation](#installation)
* [Usage](#usage)
* [Source](#source)
* [License](#license)

## Installation

#### [Package Control](https://sublime.wbond.net/installation)

The preferred method of installation is via [Sublime Package Control](https://sublime.wbond.net/installation).

1. Install [Package Control](https://sublime.wbond.net/installation)
2. Open command palette with <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>P</kbd>
3. Type `install package` and hit return. A list of available packages will be displayed.
4. Type `FullScreenStatus` and hit return. The package will be downloaded into the appropriate directory.

#### Using Git

1. Go to your `Packages` directory. You can locate your `Packages` directory by using the menu item _Preferences > Browse Packages..._
2. Inside the `Packages` directory, clone FullScreenStatus repository using the command below:

        git clone https://github.com/maliayas/SublimeText_FullScreenStatus.git FullScreenStatus

## Usage

```py
import sublime

if sublime.active_window().settings().get('fss_on_full_screen'):
    # ST is running on full screen.

if sublime.active_window().settings().get('fss_on_distraction_free'):
    # ST is running on distraction free mode.
```

## Source

Source code of this project is hosted at https://github.com/maliayas/SublimeText_FullScreenStatus. Contributions are welcome via pull requests.

## License

FullScreenStatus is released under the [MIT License](http://www.opensource.org/licenses/MIT).
