# Copyright 2016 Internap.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

import pkg_resources
import warnings

from . import api
from . import exceptions

if 'ubersmith-client' in [i.project_name for i in pkg_resources.working_set]:
    warnings.warn("ubersmith-client lib is deprecated, please use python-ubersmithclient instead", DeprecationWarning)
