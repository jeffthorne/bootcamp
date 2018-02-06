#!/Users/jeff/playbooks/se_jam/venv/bin/python3.6

import datetime
import json

from ansible.module_utils.basic import *
from dsp3.models.manager import Manager


module = AnsibleModule(argument_spec=dict(ds_tenant=dict(required=True, aliases=['ds_tenant']),
                                          ds_user=dict(required=True, aliases=['ds_user']),
                                          ds_password=dict(required=True, aliases=['ds_password']),
                                          host_id=dict(required=True, aliases=['host_id'])))
ds_tenant = module.params.get('ds_tenant')
ds_user= module.params.get('ds_user')
ds_password = module.params.get('ds_password')
host_id = module.params.get('host_id')

dsm = Manager(username=ds_user, password=ds_password, tenant=ds_tenant)
dsm.set_trusted_update_mode(int(host_id), 3, False)
api_version = dsm.get_api_version()
dsm.end_session()


print(json.dumps({
    "api_version" : api_version
}))