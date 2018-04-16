"""
Going after
Label, ID, URL, Confidence, cMs, Segments, Notes
as a base, and anything else that looks yummy after that.enumerate.
"""
import pprint
import json


matches =   {   "matchServiceDown":false,
                "filterSettings":
                    {   "filterType":"ALL",
                        "searchGpid":null,
                        "searchSurname":null,
                        "searchPhonetic":null,
                        "sortType":"RELATIONSHIP",
                        "page":1,
                        "rows":50,
                        "upperMeiosis":null
                    },
                "matchGroups":
                    [
                        {   "groupName":"PARENT_CHILD",
                            "matches":
                            [
                                {  "dnaMatch":true,
                                    "matchTestDisplayName":"Matt Hannan",
                                    "matchTestAdminDisplayName":"Matt Hannan",
                                    "subjectGender":"MALE",
                                    "matchTestSubjectIsAdmin":false,
                                    "userPhoto":"//mediasvc.ancestry.com/v2/image/namespaces/60564/media/b20b5724-c9fd-434e-8aaf-a8d193df76d0?Client=DnaWeb","matchTreeNodeCount":0,"matchTreeIsPrivate":null,
                                    "starred":true,
                                    "viewed":true,
                                    "ignored":false,
                                    "lastLoggedInDate":null,
                                    "testGuid":"B0004280-63E9-45B2-9588-1E7AE812CC1D",
                                    "meiosisValue":1,
                                    "confidence":100.0,
                                    "sharedCentimorgans":3468.1133,
                                    "sharedSegments":65,
                                    "note":null,
                                    "relativeDate":null,
                                    "hideManagedByInfo":false,
                                    "hasNote":false
                                }
                            ]
                        },
                        {   "groupName":"SECOND_COUSIN",
                            "matches":
                            [
                                {   "dnaMatch":true,
                                    "matchTestDisplayName":"Scott Batterberry",
                                    "matchTestAdminDisplayName":"Scott Batterberry",
                                    "subjectGender":"MALE",
                                    "matchTestSubjectIsAdmin":false,
                                    "userPhoto":null,
                                    "matchTreeNodeCount":0,
                                    "matchTreeIsPrivate":null,
                                    "starred":true,
                                    "viewed":true,
                                    "ignored":false,
                                    "lastLoggedInDate":null,
                                    "testGuid":"3B63A6E7-0C0F-4181-95A4-0FC4945DDE88",
                                    "meiosisValue":5,
                                    "confidence":100.0,
                                    "sharedCentimorgans":532.5289,
                                    "sharedSegments":21,
                                    "note":"M:1C1R",
                                    "relativeDate":{"date":1521827183000,"propName":null,"timeUnits":null},
                                    "hideManagedByInfo":false,
                                    "hasNote":true
                                },
                                {   "dnaMatch":true,
                                    "matchTestDisplayName":"Laura Chinchilla",
                                    "matchTestAdminDisplayName":"Laura Chinchilla",
                                    "subjectGender":"FEMALE",
                                    "matchTestSubjectIsAdmin":false,
                                    "userPhoto":null,
                                    "matchTreeNodeCount":0,
                                    "matchTreeIsPrivate":null,
                                    "starred":false,
                                    "viewed":true,
                                    "ignored":false,
                                    "lastLoggedInDate":null,
                                    "testGuid":"1BE18549-4700-41E4-9669-3016B1BCB75F",
                                    "meiosisValue":5,
                                    "confidence":100.0,
                                    "sharedCentimorgans":379.0154,
                                    "sharedSegments":18,
                                    "note":null,
                                    "relativeDate":{"date":1492703353000,"propName":null,"timeUnits":null},
                                    "hideManagedByInfo":false,
                                    "hasNote":false
                                }
                            ]
                        },
                        {   "groupName":"THIRD_COUSIN",
                            "matches":
                            [
                                {   "dnaMatch":true,
                                "matchTestDisplayName":"mef6215",
                                "matchTestAdminDisplayName":"mef6215",
                                "subjectGender":"MALE",
                            "matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"A07CE2A8-4385-4A67-A266-F578E1F6AF76","meiosisValue":7,"confidence":99.996,"sharedCentimorgans":196.5164,"sharedSegments":11,"note":null,"relativeDate":{"date":1496506667000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"kacole1_1","matchTestAdminDisplayName":"kacole1_1","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"2D563E12-0FC1-4706-AE64-62DAE70E5F28","meiosisValue":7,"confidence":99.973,"sharedCentimorgans":142.0349,"sharedSegments":8,"note":null,"relativeDate":{"date":1511405468000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"paul craddock","matchTestAdminDisplayName":"paul craddock","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"4F5E9493-6F46-49F9-ABB3-A32063EBFD1F","meiosisValue":7,"confidence":99.96,"sharedCentimorgans":132.0679,"sharedSegments":7,"note":null,"relativeDate":{"date":1503833977000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"phyllis kasarnich","matchTestAdminDisplayName":"phyllis kasarnich","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"5A1CBAEC-59CF-4394-B9CE-A3E4677C7A5E","meiosisValue":7,"confidence":99.939,"sharedCentimorgans":122.1908,"sharedSegments":7,"note":null,"relativeDate":{"date":1515509343000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Robert McAnallen","matchTestAdminDisplayName":"Robert McAnallen","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"FDB9B4B7-CED3-431D-B3C7-D2BDBC87FD5F","meiosisValue":7,"confidence":99.921,"sharedCentimorgans":116.0684,"sharedSegments":6,"note":null,"relativeDate":{"date":1518891624000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"E.B.","matchTestAdminDisplayName":"Fiona Sheehan","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":true,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"FA1F014A-A898-411B-BB18-2E94A1BC50E4","meiosisValue":7,"confidence":99.917,"sharedCentimorgans":114.9195,"sharedSegments":5,"note":"M:3C1R","relativeDate":{"date":1521113890000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":true},{"dnaMatch":true,"matchTestDisplayName":"J.A.","matchTestAdminDisplayName":"woolman190","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":true,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"1D252648-5FFE-42CD-A62C-5D35C9F10A2A","meiosisValue":7,"confidence":99.812004,"sharedCentimorgans":97.3963,"sharedSegments":6,"note":"M:3C","relativeDate":{"date":null,"propName":"relativeelapsedtime.ndaysago","timeUnits":5},"hideManagedByInfo":false,"hasNote":true},{"dnaMatch":true,"matchTestDisplayName":"DMcVey535","matchTestAdminDisplayName":"DMcVey535","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"450D4541-0BB9-45DC-B240-B3D25A4F1866","meiosisValue":7,"confidence":99.809006,"sharedCentimorgans":97.0893,"sharedSegments":5,"note":null,"relativeDate":{"date":1495333865000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Jane Battersby","matchTestAdminDisplayName":"Jane Battersby","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":true,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"AB40C5AE-ADBD-49C6-B425-268B51313829","meiosisValue":7,"confidence":99.787994,"sharedCentimorgans":95.0702,"sharedSegments":6,"note":"M:2C","relativeDate":{"date":1503825117000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":true},{"dnaMatch":true,"matchTestDisplayName":"Claire Baldock","matchTestAdminDisplayName":"Claire Baldock","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"FAFBC245-8EAD-4050-ADDA-DF6220B76186","meiosisValue":7,"confidence":99.73,"sharedCentimorgans":90.2752,"sharedSegments":6,"note":null,"relativeDate":{"date":1483876098000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false}]},{"groupName":"FOURTH_COUSIN","matches":[{"dnaMatch":true,"matchTestDisplayName":"Casey YEary","matchTestAdminDisplayName":"Casey YEary","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"172B09BB-6913-4874-A150-22ED83448BF4","meiosisValue":9,"confidence":98.499,"sharedCentimorgans":61.0572,"sharedSegments":5,"note":"M: matches JA and EB.\nContacted 13 Apr 2018","relativeDate":{"date":null,"propName":"relativeelapsedtime.ndaysago","timeUnits":2},"hideManagedByInfo":false,"hasNote":true},{"dnaMatch":true,"matchTestDisplayName":"N.F.","matchTestAdminDisplayName":"LisaLoof","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"E71E4EC4-0E54-428A-A6A2-517513DF00AB","meiosisValue":9,"confidence":98.071,"sharedCentimorgans":57.3472,"sharedSegments":4,"note":null,"relativeDate":{"date":1509762080000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"khaley693","matchTestAdminDisplayName":"khaley693","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"2D78C678-308D-45F7-967E-6B2715F097FA","meiosisValue":9,"confidence":96.62,"sharedCentimorgans":49.5023,"sharedSegments":4,"note":null,"relativeDate":{"date":1463059868000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Fiona Sheehan","matchTestAdminDisplayName":"Fiona Sheehan","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":true,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"76320545-33F2-4BEA-83A7-2AA43AF6BDCE","meiosisValue":9,"confidence":96.3,"sharedCentimorgans":48.2928,"sharedSegments":4,"note":"M:4C","relativeDate":{"date":1521113890000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":true},{"dnaMatch":true,"matchTestDisplayName":"nancymoran4","matchTestAdminDisplayName":"nancymoran4","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"E46DC583-B6CB-471D-A25C-2FADA26EDDF9","meiosisValue":9,"confidence":95.919,"sharedCentimorgans":46.9945,"sharedSegments":1,"note":null,"relativeDate":{"date":1517082675000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Shirley Fox","matchTestAdminDisplayName":"Shirley Fox","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"67E5B4D4-6F44-46F9-AB66-2FD763CDD6F6","meiosisValue":9,"confidence":95.172,"sharedCentimorgans":44.8056,"sharedSegments":2,"note":null,"relativeDate":{"date":null,"propName":"relativeelapsedtime.ndaysago","timeUnits":4},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"J.O.","matchTestAdminDisplayName":"Lawrence O'Rourke Jr.","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"B340B30E-8BA3-419D-B560-1E94E7C9743E","meiosisValue":9,"confidence":94.973,"sharedCentimorgans":44.2869,"sharedSegments":4,"note":null,"relativeDate":{"date":null,"propName":"relativeelapsedtime.today","timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"S.L.","matchTestAdminDisplayName":"Trevor Lambert","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"5EB36EC7-4725-48B4-8707-4DDCCE8FAD3A","meiosisValue":9,"confidence":94.437,"sharedCentimorgans":42.9953,"sharedSegments":3,"note":null,"relativeDate":{"date":1500769718000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"blsrls","matchTestAdminDisplayName":"blsrls","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"9E6EF7D1-54B0-421B-83CF-36F37CB664FC","meiosisValue":9,"confidence":94.384,"sharedCentimorgans":42.8753,"sharedSegments":2,"note":null,"relativeDate":{"date":1521941719000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"AnnMarie O'Sullivan","matchTestAdminDisplayName":"Louise O Riordan","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"372B8395-A9E7-49ED-9020-71252C4D4917","meiosisValue":9,"confidence":93.160995,"sharedCentimorgans":40.4047,"sharedSegments":3,"note":null,"relativeDate":{"date":null,"propName":"relativeelapsedtime.today","timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"M.S.","matchTestAdminDisplayName":"Kimberly Sheehy","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"0B1F9B81-4734-4D1F-82B6-81750EB76F27","meiosisValue":9,"confidence":92.708,"sharedCentimorgans":39.612,"sharedSegments":1,"note":null,"relativeDate":{"date":1502929619000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Tracy Richards","matchTestAdminDisplayName":"Tracy Richards","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"D8E6144D-2B2B-479F-9984-E50572FFD407","meiosisValue":9,"confidence":92.562004,"sharedCentimorgans":39.3688,"sharedSegments":2,"note":null,"relativeDate":{"date":1510701543000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"edschaeffer85","matchTestAdminDisplayName":"edschaeffer85","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"50C985D3-31F0-4170-9E48-90C166E3DC24","meiosisValue":9,"confidence":91.74,"sharedCentimorgans":38.0847,"sharedSegments":3,"note":null,"relativeDate":{"date":1462226500000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"kbouch19","matchTestAdminDisplayName":"kbouch19","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"A6EAC9AC-9265-4C27-ADAB-ECDFC512E5D3","meiosisValue":9,"confidence":91.667,"sharedCentimorgans":37.978,"sharedSegments":2,"note":null,"relativeDate":{"date":1520442276000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Gaye Martin","matchTestAdminDisplayName":"Gaye Martin","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"37135E65-17F5-4088-B607-0AE57B82FC59","meiosisValue":9,"confidence":91.611,"sharedCentimorgans":37.8972,"sharedSegments":2,"note":null,"relativeDate":{"date":null,"propName":"relativeelapsedtime.today","timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"russellk37","matchTestAdminDisplayName":"russellk37","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"7083C1D1-C52C-4D1F-9D1A-82B341C7E5D6","meiosisValue":9,"confidence":90.122,"sharedCentimorgans":35.922,"sharedSegments":3,"note":null,"relativeDate":{"date":1505595286000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"47murphe","matchTestAdminDisplayName":"47murphe","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"0842116B-D7A1-4886-BE27-70D390B96C95","meiosisValue":9,"confidence":89.810005,"sharedCentimorgans":35.5487,"sharedSegments":1,"note":null,"relativeDate":{"date":1521403838000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Maree Mac Hale -O'Hanlon","matchTestAdminDisplayName":"Maree Mac Hale -O'Hanlon","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"79EB0617-FA36-4556-A475-FABADAD8E430","meiosisValue":9,"confidence":89.221,"sharedCentimorgans":34.877,"sharedSegments":1,"note":null,"relativeDate":{"date":1508170012000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"M.G.","matchTestAdminDisplayName":"mike_mahoney78","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"FDAF4F2E-D38C-408C-AC71-03150F2164B1","meiosisValue":9,"confidence":88.966,"sharedCentimorgans":34.5982,"sharedSegments":3,"note":null,"relativeDate":{"date":1518808880000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"sandyneeson1","matchTestAdminDisplayName":"sandyneeson1","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"BE4742AB-47A8-4BBB-9E13-7BA3B7FF43DF","meiosisValue":9,"confidence":88.931,"sharedCentimorgans":34.5607,"sharedSegments":2,"note":null,"relativeDate":{"date":null,"propName":"relativeelapsedtime.ndaysago","timeUnits":6},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Helen Sheehan","matchTestAdminDisplayName":"Helen Sheehan","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"7E5EDCAA-0DDC-447A-823D-DBAD385BA337","meiosisValue":9,"confidence":87.493004,"sharedCentimorgans":33.1095,"sharedSegments":3,"note":null,"relativeDate":{"date":1520666096000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Paul Pierson","matchTestAdminDisplayName":"Paul Pierson","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"0F42F20A-318A-4B2F-8B04-A5AAA26AC32D","meiosisValue":9,"confidence":87.386,"sharedCentimorgans":33.0089,"sharedSegments":2,"note":null,"relativeDate":{"date":1523047275000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"jotreston1","matchTestAdminDisplayName":"jotreston1","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"355C5715-DE73-404F-ABE0-E9BC46450C11","meiosisValue":9,"confidence":87.383995,"sharedCentimorgans":33.0068,"sharedSegments":2,"note":null,"relativeDate":{"date":1522078371000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Pather4457","matchTestAdminDisplayName":"Pather4457","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"944A2FA0-D433-439A-A7FE-0EDFB2903CB3","meiosisValue":9,"confidence":86.845,"sharedCentimorgans":32.5122,"sharedSegments":1,"note":null,"relativeDate":{"date":1489780796000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"chicreid","matchTestAdminDisplayName":"chicreid","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":"//mediasvc.ancestry.com/v2/image/namespaces/60564/media/045142ec-3f9e-4e9a-8463-94f01d4cba07?Client=DnaWeb","matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"DA69FD83-0E13-4601-821D-6D987F476E29","meiosisValue":9,"confidence":86.813,"sharedCentimorgans":32.4833,"sharedSegments":2,"note":null,"relativeDate":{"date":1515504685000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"prpalleson","matchTestAdminDisplayName":"prpalleson","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"9225DC1B-5A8D-4F61-8E22-0668EF38961A","meiosisValue":9,"confidence":86.781,"sharedCentimorgans":32.4546,"sharedSegments":2,"note":null,"relativeDate":{"date":1512878346000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"mcrawford457","matchTestAdminDisplayName":"mcrawford457","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":"//mediasvc.ancestry.com/v2/image/namespaces/60564/media/ba58c230-9bef-4fe5-b9de-7c377077feea?Client=DnaWeb","matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"ACF926F8-0DF7-47AE-A214-52FDBC3F7AF9","meiosisValue":9,"confidence":86.558,"sharedCentimorgans":32.2576,"sharedSegments":3,"note":null,"relativeDate":{"date":1520975060000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"bensonchristopher85","matchTestAdminDisplayName":"bensonchristopher85","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":"//mediasvc.ancestry.com/v2/image/namespaces/60564/media/a3cf68e4-2a17-4de1-93f6-1c468f849c53?Client=DnaWeb","matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"FF0A79CC-C29F-44F6-BB9F-FD605705BCCA","meiosisValue":9,"confidence":86.081,"sharedCentimorgans":31.8461,"sharedSegments":1,"note":null,"relativeDate":{"date":1516580466000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"sodonnell8677","matchTestAdminDisplayName":"sodonnell8677","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":"//mediasvc.ancestry.com/v2/image/namespaces/60564/media/d72afd80-cbef-4b16-822d-64a80cab4d0b?Client=DnaWeb","matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"958FB7FE-FB1F-4834-B39A-4AE497EC0E2C","meiosisValue":9,"confidence":85.325005,"sharedCentimorgans":31.223,"sharedSegments":4,"note":null,"relativeDate":{"date":1506408428000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Michelle McNeill","matchTestAdminDisplayName":"Michelle McNeill","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"FE772AD0-9FE5-48D2-882B-A24C82942658","meiosisValue":9,"confidence":85.071,"sharedCentimorgans":31.0204,"sharedSegments":2,"note":null,"relativeDate":{"date":null,"propName":"relativeelapsedtime.yesterday","timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"craftypat2004","matchTestAdminDisplayName":"craftypat2004","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"4390DD26-EEF2-42BB-BBF2-D064164CF27C","meiosisValue":9,"confidence":84.438,"sharedCentimorgans":30.5322,"sharedSegments":1,"note":null,"relativeDate":{"date":1512007859000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"woolman190","matchTestAdminDisplayName":"woolman190","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":"//mediasvc.ancestry.com/v2/image/namespaces/60564/media/4398a8aa-31f4-4256-9eac-1af4d497e717?Client=DnaWeb","matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":true,"viewed":true,"ignored":false,"lastLoggedInDate":null,"testGuid":"3629EC24-C5CF-40B6-97CB-4531A3DD13CC","meiosisValue":9,"confidence":84.298004,"sharedCentimorgans":30.4268,"sharedSegments":2,"note":"M:4C","relativeDate":{"date":null,"propName":"relativeelapsedtime.ndaysago","timeUnits":5},"hideManagedByInfo":false,"hasNote":true},{"dnaMatch":true,"matchTestDisplayName":"Phillip Capone","matchTestAdminDisplayName":"Phillip Capone","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"6F78BB78-FFDE-4C9C-9840-C1E4F0DA6343","meiosisValue":9,"confidence":84.12,"sharedCentimorgans":30.2939,"sharedSegments":1,"note":null,"relativeDate":{"date":1506357335000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"R.M.","matchTestAdminDisplayName":"DMcVey535","subjectGender":"MALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"21B780F8-640D-46C5-A32C-85A146A926B3","meiosisValue":9,"confidence":83.994,"sharedCentimorgans":30.201,"sharedSegments":3,"note":null,"relativeDate":{"date":1495333865000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Frances Keary","matchTestAdminDisplayName":"Frances Keary","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"03B161BB-06A0-4862-8443-BFD607663659","meiosisValue":9,"confidence":83.792,"sharedCentimorgans":30.0535,"sharedSegments":2,"note":null,"relativeDate":{"date":1521740681000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false},{"dnaMatch":true,"matchTestDisplayName":"Sylvia Joan Jenkins","matchTestAdminDisplayName":"Sylvia Joan Jenkins","subjectGender":"FEMALE","matchTestSubjectIsAdmin":false,"userPhoto":null,"matchTreeNodeCount":0,"matchTreeIsPrivate":null,"starred":false,"viewed":false,"ignored":false,"lastLoggedInDate":null,"testGuid":"C6F4F9CC-A092-4F84-83E4-8CC06388BD20","meiosisValue":9,"confidence":83.54,"sharedCentimorgans":29.8722,"sharedSegments":2,"note":null,"relativeDate":{"date":1518647862000,"propName":null,"timeUnits":null},"hideManagedByInfo":false,"hasNote":false}]}],"hasIgnored":false,"pageCount":0,"loggedInUserHasTrees":false}



data = json.loads(matches)
pprint(data)