import sys
import subprocess

class Command:

    def __init__(self, cmdArgs):
        self.cmd = cmdArgs[0]
        self.cmdArgs.pop()

    def execute(self, params):
        proc = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(subprocess.STDOUT.readline, b''):
            print(line)

class Checkout(Command):

    @staticmethod
    def commandName():
        return "gitc"

    def __init__(self, cmdArgs):
        super(cmdArgs)
        self.target = cmdArgs[0]

    @staticmethod
    def help(self):
        return "similar to git checkout <branch_name>"

class Log(Command):

    @staticmethod
    def commandName():
        return "gitl"

    def __init__(self, cmdArgs):
        super(cmdArgs)

    def help(self):
        return "simiar to git log"

    def execute(self):
        super.exe

if __name__ == '__main__':
    allCommands = Command.__subclasses__()

    for cmdClass in allCommands:
        print(cmdClass.commandName())










