#!/usr/bin/env python3

import sublime
import sublime_plugin

class DeleteSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, event):
        cursor_vector = (event['x'], event['y'])
        cursor_point = self.view.window_to_text(cursor_vector)

        cursor_region = sublime.Region(cursor_point, cursor_point)
        regions_to_remove = []
        for selected_region in self.view.selection:
            if selected_region.contains(cursor_region):
                regions_to_remove.append(selected_region)

        if len(self.view.selection) == len(regions_to_remove):
            self.view.selection.clear()
        else:
            for region in regions_to_remove:
                self.view.selection.subtract(region)

    def want_event(self):
        return True

