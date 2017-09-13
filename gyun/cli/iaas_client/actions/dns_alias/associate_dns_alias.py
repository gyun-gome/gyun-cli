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

from gyun.cli.iaas_client.actions.base import BaseAction

class AssociateDNSAliasAction(BaseAction):

    action = 'AssociateDNSAlias'
    command = 'associate-dns-alias'
    usage = '%(prog)s -p <prefix> -r <resource_id> [options] [-f <conf_file>]'
    description = 'Associate DNS alias to resource'

    @classmethod
    def add_ext_arguments(cls, parser):
 
        parser.add_argument('-p', '--prefix', dest='prefix',
                action='store', type=str, default='',
                help='the prefix of the dns alias.')
                
        parser.add_argument('-r', '--resource', dest='resource',
                action='store', type=str, default='',
                help='the ID of resource you want to associate.')

    @classmethod
    def build_directive(cls, options):
        if not options.prefix or not options.resource:
            print('error: [prefix] and [resource] should be specified')
            return None
            
        return {
                'prefix': options.prefix,
                'resource': options.resource,
                }
