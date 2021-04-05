# FE03
> 100pt

## Briefing
> Download the file and find a way to get the flag from the docker image.

## Solution
The provided file can be found [here](fe03.zip).

Grep makes light work of this challenge once again using the command `find . -type f | xargs strings | grep -i flag`:

```console
CDSkids@kali:~/Desktop/fe03$ find . -type f | xargs strings | grep -i flag
{"architecture":"amd64","config":{"Hostname":"e5555c83ffd1","Domainname":"","User":"","AttachStdin":false,"AttachStdout":true,"AttachStderr":true,"Tty":false,"OpenStdin":false,"StdinOnce":false,"Env":["PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"],"Cmd":["bash","/opt/hold.sh"],"Image":"fe03","Volumes":null,"WorkingDir":"","Entrypoint":null,"OnBuild":null,"Labels":{}},"container":"e5555c83ffd1599e0a76025300a62752a9e86f43563ea62f42487dbe3ad54efa","container_config":{"Hostname":"e5555c83ffd1","Domainname":"","User":"","AttachStdin":false,"AttachStdout":true,"AttachStderr":true,"Tty":false,"OpenStdin":false,"StdinOnce":false,"Env":["PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"],"Cmd":["bash","/opt/hold.sh"],"Image":"fe03","Volumes":null,"WorkingDir":"","Entrypoint":null,"OnBuild":null,"Labels":{}},"created":"2021-03-14T14:26:32.175139908Z","docker_version":"20.10.5","history":[{"created":"2021-02-17T21:19:54.634967707Z","created_by":"/bin/sh -c #(nop) ADD file:80bf8bd014071345b1c0364eeb0a5e48f3fb0d87f9c31cb990e57caa652b59b8 in / "},{"created":"2021-02-17T21:19:54.811094842Z","created_by":"/bin/sh -c #(nop)  CMD [\"/bin/sh\"]","empty_layer":true},{"created":"2021-03-14T13:40:09.260119522Z","created_by":"/bin/sh -c apk update"},{"created":"2021-03-14T13:40:10.111405825Z","created_by":"/bin/sh -c apk add --update zip"},{"created":"2021-03-14T13:41:35.618807066Z","created_by":"/bin/sh -c apk add --update bash"},{"created":"2021-03-14T13:41:36.213347028Z","created_by":"/bin/sh -c addgroup -S usergroup \u0026\u0026 adduser -S secret -G usergroup"},{"created":"2021-03-14T14:22:31.349307153Z","created_by":"/bin/sh -c #(nop) ADD file:9ae478ef983cfd7a1762156ecbf2c745eb4f54af8480753e39fcbc4296bc2cdb in /home/secret/flag.txt "},{"created":"2021-03-14T14:22:31.480943969Z","created_by":"/bin/sh -c #(nop) ADD file:89031f8d173232093e60691d7236ae59e80a5c38dbc66fc040544ecf83c1bba3 in /opt/setup.sh "},{"created":"2021-03-14T14:22:31.604890963Z","created_by":"/bin/sh -c #(nop) ADD file:40455faf708837f61a1146081e0f6cd9fb2148b04b9087a1e99608563c5153fe in /opt/hold.sh "},{"created":"2021-03-14T14:22:32.140355489Z","created_by":"/bin/sh -c chmod 777 /opt/setup.sh"},{"created":"2021-03-14T14:22:32.675736015Z","created_by":"/bin/sh -c chmod 777 /opt/hold.sh"},{"created":"2021-03-14T14:22:33.220948525Z","created_by":"/bin/sh -c chmod 777 /home/secret/flag.txt"},{"created":"2021-03-14T14:22:33.781335079Z","created_by":"/bin/sh -c chown secret:usergroup /opt/setup.sh"},{"created":"2021-03-14T14:22:34.38162559Z","created_by":"/bin/sh -c chown secret:usergroup /home/secret/flag.txt"},{"created":"2021-03-14T14:22:34.47606373Z","created_by":"/bin/sh -c #(nop)  CMD [\"bash\" \"/opt/hold.sh\"]","empty_layer":true},{"created":"2021-03-14T14:26:32.175139908Z","created_by":"bash /opt/hold.sh"}],"os":"linux","rootfs":{"type":"layers","diff_ids":["sha256:cb381a32b2296e4eb5af3f84092a2e6685e88adbc54ee0768a1a1010ce6376c7","sha256:b90fea6bd404d5b6b484b6420128470cd0b1827bb64bac8b42fa506039211052","sha256:8613a3487460184ff001c9d5e4a4cdab7cc38eeb89b51727351dc3c0c38c1a53","sha256:ccad2dc313f4d52b4b0a634f0ab3b9498386ba67c6dfd0a8273419aa0887b7e1","sha256:5aefc129b9ed971b01f07e10f8c68c3c53c0712d18bc889d1578837c52032c14","sha256:a71aa4d543e3f5496f80fc9fb95419e193dd637f7d13b3e9a4977dff79321190","sha256:53e6e4ef8e4122d1b8c877f19de92ea3ec8b76ec90aebd378ac3c0dbe60a081f","sha256:9f6678a8c34d8b5fe4738773fb0bcbbbc97ee101223d35f7692caf0bb8b48ac2","sha256:c35f02ba6c1e7dfb37cdfef06ecc2bb2182182b738b2ddbdf4f2782be960cb91","sha256:33f7caa30a818cb05e9c92212ab57e466824d4b6a6c4ba0a35a2d77566fce142","sha256:1ab27e5d47097d33490888b6fbcf9757efeb1ea1db6191053390fb48cb7f711e","sha256:73350546be98bc21709300f277f793b58dacf0e5e74b5f7489f6e6608e04a2c8","sha256:ffe82bde3af6ecf757101b8b6d4dcf52d92042e07b8e2832ee70d19b04b1488d","sha256:1664ccd6d3ad72ca54b80d8f55fe5b97a5b6ff4e67de8a814bb1a8e1034a7615"]}}                                                          
zip -P taskdeadlyauditorywoodwork flag.zip flag.txt
rm /home/secret/flag.txt
         continuing with central flag (IsUTF8 = %d)
bad flag to add_filter
local flags = 0x%04x, central = 0x%04x:
undefined bits used in flags = 0x%04x:
Local Entry Flag does not match CD:
Local Entry Flag does not match CD:
Local Entry Flag does not match CD:
Local Entry Flag does not match CD:
home/secret/.wh.flag.txt
home/secret/flag.zip
flag.txtUT
flag.txtUT
 0home/secret/flag.txt
zip -P taskdeadlyauditorywoodwork flag.zip flag.txt
rm /home/secret/flag.txt
        Flags:
, Flags:
invalid flag: %s
 flags
%s: can't get flags
[NO FLAGS]
Proto RefCnt Flags       Type       State         I-Node %sPath
%-44s%-40sFlags Metric Ref    Use Iface
Destination     Gateway         Genmask         Flags %s Iface
set_flag
flags %02x
a       toggle a read only flag
c       toggle the mountable flag
a       toggle a bootable flag
c       toggle the dos compatibility flag
flags:
%*s Flag    Start       End    Blocks   Id  System
Warning: invalid flag 0x%02x,0x%02x of partition table %u will be corrected by w(rite)
DOS Compatibility flag is %sset
can't mount %s on %s (flags:0x%lx)
zip flag %s is not supported
unknown typeflag: 0x%x
iflag
oflag
iflag
oflag
has_flag() {
while has_flag tentative && ! has_flag dadfailed; do
1CV2yreN1x5KZmTNXMWcg+HCCIia7E6j8T4cLNlsHaFLAgMBAAGjgYowgYcwDwYD
# Use the "--openssl_output" flag.
# Use the "--openssl_output" flag.
#opt sipsrv     STRING LIST     # [0x78] RFC 3361. flag byte, then: 0: domain names, 1: IP addrs
fegetexceptflag
fesetexceptflag
_ns_flagdata
posix_spawnattr_getflags
posix_spawnattr_setflags
Invalid flags
apk_flags
EVP_MD_CTX_set_flags
EVP_MD_CTX_clear_flags
apk_solver_set_name_flags
X509_STORE_set_flags
Invalid open flags (internal error)
BIO_clear_flags
ASN1_PCTX_get_flags
ASN1_PCTX_set_flags
ASN1_PCTX_get_nm_flags
ASN1_PCTX_set_nm_flags
ASN1_PCTX_get_cert_flags
ASN1_PCTX_set_cert_flags
ASN1_PCTX_get_oid_flags
ASN1_PCTX_set_oid_flags
ASN1_PCTX_get_str_flags
ASN1_PCTX_set_str_flags
ASN1_SCTX_get_flags
BN_set_flags
BIO_set_flags
BIO_test_flags
BN_get_flags
BN_BLINDING_get_flags
BN_BLINDING_set_flags
BN_with_flags
EVP_MD_CTX_set_flags
EVP_CIPHER_CTX_set_flags
EVP_CIPHER_flags
OPENSSL_INIT_set_config_file_flags
CONF_imodule_get_flags
CONF_imodule_set_flags
DH_clear_flags
DH_test_flags
DH_set_flags
DH_meth_get_flags
DH_meth_set_flags
DSA_clear_flags
DSA_test_flags
DSA_set_flags
DSA_meth_get_flags
DSA_meth_set_flags
DSO_flags
EC_GROUP_set_asn1_flag
EC_GROUP_get_asn1_flag
EC_KEY_get_enc_flags
EC_KEY_set_enc_flags
EC_KEY_set_asn1_flag
EC_KEY_get_flags
EC_KEY_set_flags
EC_KEY_clear_flags
ENGINE_set_flags
ENGINE_get_flags
EVP_MD_meth_set_flags
EVP_CIPHER_meth_set_flags
ENGINE_get_table_flags
ENGINE_set_table_flags
EVP_MD_CTX_test_flags
EVP_MD_CTX_clear_flags
EVP_CIPHER_CTX_test_flags
EVP_MD_flags
EVP_MD_meth_get_flags
EVP_CIPHER_CTX_clear_flags
HMAC_CTX_set_flags
X509_get_extension_flags
RSA_flags
RSA_clear_flags
RSA_test_flags
RSA_set_flags
RSA_meth_get_flags
RSA_meth_set_flags
TS_RESP_CTX_add_flags
TS_VERIFY_CTX_add_flags
TS_VERIFY_CTX_set_flags
UI_get_input_flags
X509_STORE_set_flags
X509_VERIFY_PARAM_set_flags
X509_TRUST_get_flags
X509_STORE_CTX_set_flags
X509_VERIFY_PARAM_clear_flags
X509_VERIFY_PARAM_get_flags
X509_VERIFY_PARAM_get_inh_flags
X509_VERIFY_PARAM_set_inh_flags
X509_VERIFY_PARAM_set_hostflags
X509_VERIFY_PARAM_get_hostflags
X509_set_proxy_flag
asn1_item_flags_i2d
unsupported drbg flags
proxy certificates not allowed, please set the appropriate flag
BIO_clear_flags
BIO_set_flags
BIO_test_flags
EVP_CIPHER_flags
EVP_MD_CTX_set_flags
X509_STORE_CTX_set_flags
X509_get_extension_flags
SSL_CONF_CTX_set_flags
SSL_CONF_CTX_clear_flags
SSL_set_hostflags
X509_VERIFY_PARAM_set_hostflags
SSL_CTX_dane_set_flags
SSL_CTX_dane_clear_flags
SSL_dane_set_flags
SSL_dane_clear_flags
flags
zlibCompileFlags
unknown header flags set
apk_solver_set_name_flags
apk_flags
ai_flags
%s%s%s: inconsistent state detected.  flags=%lX
DT_FLAGS
DT_FLAGS_1
PT_PAX_FLAGS
%s%s%s: Invalid section flags for GNU-stack
Sets EI_PAX/PT_PAX_FLAGS to <arg> (use with -Xx)
EVP_CIPHER_meth_set_flags
EVP_CIPHER_meth_set_flags
EVP_CIPHER_flags
X509_VERIFY_PARAM_set_flags
BIO_clear_flags
BIO_set_flags
zip -P taskdeadlyauditorywoodwork flag.zip flag.txt
rm /home/secret/flag.txt
home/secret/flag.txt
Flag: 8191-SiMpLeFilESysTemForens1Cs
return_catch_flag
get_current_flags
errexit_flag
verbose_flag
initialize_flags
find_flag
set_current_flags
which_set_flags
histexp_flag
make_word_flags
change_flag
optflags
wait_intr_flag
reset_shell_flags
jobs_m_flag
      -H  Enable ! style history substitution.  This flag is on
    Using + rather than - causes these flags to be turned off.  The
    flags can also be used upon invocation of the shell.  The current
    set of flags may be found in $-.  The remaining n ARGs are positional
    is trapped and flagged as an error.  The following list of operators is
R:fdflags
usr/lib/bash/fdflags
fdflags_builtin
fdflags_struct
fdflags_doc
fdflags
Can't get flags for fd %d: %s
can't set flags for fd %d: %s
invalid flag `%s'
fdflags
fdflags [-v] [-s flags_string] [fd ...]
Display and modify file descriptor flags.
Display or, if the -s option is supplied, set flags for each file
The -s option accepts a string with a list of flag names, each preceded
consists of the status of flags for each of the shell's open files.
fdflags.debug
tigetflag
tgetflag_sp
tgetflag
tigetflag_sp
flag
_flags
_rl_meta_flag
tgetflag
meta-flag
zip -P taskdeadlyauditorywoodwork flag.zip flag.txt
rm /home/secret/flag.txt
home/secret/flag.txt
Flag: 8191-SiMpLeFilESysTemForens1Cs
home/secret/flag.txt
Flag: 8191-SiMpLeFilESysTemForens1Cs
```

## Flag
Flag: `8191-SiMpLeFilESysTemForens1Cs`
