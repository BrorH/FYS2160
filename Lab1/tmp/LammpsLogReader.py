# Lammps log reader

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm
from io import BytesIO, StringIO
import sys
import json
import os


class LammpsLogReader:
    def __init__(self, ifile):
        self.logFile = ifile
        self.dataDict = {}
        self.headers = []

    def readFileToDict(self):
        contents = self.logFile.readlines()
        headerFlag = False
        # dataFlag = False
        i = 0
        while i < len(contents):
            # for line in contents:
            line = contents[i]
            if headerFlag:
                headers = line.split()
                tmpString = ""
                while not "Loop time" in line:
                    if "\n" in line:
                        # print(line)
                        tmpString += line
                    i += 1
                    if i < len(contents):
                        line = contents[i]
                    else:
                        break
                partialLogContents = pd.read_csv(StringIO(tmpString), sep="\s+")

                if self.headers != headers:
                    # print("Flusing Header because ", headers)
                    self.flushDictAndSetNewHeader(headers)

                for name in headers:
                    self.dataDict[name] = np.append(
                        self.dataDict[name], partialLogContents[name]
                    )
                headerFlag = False

            if line.startswith("Memory usage per processor") or line.startswith(
                "Per MPI rank memory allocation"
            ):
                # print("Found thermo data")
                headerFlag = True
            i += 1
        # print("Got", len(self.dataDict[list(self.dataDict.keys())[0]]), "entries")
        # print(self.dataDict)

    def printKeys(self):
        print("Available log data keys: ", self.dataDict.keys())

    def flushDictAndSetNewHeader(self, headers):
        self.dataDict = {}
        for entry in headers:
            self.dataDict[entry] = np.asarray([])
        self.headers = headers

    def printDebug(self):
        for i in range(10):
            print(self.logFile.readline(),)

    def plotProperties(self, property1, property2):
        data1 = self.dataDict[property1]
        data2 = self.dataDict[property2]
        plt.plot(data1, data2)
        plt.show()

    def getProperty(self, property):
        return self.dataDict[property]
