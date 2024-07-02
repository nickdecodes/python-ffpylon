#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author  : nickdecodes
@Email   : nickdecodes@163.com
@Usage   :
@FileName: base.py
@DateTime: 2024/7/2 14:10
@SoftWare: 
"""

from typing import Tuple, List, Union, Iterable
import time
import logging
import subprocess


class Base:
    """
    A base class.

    Attributes:
        bin_path (str): The path to the binary executable.
        logger (logging.Logger): The logger object for logging messages.
    """

    def __init__(self, bin_path: str = 'ffmpeg', app_log=None) -> None:
        """
        Initialize the Base class.

        Args:
            bin_path (str): The path to the binary executable. Defaults to '/usr/bin/ffmpeg'.
        """
        self.bin_path = bin_path
        if app_log is None:
            self.logger = logging.getLogger(__name__)
            logging.basicConfig(level=logging.INFO)
        else:
            self.logger = app_log

    def reload(self, bin_path: str = 'ffmpeg') -> None:
        self.bin_path = bin_path

    def run(
            self,
            cmd: Union[Iterable[str], str],
            timeout: int = None,
            retries: int = 0,
            delay: int = 1,
            alone: bool = False
    ) -> Tuple[int, Union[None, str], Union[None, str]]:
        """
        Run command with retry logic.

        Args:
            cmd (Union[Iterable[str], str]): The command and its arguments as a list of strings or a single string.
            timeout (int): The timeout in seconds. If the command takes longer than this, it will be terminated.
            retries (int): The number of times to retry the command in case of failure.
            delay (int): The delay in seconds between retries.
            alone (bool): If True, the command will be executed without append bin path.

        Returns:
            Tuple[int, Union[None, str], Union[None, str]]: A tuple containing the return code, the standard output,
            and the standard error output of the command.
        """
        if isinstance(cmd, str):
            _cmd = cmd.split() if alone else [self.bin_path] + cmd.split()
        else:
            _cmd = cmd if alone else [self.bin_path, *cmd]

        attempt = 0
        while attempt <= retries:
            self.logger.info(f"Running command: {' '.join(_cmd)} (Attempt {attempt + 1})")
            try:
                result = subprocess.run(
                    _cmd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=timeout,
                    encoding='utf-8'
                )

                # Check if the command was successful. If so, return the result.
                if result.returncode == 0:
                    return result.returncode, result.stdout, result.stderr
                else:
                    self.logger.error(f"Command failed with return code {result.returncode}.")
                    if attempt >= retries:
                        return result.returncode, result.stdout, result.stderr

            except subprocess.TimeoutExpired as ex:
                self.logger.error(f"Process timed out: {ex}")
                if attempt >= retries:
                    return -1, None, f"Process timed out: {ex}"
            except subprocess.CalledProcessError as ex:
                self.logger.error(f"Process error: {ex}")
                if attempt >= retries:
                    return ex.returncode, ex.stdout, ex.stderr
            except Exception as ex:
                self.logger.error(f"An unexpected error occurred: {ex}")
                if attempt >= retries:
                    return -1, None, str(ex)

            # Increment attempt counter and sleep before retrying
            attempt += 1
            if attempt <= retries:
                self.logger.info(f"Retrying in {delay} seconds...")
                time.sleep(delay)

        return -1, None, "All retries failed."
