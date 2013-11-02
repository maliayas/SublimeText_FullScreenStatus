import sublime, sublime_plugin

def plugin_loaded():
    # Set flags to `false` on plugin load.
    set_setting('fss_on_full_screen', False)
    set_setting('fss_on_distraction_free', False)

def plugin_unloaded():
    remove_setting('fss_on_full_screen')
    remove_setting('fss_on_distraction_free')

def get_setting(setting):
    return sublime.active_window().settings().get(setting)

def set_setting(setting, value):
    sublime.active_window().settings().set(setting, value)

def remove_setting(setting):
    sublime.active_window().settings().erase(setting)

class ToggleFullScreenWrapperCommand(sublime_plugin.WindowCommand):
    def run(self):
        if get_setting('fss_on_full_screen'):
            set_setting('fss_on_full_screen', False)

        elif get_setting('fss_on_distraction_free'):
            set_setting('fss_on_distraction_free', False)

        else:
            set_setting('fss_on_full_screen', True)

        self.window.run_command("toggle_full_screen")

class ToggleDistractionFreeWrapperCommand(sublime_plugin.WindowCommand):
    def run(self):
        if get_setting('fss_on_distraction_free'):
            set_setting('fss_on_distraction_free', False)

        else:
            set_setting('fss_on_full_screen', False)
            set_setting('fss_on_distraction_free', True)

        self.window.run_command("toggle_distraction_free")
