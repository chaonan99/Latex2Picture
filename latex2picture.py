import sublime, sublime_plugin, urllib

def quote(s):
    return "![equation](http://latex.codecogs.com/svg.latex?" + urllib.parse.quote(s, safe='') + ")"

class LatexPictureCommand(sublime_plugin.TextCommand):
    """
    Main logic
    """
    def run(self, edit):
        view = self.view
        s = []
        for region in view.sel():
            if not region.empty():
                s = view.substr(region)
                re = quote(s)
                view.replace(edit, region, re)
