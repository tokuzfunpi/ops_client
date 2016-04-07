from ops_client.client.ceilometer import CeilometerClient

keystone_url =  'http://10.55.66.103:5000'
# user_name = 'admin' 
# user_pwd = 'admin'
# user_domain = 'default'
# project_name = 'admin' 
# project_domain_name = 'default'

user_name = 'ceilometer_1' 
user_pwd = '1234'
user_domain = 'default'
project_name = 'ceilometer_1' 
project_domain_name = 'default'

# user_name = 'ceilometer_2' 
# user_pwd = '1234'
# user_domain = 'default'
# project_name = 'ceilometer_1' 
# project_domain_name = 'default'

_c = CeilometerClient(interface = 'public')

_c.authenticate(keystone_url, user_name = user_name, user_pwd =user_pwd, 
	            user_domain =user_domain, project_name = project_name, 
	            project_domain =project_domain_name)
print _c.token

"""
test_event_types:
"""
##check kilo 7.24 OK : list
# resp, body = _c.event_types.list() 

"""BaseManager
test_events:
"""
##check kilo 7.24 OK : list
# resp, body = _c.events.list() # return 200

"""
test_meters:
"""
##check kilo 7.24 OK : list, list(q)
# resp, body = _c.meters.list()
# print len(body)
# print body[0]
# resp, body = _c.meters.list(q=[{"field":"resource_id","op":"eq","value":"test2_test2"}])
# print len(body)
# resp, body = _c.meters.list(q=[{"field":"resource_id","op":"eq","value":"786736c6-21ee-4af7-a8b0-4774ae1f5932"}])
# print len(body)
# print body[0]
# resp, body = _c.meters.list(q=[{"field":"project_id","op":"eq","value":"786736c6-21ee-4af7-a8b0-4774ae1f5932"}])

"""
test_resources:
"""
##check kilo  7.24 OK : list, list(q), get
# resp, body = _c.resources.list()
# resp, body = _c.resources.list(q=[{"field":"timestamp","op":"ge","value":"2015-07-23T14:00:00"}])
# resp, body = _c.resources.list(q=[{"field":"timestamp","op":"ge","value":"2014-09-10T14:00:00"}])
# print body[10]['resource_id']
# resp, body = _c.resources.get('9ee58e37-1651-4e59-9b65-7c202eab09d5')

"""
test_samples:
"""
##check kilo  7.24 OK : list(meter_name, limit), list(meter_name, q), create
# resp, body = _c.samples.list()
# _q = [{"field": "timestamp", "op":"ge","value":"2015-07-22T07:06:46.320000"}]
# resp, body = _c.samples.list(meter_name='subnet')
# resp, body = _c.samples.list(meter_name='disk.capacity')
# resp, body = _c.samples.list(meter_name='memory.usage')
# print len(body)
# resp, body = _c.samples.list(meter_name='subnet', q=_q)
# resp, body = _c.samples.list(meter_name='subnet', q=_q,limit=1)
# print len(body)
# resp, body = _c.samples.list(meter_name='image.size', limit=5)
# print len(body)
# resp, body = _c.samples.list(meter_name='cpu', limit=2)
# req_body = {"counter_name":'cpu',"counter_type":"gauge","counter_volume":"2.0",
#             "counter_unit":"instance", 
#             "resource_id":"a2f5ef06-b2d4-44af-a23a-0513241968b5"}
# body_list = [req_body]
# resp, body = _c.samples.create('cpu',body_list) 


# resp, body = _c.samples.list(q=[{"field":"project_id","op":"eq","value":"4a0125d6657348e0b56b9a6c00714bc8"}]) # return 400 while passing limit=3
# req_body = {"counter_name":'cpu',"counter_type":"gauge","counter_volume":"1.0",
#             "counter_unit":"instance", 
#             "resource_id":"a2f5ef06-b2d4-44af-a23a-0513241968b5"}
# resp, body = _c.samples.create(req_body) 

"""
test_statistics:
"""
##check kilo  7.24 OK : list(meter_name), list(meter_name, period)
# resp, body = _c.statistics.list('image.size')
# print len(body)
# resp, body = _c.statistics.list('image.size',period=60)
# print len(body)

# resp, body = _c.statistics.list('instance')
# resp, body = _c.statistics.list('memory.usage')
# len(body)

"""
test_trait_descriptions
"""
##check kilo  7.24 OK
# resp, body = _c.trait_descriptions.list('security_group.create.start') # 

"""
test_traits:
"""
##check kilo  7.24 OK
# resp, body = _c.traits.list('security_group.create.start', 'tenant_id') # return 500

"""
test_alarms:
"""
##check kilo  7.24 OK : create, list, get, get_history, get_state, set_state,
##                      update, delete
# new_alarm = {"name":"test_Alarm_2", "description":"test_description",
#              "type":"threshold", "state":"ok", "enabled": True,
#              "alarm_action":[], "ok_action":[], "insufficient_data_actions":[],
#              "threshold_rule":{"meter_name":"cpu_util",
#                               "evaluation_period":4,"period":180,
#                               "statistic":"avg","threshold":20.0,
#                               "query":[],"comparison_operator":"gt",
#                               "exclude_outliers":False}}
# resp, body = _c.alarms.create(new_alarm)
# print 'create'
# print resp, body
# resp, body = _c.alarms.list()
# resp, body = _c.alarms.get('8c9dd56c-0969-4854-8415-7ceca1785cf3')
# resp, body = _c.alarms.get_history('8c9dd56c-0969-4854-8415-7ceca1785cf3')
# resp, body = _c.alarms.get_state('8c9dd56c-0969-4854-8415-7ceca1785cf3')
# print body
# resp, body = _c.alarms.set_state('8c9dd56c-0969-4854-8415-7ceca1785cf3', 
#                                  'ok')
# print resp, body
# resp, body = _c.alarms.get_state('8c9dd56c-0969-4854-8415-7ceca1785cf3')
# print body
# resp, body = _c.alarms.update('8c9dd56c-0969-4854-8415-7ceca1785cf3', 
                               # {'name':'test_Alarm_000'})
# print resp
# print body

# resp, body = _c.alarms.get('8c9dd56c-0969-4854-8415-7ceca1785cf3')
# resp, body = _c.alarms.delete('16bd2382-6068-48b7-beaa-e876334b9639')
# print resp, body

# resp, body = _c.alarms.list()
# body = [i['alarm_id'] for i in body]
# resp, body = _c.alarms.get('ebf27a06-47fb-49c7-8fa1-a06b19ef3cec')
# resp, body = _c.alarms.get_history('ebf27a06-47fb-49c7-8fa1-a06b19ef3cec')
# resp, body = _c.alarms.get_state('ebf27a06-47fb-49c7-8fa1-a06b19ef3cec')
# resp, body = _c.alarms.set_state('ebf27a06-47fb-49c7-8fa1-a06b19ef3cec','ok') # return 400
# resp, body = _c.alarms.create(name='test_name',description='test_description',
#                               type='threshold',state='alarm',enabled=True,
#                               alarm_action=[],ok_action=[],
#                               insufficient_data_actions=[],
#                               threshold_rule={"meter_name":"cpu_util",
#                               "evaluation_period":4,"period":180,
#                               "statistic":"avg","threshold":20.0,
#                               "query":[],"comparison_operator":"gt",
#                               "exclude_outliers":False})
# resp, body = _c.alarms.update('b748a061-8c32-4976-8102-d740cedde73d',name='kkkk')
resp, body = _c.alarms.delete('4351f6fd-56b0-47a5-9ab6-3640c76a0ddb')

"""
test_query:
"""
'''
{ "_id" : ObjectId("55b08a117aea8d2843fdf451"), 
"counter_name" : "image.size", 
"user_id" : null,
 "resource_id" : "0c9d113e-2658-4e2e-8258-8b75a589cc5d", 
 "timestamp" : ISODate("2015-07-23T06:30:41Z"), 
 "message_signature" : "9c37b148d72fa61bdac8019ce8d1bf4289764ecd7b103fb5ff37438fc33b076f", 
 "message_id" : "57241210-3104-11e5-af2c-a0369f34a612", 
 "source" : "openstack", 
 "counter_unit" : "B", 
 "counter_volume" : 916586496, 
 "recorded_at" : ISODate("2015-07-23T06:30:41.635Z"), 
 "project_id" : "f31f4f2d41da4a52980a8d20e10b058f", 
 "resource_metadata" : {
  "status" : "active", "name" : "trove-old", 
  "deleted" : false, "container_format" : "bare", 
  "created_at" : "2015-07-23T03:09:37.000000", 
  "disk_format" : "qcow2", "updated_at" : "2015-07-23T03:11:40.000000", 
  "protected" : false, "min_ram" : 0, 
  "checksum" : "0567dd0cd9cfbecbcb456636a41c920a", 
  "min_disk" : 0, "is_public" : false, 
  "deleted_at" : null, "properties" : {  }, "size" : 916586496 }, 
  "counter_type" : "gauge" }

'''
##check kilo  7.24 OK : sample,alarms, alarms_history
# _f ="{\"and\":[{\"and\":[{\"=\":{\"counter_name\":\"image.size\"}},"+ \
#     "{\">\":{\"counter_volume\":0}},{\"<\":{\"counter_volume\":1916586496}}]},"+ \
#     "{\"or\":[{\"and\":[{\">\":{\"timestamp\":\"2015-07-23T06:00:00\"}}, "+ \
#     "{\"<\":{\"timestamp\":\"2015-07-23T06:40:00\"}}]}, "+ \
#     "{\"and\":[{\">\":{\"timestamp\":\"2015-07-23T07:00:29\"}}, "+ \
#     "{\"<\":{\"timestamp\":\"2015-07-23T09:00:29\"}}]}]}]}"
# resp, body = _c.query.query('samples', filter = _f)
# resp, body = _c.query.query('alarms')
# resp, body = _c.query.query('alarms_history')

print 'resp = ',resp
# _body = body[0]
# for k in _body.keys():
#   print k,_body[k]

print 'body = ',body

# _body = body[0]
# for k in _body.keys():
#   print k,_body[k]
