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
		#sublime.status_message("%s on branch %s" %(filename, branch))
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