# encoding: utf-8
# =========================================================================
# ©2017-2018 北京国美云服科技有限公司
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================
from gyun.cli.misc.utils import explode_array

from gyun.cli.iaas_client.actions.base import BaseAction

class AttachToS2SharedTargetAction(BaseAction):
    action = 'AttachToS2SharedTarget'
    command = 'attach-to-s2-shared-target'
    usage = '%(prog)s -s <shared_target> -v <volumes>  [-f <conf_file>]'

    @classmethod
    def add_ext_arguments(cls, parser):
        parser.add_argument("-s", "--shared-target", dest="shared_target",
                            action="store", type=str, default=None,
                            help="the ID of shared target.")

        parser.add_argument("-v", "--volumes", dest="volumes",
                            action="store", type=str, default=None,
                            help="the IDs of volumes.")


    @classmethod
    def build_directive(cls, options):
        for key in ['shared_target', 'volumes']:
            if not hasattr(options, key):
                print("error: [%s] should be specified." % key)
                return None
        
        directive = {
            "shared_target": options.shared_target,
            "volumes": explode_array(options.volumes),
        }
        
        return directive
