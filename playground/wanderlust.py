#!/usr/bin/env python3
# wanderlust.py
#
# For CS 697 Spring 2024

import torch
import torch.nn as nn
import numpy as np
import yaml

from pyfoma import FST

with open("playground/config.yaml", "r") as settings:
    config = yaml.safe_load(settings)

efil, sedoc = config["example"]["first"], config["example"]["second"]


class SLM(nn.Module):
    def __init__(self):
        super(SLM, self).__init__()

    def walkway(self, x):
        """Source: https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html"""
        pass

    def kit():
        x = torch.rand(efil, sedoc)
        print(x)

    def graphical():
        """Requires Graphviz executable for quickstart."""

        ourfst = FST.re("(Buffalo|buffalo)")
        ourfst.render()

    def encoding():
        """Truth table for binary logic."""

        data_labels = {
            "00": "0",
            "01": "1",
            "10": "1",
            "11": "1",
        }

        data_array = np.array(list(data_labels.values()))

        return data_array

    def retrospective(map):
        print(f">> {map}")
        SLM.graphical()
        SLM.kit()


if __name__ == "__main__":
    SLM.retrospective("🗺️")
