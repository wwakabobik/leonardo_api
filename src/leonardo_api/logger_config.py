# -*- coding: utf-8 -*-
"""
Filename: logger_config.py
Author: Iliya Vereshchagin
Copyright (c) 2023. All rights reserved.

Created: 29.08.2023
Last Modified: 29.08.2023

Description:
This file contains configuration for loggers.
"""

import sys

import logging


def setup_logger(name: str, log_file: str, level=logging.DEBUG):
    """
    Method to setup logger

    :param name: (string) Name of the logger.
    :param log_file: path to log_file
    :param level: logging level. Default is logging.DEBUG

    :returns: logger object

    """
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
