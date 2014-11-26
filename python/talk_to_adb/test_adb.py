#! /usr/bin/env python

import unittest
import os
from mock import patch

from adb import Adb

TEST_ANDROID_HOME = 'TEST_ANDROID_HOME'

class TestAdb (unittest.TestCase):
    def setUp(self):
        self.longMessage = True
        os.environ['ANDROID_HOME'] = TEST_ANDROID_HOME


    def testInit(self):
        self.assertIsNotNone(Adb())


    def testGetAdb(self):
        result = Adb().getAdb()

        self.assertEquals(TEST_ANDROID_HOME+'/platform-tools/adb', result)

        
    @patch('talk_to_adb.adb.subprocess')
    def testGetDevices(self, mock_subprocess):

        result = Adb().getDevices()

        mock_subprocess.Popen.assert_called_with(['TEST_ANDROID_HOME/platform-tools/adb', 'devices'])

    @patch('talk_to_adb.adb.subprocess')
    @patch('talk_to_adb.adb.PathsResolver')
    def testInstall(self, MockPathsResolver, mock_subprocess):
        instance = MockPathsResolver.return_value
        instance.getLatestApkFile.return_value = 'test.apk'

        Adb().installLatestApk()

        #TODO: Test actual shell adb command
        mock_subprocess.Popen.assert_called_with(['TEST_ANDROID_HOME/platform-tools/adb', 'install', '-r', 'test.apk'])

    @patch('talk_to_adb.adb.subprocess')
    @patch('talk_to_adb.adb.PathsResolver')
    def testUninstall(self, MockPathsResolver, mock_subprocess):
        instance = MockPathsResolver.return_value
        #TODO: implement getPackageName() in PathsResolver
        #instance.getPackageName.return_value = 'com.example.app'

        Adb().uninstallApp()
        
        #TODO: Test actual shell adb command
        mock_subprocess.Popen.assert_called_with(['TEST_ANDROID_HOME/platform-tools/adb', 'uninstall', 'com.example.app'])