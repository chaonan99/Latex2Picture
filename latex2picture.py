import sublime, sublime_plugin, urllib

def selections(view, default_to_all=True):
    """
    Return all non-empty selections in view
    If None, return entire view if default_to_all is True
    code from: https://github.com/mastahyeti/URLEncode
    """
    regions = [r for r in view.sel() if not r.empty()]

    if not regions and default_to_all:
        regions = [sublime.Region(0, view.size())]

    return regions

def quote(view, s):
    return "![equation](http://latex.codecogs.com/svg.latex?" + urllib.parse.quote(s, safe='') + ")"

class LatexPictureCommand(sublime_plugin.TextCommand):
    """
    Main logic
    """
    def run(self, edit):
        view = self.view
        for region in selections(view):
            s = view.substr(region)
            view.replace(edit, region, quote(view, s))
