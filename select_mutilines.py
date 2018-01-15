#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-01-12 21:11:24
#


class select_mutiline(sublime_plugin.TextCommand):
    """select mutiline"""
    '''### eg select 2 lines by "ctrl+up/down"
    {"keys": ["ctrl+up"], "command": "select_mutiline" ,

        "args": {"forward": false, "line_s": 2, "self_line": true}
    },

    {"keys": ["ctrl+down"], "command": "select_mutiline" ,

        "args": {"forward": true, "line_s": 2, "self_line": true}
    },

    '''
    def run(self, edit, line_s=3, forward=False, self_line=True):

        selection = self.view.sel()


        near_region = selection[forward and -1 or 0]
        selects0 = selection[0]

        end = forward and near_region.end() or near_region.begin()
        row, col = self.view.rowcol(end)
        if selects0.empty() and self_line:
            if not forward :
                row += 1

        start_row = row + line_s*(forward or -1)
        new_region = sublime.Region(self.view.text_point(
            start_row, 0), self.view.text_point(row, 0))
        selection.add(new_region)
