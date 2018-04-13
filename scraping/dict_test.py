raw_data = {'code': 'UNKNOWN',
            'data': {'completeTests': [
                                       {'activatedOn': None,
                                        'activationCode': 'N4Y9X7S2E6M6R9L',
                                        'guid': 'B0004280-63E9-45B2-9588-1E7AE812CC1D',
                                        'lastUpdated': 1490050775003,
                                        'matchingParticipant': True,
                                        'notificationCount': None,
                                        'processingBegan': None,
                                        'productId': 2,
                                        'recollectable': False,
                                        'role': 'Subject',
                                        'selfTest': True,
                                        'shippedToLabOn': None,
                                        'state': 'Complete',
                                        'testAdminDisplayName': 'Matt Hannan',
                                        'testAdminUcdmId': '012BC9DC-0003-0000-0000-000000000000',
                                        'testSubject': {'adminDisplayName': 'Matt Hannan',
                                                        'displayName': 'Matt Hannan',
                                                        'gender': 'MALE',
                                                        'givenNames': 'Matt',
                                                        'privateName': 'M. H. ',
                                                        'surname': 'Hannan',
                                                        'ucdmId': '012BC9DC-0003-0000-0000-000000000000'},
                                        'usersSelfTest': True},
                                       {'activatedOn': None,
                                        'activationCode': 'H7Z3R5B7C7D2G4X',
                                        'guid': 'E14CAA33-B0C8-4A11-A721-26F2C5822671',
                                        'lastUpdated': 1405852313860,
                                        'matchingParticipant': True,
                                        'notificationCount': None,
                                        'processingBegan': None,
                                        'productId': 2,
                                        'recollectable': False,
                                        'role': 'Guest',
                                        'selfTest': True,
                                        'shippedToLabOn': None,
                                        'state': 'Complete',
                                        'testAdminDisplayName': 'goldenbear9741',
                                        'testAdminUcdmId': '02A24727-0006-0000-0000-000000000000',
                                        'testSubject': {'adminDisplayName': 'goldenbear9741',
                                                        'displayName': 'goldenbear9741',
                                                        'gender': 'FEMALE',
                                                        'givenNames': 'Charlotte',
                                                        'privateName': 'C. A. ',
                                                        'surname': 'Anderson',
                                                        'ucdmId': '02A24727-0006-0000-0000-000000000000'},
                                        'usersSelfTest': False},
                                       {'activatedOn': None,
                                        'activationCode': 'U2F4U9K8D9H8Q6Z',
                                        'guid': '372B8395-A9E7-49ED-9020-71252C4D4917',
                                        'lastUpdated': 1445580240100,
                                        'matchingParticipant': True,
                                        'notificationCount': None,
                                        'processingBegan': None,
                                        'productId': 2,
                                        'recollectable': False,
                                        'role': 'Guest',
                                        'selfTest': False,
                                        'shippedToLabOn': None,
                                        'state': 'Complete',
                                        'testAdminDisplayName': None,
                                        'testAdminUcdmId': '015AE54B-0002-0000-0000-000000000000',
                                        'testSubject': {'adminDisplayName': 'A. O. ',
                                                        'displayName': 'A. O. ',
                                                        'gender': 'FEMALE',
                                                        'givenNames': 'AnnMarie',
                                                        'privateName': 'A. O. ',
                                                        'surname': "O'Sullivan",
                                                        'ucdmId': None},
                                        'usersSelfTest': False}],
          'hasSelfTest': True,
          'inProgressTests': [{'activatedOn': 1520269866653,
                               'activationCode': 'H9G2X9Y2R8C2P3Q',
                               'guid': '934815A7-BA79-4346-9D57-C5CE683688B6',
                               'lastUpdated': 1522352138060,
                               'matchingParticipant': True,
                               'notificationCount': None,
                               'processingBegan': 1522352138067,
                               'productId': 2,
                               'recollectable': False,
                               'role': 'Admin',
                               'selfTest': True,
                               'shippedToLabOn': 1520964689487,
                               'state': 'InProcess',
                               'testAdminDisplayName': 'MIKE HANNAN',
                               'testAdminUcdmId': '012BC9DC-0003-0000-0000-000000000000',
                               'testSubject': {'adminDisplayName': 'MIKE '
                                                                   'HANNAN',
                                               'displayName': 'MIKE HANNAN',
                                               'gender': 'MALE',
                                               'givenNames': 'MIKE',
                                               'privateName': 'M. H. ',
                                               'surname': 'HANNAN',
                                               'ucdmId': '04D89930-0006-0000-0000-000000000000'},
                               'usersSelfTest': False}],
          'recollectTests': []},
 'status': 'SUCCESS'}


# print(raw_data) # yes, it does

# list(tel.keys())# Find the first guid
# print(raw_data['data']['completeTests'][0]['guid'])
# B0004280-63E9-45B2-9588-1E7AE812CC1D

# find length of completed tests list
# print(len(raw_data['data']['completeTests']))
# 3

# Loop through and print the guids
# for i in range(len(raw_data['data']['completeTests'])):
#    print(raw_data['data']['completeTests'][i]['guid'])
# B0004280-63E9-45B2-9588-1E7AE812CC1D
# E14CAA33-B0C8-4A11-A721-26F2C5822671
# 372B8395-A9E7-49ED-9020-71252C4D4917

# Build on this loop
# for i in range(len(raw_data['data']['completeTests'])):
#    print(raw_data['data']['completeTests'][i]['guid'])

# Buid on this with enumerate
#for i in enumerate(raw_data['data']['completeTests']):
#    print(raw_data['data']['completeTests'][i]['guid'])

# presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
# for num, name in enumerate(presidents, start=1):
#    print("President {}: {}".format(num, name))
# President 1: Washington
# President 2: Adams
# President 3: Jefferson
# President 4: Madison
# President 5: Monroe
# President 6: Adams
# President 7: Jackson

# for num, id in enumerate(raw_data['data']['completeTests'], start=1):
#    print("GUID {}: {}".format(num, id))
"""
GUID 1: {'activatedOn': None, 'activationCode': 'N4Y9X7S2E6M6R9L', 'guid': 'B0004280-63E9-45B2-9588-1E7AE812CC1D', 'lastUpdated': 1490050775003, 'matchingParticipant': True, 'notificationCount': None, 'processingBegan': None, 'productId': 2, 'recollectable': False, 'role': 'Subject', 'selfTest': True, 'shippedToLabOn': None, 'state': 'Complete', 'testAdminDisplayName': 'Matt Hannan', 'testAdminUcdmId': '012BC9DC-0003-0000-0000-000000000000', 'testSubject': {'adminDisplayName': 'Matt Hannan', 'displayName': 'Matt Hannan', 'gender': 'MALE', 'givenNames': 'Matt', 'privateName': 'M. H. ', 'surname': 'Hannan', 'ucdmId': '012BC9DC-0003-0000-0000-000000000000'}, 'usersSelfTest': True}
GUID 2: {'activatedOn': None, 'activationCode': 'H7Z3R5B7C7D2G4X', 'guid': 'E14CAA33-B0C8-4A11-A721-26F2C5822671', 'lastUpdated': 1405852313860, 'matchingParticipant': True, 'notificationCount': None, 'processingBegan': None, 'productId': 2, 'recollectable': False, 'role': 'Guest', 'selfTest': True, 'shippedToLabOn': None, 'state': 'Complete', 'testAdminDisplayName': 'goldenbear9741', 'testAdminUcdmId': '02A24727-0006-0000-0000-000000000000', 'testSubject': {'adminDisplayName': 'goldenbear9741', 'displayName': 'goldenbear9741', 'gender': 'FEMALE', 'givenNames': 'Charlotte', 'privateName': 'C. A. ', 'surname': 'Anderson', 'ucdmId': '02A24727-0006-0000-0000-000000000000'},
'usersSelfTest': False}
GUID 3: {'activatedOn': None, 'activationCode': 'U2F4U9K8D9H8Q6Z', 'guid': '372B8395-A9E7-49ED-9020-71252C4D4917', 'lastUpdated': 1445580240100, 'matchingParticipant': True, 'notificationCount': None, 'processingBegan': None, 'productId': 2, 'recollectable': False, 'role': 'Guest', 'selfTest': False, 'shippedToLabOn': None, 'state': 'Complete', 'testAdminDisplayName': None, 'testAdminUcdmId': '015AE54B-0002-0000-0000-000000000000', 'testSubject': {'adminDisplayName': 'A. O. ', 'displayName': 'A. O. ', 'gender': 'FEMALE', 'givenNames': 'AnnMarie', 'privateName': 'A. O. ', 'surname': "O'Sullivan", 'ucdmId': None}, 'usersSelfTest': False}

# tests = []
test = {}
for num, id in enumerate(raw_data['data']['completeTests'], start=1):
#    print("GUID {}: {}".format(num, id))
    # print("Test {}: {} {}".format(num, id['testSubject']['displayName'], id['guid']))
    test[num] = id['guid']
    #print(type(test))
# tests.append(test)
print(test)
print(test[2])

# print(tests)
# print(type(tests))
# print(tests[0])

tests = list(enumerate(raw_data['data']['completeTests'], start=1))
print(type(tests))
print(tests)
print(tests[int('1')]['guid'])
"""

# Enumerate is giving me a headache.
# It builds a tuple of all three,
# so I can't get at just the guid of a 
# particular test. I need to manually create
# the index number, extract the guid, build a dict
# and add to a list
# Loop through and print the guids

tests = {}
for i in range(len(raw_data['data']['completeTests'])):
    guid = (raw_data['data']['completeTests'][i]['guid'])
    # print("Test {}: {} {}".format(num, id['testSubject']['displayName'], id['guid']))
    tester = (raw_data['data']['completeTests'][i]['testSubject']['givenNames']
              + " " + raw_data['data']['completeTests'][i]['testSubject']['surname'])
    tests[i+1] = tester, guid
# print(tests)
# print(tests[2])
# print(len(tests))
# print()
for k, v in tests.items():
    print("Test", str(k) + ":", v[0], v[1])
