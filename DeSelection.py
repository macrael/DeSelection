#!/usr/bin/env python3

import sublime
import sublime_plugin

class DeleteSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        event = kwargs['event']
        cursor_vector = (event['x'], event['y'])
        cursor_point = self.view.window_to_text(cursor_vector)

        cursor_region = sublime.Region(cursor_point, cursor_point)
        regions_to_remove = []

        didSubtract = False
        for selected_region in self.view.selection:
            if selected_region.contains(cursor_region):
                didSubtract = True
                self.view.selection.subtract(selected_region)

        if not didSubtract:
            kwargs['additive'] = True
            self.view.run_command("drag_select", kwargs)


    def want_event(self):
        return True

