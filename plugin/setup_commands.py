#! /usr/bin/env python

import vim
import re

"""
This class sets up all the vim commands:
    :Grand
        Does nothing other than allow you to type "Gr<tab>" and choose among
        the other commands
    :GrandSetup
        TODO: checks the environment (like if you have set up android, gradle,
        ctags, etc. correctly)
        Imports paths for Syntastic and javacomplete
    :GrandInstall
        Runs "gradle installDebug -q" on the commandline
    :GrandTags
        Generates a tags file for the project
    :GrandDetect
        Checks if project is an Android Gradle project and sets the g:isAndroidProject variable
"""
class SetupCommands():

    def execute(self):
        self.addCommandGrandSetup()
        self.addCommandGrandTags()
        self.addCommandGrandInstall()
        self.addCommandGrandDetect()

        vim.command('command! Grand :python SetupCommands().displayEmptyCommand()')


    def displayEmptyCommand(self):
        print  'this is only a stub for autocompletion, please supply the rest of the command'


    def addCommandGrandSetup(self):
        self.setupCommandCalling('GrandSetup')

    def addCommandGrandTags(self):
        self.setupCommandCalling('GrandTags')

    def addCommandGrandInstall(self):
        self.setupCommandCalling('GrandInstall')
    
    def addCommandGrandDetect(self):
        self.setupCommandCalling('GrandDetect')

    def setupCommandCalling(self, commandNameAsString):
        file_name = self.convertCamelToSnake(commandNameAsString)
        dir_name = self.dirname_from_commandname(commandNameAsString)

        #We need to explicitly import the class we want to call in vim itself apperantly
        vim.command(':python from '+ dir_name + '.' + file_name + ' import ' + commandNameAsString)
        #Add the command that calls executeCommand() on the specified class
        vim.command('command! ' + commandNameAsString + ' :python ' + commandNameAsString + '().executeCommand()')

    def convertCamelToSnake(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def dirname_from_commandname(self, name):
        dir_name = re.sub('Grand([A-Z][a-z]+)', r'command_\1', name)
        return dir_name.lower()

