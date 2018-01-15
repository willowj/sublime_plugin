#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-01-13 16:56:26
#


import sublime
import sublime_plugin



class New_file2(sublime_plugin.TextCommand):
    """customise new_file"""

    def run(self, edit):
        window = sublime.active_window()
        view = window.new_file()
        view.set_name('name.py')
        view.run_command("insert_snippet",
                         {"contents":
                          '#!/usr/bin/python\n'
                          '# -*- coding: utf-8 -*-\n'
                          '#author: willowj\n'
                          '#license: MIT\n'
                          '#date: ' + datetime.datetime.now(
                          ).strftime("%Y-%m-%d %H:%M:%S")+'\n'
                          }
                         )
        view.set_syntax_file(
            "Packages/Python/Python.sublime-syntax")
        # if not exist, need to down  '.tmLanguage', or '.sublime-syntax'
        # syntax file



'''# monitor all new file
class New_file_config(sublime_plugin.EventListener):

    def on_new(self, view):
        view.run_command("insert_snippet",
                         {"contents": '#coding:utf8'}  # <<<
                         )
        view.set_name('na.py')  # <<<
        # <<<  Syntax tmLanguage
        # view.set_syntax_file(
        #     "Packages/Python/Python.sublime-syntax")

'''
