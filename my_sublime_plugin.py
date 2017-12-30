# coding:utf8
import sublime
import sublime_plugin
import datetime
import re

debug = True

if debug:
    sublime.log_input(True)
    sublime.log_commands(True)


class AddCurrentTimeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command("insert_snippet",
                              {"contents": "#%s" % datetime.datetime.now(
                              ).strftime("%Y-%m-%d %H:%M:%S")}  # <<<
                              )


class AddSplitLine(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command("insert_snippet", {"contents": "#"+'-'*50}
                              )


class Wrap_3comma(sublime_plugin.TextCommand):
    '''wrap with '''''' '''

    def run(self, edit):
        view = self.view
        selects = view.sel()
        if len(selects) > 0:
            selects = selects[0]    # 获取以一个选中区域
        if selects.empty():
            line = view.line(selects)
            region_str = view.substr(line)
        else:
            region_str = view.substr(selects)  # 获取选中区域内容

        #print('<', region_str, '>')
        wrap_ = True

        words = region_str.strip()
        if not words:
            content_ = "''' '''"  # wrap
        elif words.startswith("'''") and words.endswith("'''"):  # <<<
            wrap_ = False  # unwrap
            if not selects.empty():
                region_str = re.sub("'''[\s\S]*?\n" , "", region_str) + '\n'
            content_ = region_str.replace("'''", "")
            content_ = content_+'\n'
        else:
            # wrap
            if not selects.empty():
                content_ = "'''>\n%s\n'''\n" % region_str  # <<<
            else:
                content_ = "'''%s'''\n" % region_str

        clip_backup = sublime.get_clipboard()
        if words:
            view.run_command('cut')
        self.view.run_command("insert_snippet", {"contents": content_}
                              )
        sublime.set_clipboard(clip_backup)

        # self.view.sel().clear()
        if selects.empty():
            for _ in range(4):
                self.view.run_command("move", {"by": "characters",
                                               "extend": False,
                                               "forward": False, }
                                      )

'''> monitor

class New_file_config(sublime_plugin.EventListener):

    def on_new(self, view):
        view.run_command("insert_snippet",
                         {"contents": '#coding:utf8'}  # <<<
                         )
        view.set_name('na.py')  # <<<
        # <<<  Syntax tmLanguage
        # view.set_syntax_file(
        #     'Packages/PowerShell/Support/PowershellSyntax.tmLanguage')

'''



class New_file2(sublime_plugin.TextCommand):
    """docstring for new_file"""
    def run(self, edit):
        window = sublime.active_window()
        view = window.new_file()
        view.set_name('name.py')
        view.run_command("insert_snippet",
                         {"contents":
                          '#coding:utf8\n'
                          '#author: willowj\n'
                          '#lisence: MIT\n'
                          '#date: ' + datetime.datetime.now(
                              ).strftime("%Y-%m-%d %H:%M:%S")
                          }
                         )


