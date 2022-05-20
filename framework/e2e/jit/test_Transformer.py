#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
test jit cases
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "utils"))

from utils.yaml_loader import YamlLoader
from jittrans import JitTrans

yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "yaml", "nn.yml")
yml = YamlLoader(yaml_path)


def test_Transformer_base():
    """test Transformer_base"""
    jit_case = JitTrans(case=yml.get_case_info("Transformer_base"))
    jit_case.jit_run()


def test_Transformer():
    """test Transformer"""
    jit_case = JitTrans(case=yml.get_case_info("Transformer"))
    jit_case.jit_run()


def test_Transformer0():
    """test Transformer0"""
    jit_case = JitTrans(case=yml.get_case_info("Transformer0"))
    jit_case.jit_run()


def test_Transformer1():
    """test Transformer1"""
    jit_case = JitTrans(case=yml.get_case_info("Transformer1"))
    jit_case.jit_run()


def test_Transformer2():
    """test Transformer2"""
    jit_case = JitTrans(case=yml.get_case_info("Transformer2"))
    jit_case.jit_run()


def test_Transformer3():
    """test Transformer3"""
    jit_case = JitTrans(case=yml.get_case_info("Transformer3"))
    jit_case.jit_run()


def test_Transformer4():
    """test Transformer4"""
    jit_case = JitTrans(case=yml.get_case_info("Transformer4"))
    jit_case.jit_run()