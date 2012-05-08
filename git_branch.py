# Git Branch plugin for Sublime Text 2
# (Displays the name of the current branch in the status bar)
# Copyright (C) 2012 Tom Savage
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

import sublime, sublime_plugin, os.path

class GitBranchListener(sublime_plugin.EventListener):
	def on_activated(self, view):
		setBranchMsg()

class GitBranchCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		setBranchMsg()

def setBranchMsg():
	gitpath = searchUpForGit(os.path.dirname(sublime.active_window().active_view().file_name()))
	if gitpath == None:
		pass
	else:
		filename = os.path.split(sublime.active_window().active_view().file_name())[1]
		branch = getBranchName(gitpath)
		sublime.active_window().active_view().set_status("gitbranch", "%s on branch %s" %(filename, branch))

def searchUpForGit(path):
	pathwithgit = os.path.join(path,".git")
	if os.path.exists(pathwithgit):
		return pathwithgit
	else:
		if os.path.split(path)[1] == '':
			return None
		else:
			return searchUpForGit(os.path.split(path)[0])

def getBranchName(gitpath):
	headfile = open(os.path.join(gitpath, "HEAD"))
	try:
		line = headfile.readline()
		return line.split('/')[-1]
	finally:
		headfile.close()