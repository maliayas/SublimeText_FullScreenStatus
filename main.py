import sublime, sublime_plugin, os

plugin_installed_marker = None
full_screen_marker      = None
distraction_free_marker = None

def plugin_loaded():
    global plugin_installed_marker, full_screen_marker, distraction_free_marker

    # Marker files.
    plugin_installed_marker = sublime.cache_path() + os.sep + ".fs-status-installed"
    full_screen_marker      = sublime.cache_path() + os.sep + ".on-full-screen"
    distraction_free_marker = sublime.cache_path() + os.sep + ".on-distraction-free"

    # Put a marker that indicates this plugin is installed. Otherwise, absence of
    # `full_screen_marker` and `distraction_free_marker` wouldn't have a meaning.
    open(plugin_installed_marker, "w+")

    # Remove any markers on startup that may be left from the previous session. Because
    # ST can't start on full screen or distraction free mode.
    try:
        os.remove(full_screen_marker)
        os.remove(distraction_free_marker)
    except:
        pass

class ToggleFullScreenWrapperCommand(sublime_plugin.WindowCommand):
    def run(self):
        if os.path.exists(full_screen_marker):
            os.remove(full_screen_marker)

        elif os.path.exists(distraction_free_marker):
            os.remove(distraction_free_marker)

        else:
            open(full_screen_marker, "w+")

        self.window.run_command("toggle_full_screen")

class ToggleDistractionFreeWrapperCommand(sublime_plugin.WindowCommand):
    def run(self):
        if os.path.exists(distraction_free_marker):
            os.remove(distraction_free_marker)

        else:
            if os.path.exists(full_screen_marker):
                os.remove(full_screen_marker)

            open(distraction_free_marker, "w+")

        self.window.run_command("toggle_distraction_free")
