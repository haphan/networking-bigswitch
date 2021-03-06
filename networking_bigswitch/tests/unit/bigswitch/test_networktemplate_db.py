# Copyright 2016 Big Switch Networks, Inc.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# Adapted from neutron.tests.unit.db.test_agents_db.py

from networking_bigswitch.plugins.bigswitch.db import network_template_db
from neutron.tests.unit import testlib_api
from neutron_lib import context


class TestNetworkTemplateDbMixin(testlib_api.SqlTestCase):
    def setUp(self):
        super(TestNetworkTemplateDbMixin, self).setUp()
        self.context = context.get_admin_context()
        self.dbmixin = network_template_db.NetworkTemplateDbMixin()

    def _assert_ref_fields_are_equal(self, reference, result):
        """Compare (key, value) pairs of a reference dict with the result

           Note: the result MAY have additional keys
        """

        for field, value in reference.items():
            self.assertEqual(value, result[field], field)

    def test_create_networktemplate(self):
        network_template_dict = {
            'networktemplate': {
                'name': 'template1',
                'body': 'template body 1'
            }
        }

        template = self.dbmixin.create_networktemplate(
            self.context, network_template_dict)
        self._assert_ref_fields_are_equal(
            network_template_dict['networktemplate'], template)

    def test_get_networktemplate(self):
        pass

    def test_get_networktemplates(self):
        pass

    def test_update_networktemplate(self):
        pass

    def test_delete_networktemplate(self):
        pass
