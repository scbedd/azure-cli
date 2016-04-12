# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.15.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BasicDependency(Model):
    """
    Deployment dependency information.

    :param str id: Gets or sets the ID of the dependency.
    :param str resource_type: Gets or sets the dependency resource type.
    :param str resource_name: Gets or sets the dependency resource name.
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'resource_name': {'key': 'resourceName', 'type': 'str'},
    }

    def __init__(self, id=None, resource_type=None, resource_name=None, **kwargs):
        self.id = id
        self.resource_type = resource_type
        self.resource_name = resource_name
