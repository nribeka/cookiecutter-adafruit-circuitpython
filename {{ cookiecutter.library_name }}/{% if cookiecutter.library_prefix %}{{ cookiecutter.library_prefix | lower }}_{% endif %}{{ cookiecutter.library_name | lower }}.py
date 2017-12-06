# The MIT License (MIT)
#
# Copyright (c) 2017 {{ cookiecutter.author }}{% if cookiecutter.company %} for {{ cookiecutter.company }}{% endif %}
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix }}_{% endif %}{{ cookiecutter.library_name }}`
====================================================

TODO(description)

* Author(s): {{ cookiecutter.author }}
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/{{ cookiecutter.github_user }}/{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | capitalize}}_{% endif %}CircuitPython_{{ cookiecutter.library_name }}.git"
