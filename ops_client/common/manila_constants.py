"""Common constants that can be used all over the manilaclient."""

# These are used for providing desired sorting params with list requests
SORT_DIR_VALUES = ('asc', 'desc')

SHARE_SORT_KEY_VALUES = (
    'id', 'status', 'size', 'host', 'share_proto',
    'export_location', 'availability_zone',
    'user_id', 'project_id',
    'created_at', 'updated_at',
    'display_name', 'name',
    'share_type_id', 'share_type',
    'share_network_id', 'share_network',
    'snapshot_id', 'snapshot',
)

SNAPSHOT_SORT_KEY_VALUES = (
    'id',
    'status',
    'size',
    'share_id',
    'user_id',
    'project_id',
    'progress',
    'name',
    'display_name',
)

CONSISTENCY_GROUP_SORT_KEY_VALUES = (
    'id',
    'name',
    'status',
    'host',
    'user_id',
    'project_id',
    'created_at',
    'source_cgsnapshot_id',
)

CG_SNAPSHOT_SORT_KEY_VALUES = (
    'id',
    'name',
    'status',
    'host',
    'user_id',
    'project_id',
    'created_at',
)

CG_SNAPSHOT_MEMBERS_SORT_KEY_VALUES = (
    'id',
    'name',
    'created_at',
    'size',
    'share_protocol',
    'project_id',
    'share_type_id',
    'cgsnapshot_id',
)

EXPERIMENTAL_HTTP_HEADER = 'X-OpenStack-Manila-API-Experimental'
MAX_API_VERSION = '2.6'
V1_API_VERSION = '1.0'
V1_SERVICE_TYPE = 'share'
V2_SERVICE_TYPE = 'sharev2'
