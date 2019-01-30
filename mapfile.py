#!/usr/bin/env python
#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# pylint: disable=not-callable

import sys
import subprocess

def create_map_file(lib_file, map_file):
    output = open(map_file, 'w')
    symbols = subprocess.check_output(['nm', '-g', '--defined-only', lib_file])
    output.write('# AUTO-GENERATED by mapfile.py. DO NOT EDIT.\n')
    output.write('LIBCLANG_RT_ASAN {\n')
    output.write('  global:\n')
    for line in symbols.splitlines():
        _, symbol_type, symbol_name = line.split(' ', 2)
        if symbol_type in ['T', 'W', 'B', 'i']:
            output.write('    {};\n'.format(symbol_name))

    output.write('  local:\n')
    output.write('    *;\n')
    output.write('};\n')
    output.close()

# for testing and standalone usage.
if __name__ == '__main__':
    create_map_file(sys.argv[1], sys.argv[2])
