# coding:utf8
import sublime
import sublime_plugin
import datetime
import re

debug = True

if debug:
    sublime.log_input(True)
    sublime.log_commands(True)


class AddCurrentTime(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command("insert_snippet",
                              {"contents": "#%s" % datetime.datetime.now(
                              ).strftime("%Y-%m-%d %H:%M:%S")}  # <<<
                              )


# --------------------------------------------------
class AddSplitLine(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command("insert_snippet", {"contents": "#"+'-'*50}
                              )


class Wrap_3comma(sublime_plugin.TextCommand):
    '''#wrap with  3comma: ~ for '
    if selected wrap or unwrap
        |1   ~~~#
        |2   selected code
        |3   ~~~
    not selected:
        insert or delete ''''''
        notice: wrap in wrap will split 2 comment parts
    '''

    def run(self, edit):
        view = self.view
        selects = view.sel()
        if len(selects) > 0:
            selects = selects[0]    # 获取以一个选中区域
            print(type(selects))

        wrap_ = True
        if selects.empty():
            line = view.line(selects)
            region_str = view.substr(line)
            if re.match("'''[\s\S]*?\n?'''" , region_str):  # unwap
                wrap_ = False
                content_ = region_str.replace("'''", "")
            else:  # wrap > insert ,need't cut
                content_ = "''''''"
        else:  # selected
            region_str = view.substr(selects)  # 获取选中区域内容
            words = region_str.strip()  # .strip('\n')
            if words.startswith("'''") and words.endswith("'''"):  # unwrap #<<<
                wrap_ = False
                content_ = region_str.replace("'''", "") +'\n'

            else:  # wrap
                lines = view.lines(selects)
                # keep indent space if select
                for line in lines:
                    _ = view.substr(line)
                    if any(map(lambda x: x != ' ', _)):
                        first_line = _
                        break
                space = 0
                for i in first_line:
                    if i == ' ':
                        space += 1
                    else:
                        break
                content_ = "{spaces}'''###\n{old_text}\n{spaces}'''\n".format(
                    old_text=region_str, spaces=" "*space)  # <<<

        # view.replace(edit,selects, content_) #只能替换，不能直接插入
        clip_backup = sublime.get_clipboard()
        if not(selects.empty() and wrap_):
            view.run_command('cut')
        self.view.run_command("insert_snippet", {"contents": content_}
                              )
        sublime.set_clipboard(clip_backup)


        # move to center if wrap str self.view.sel().clear()
        if wrap_:
            for _ in range(4 - selects.empty()):  # if insert, move 3 to center
                self.view.run_command("move", {"by": "characters",
                                               "extend": False,
                                               "forward": False, }
                                      )


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
