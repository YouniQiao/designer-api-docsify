# @ohos.security.certManager

证书管理主要提供系统级的证书管理能力，实现证书全生命周期（安装，存储，使用，销毁）的管理和安全使用。 可用于校验应用服务器的HTTPS证书链、通过双向HTTPS登录网站或应用服务器。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace certificateManager--><!--Device-unnamed-declare namespace certificateManager-End-->

**系统能力：** SystemCapability.Security.CertificateManager

## 汇总

### 函数

| 名称 |
| --- |
| [abort](arkts-devicecertificate-certificatemanager-abort-f.md#abort) |
| [abort](arkts-devicecertificate-certificatemanager-abort-f.md#abort) |
| [finish](arkts-devicecertificate-certificatemanager-finish-f.md#finish) |
| [finish](arkts-devicecertificate-certificatemanager-finish-f.md#finish) |
| [finish](arkts-devicecertificate-certificatemanager-finish-f.md#finish) |
| [getAllUserTrustedCertificates](arkts-devicecertificate-certificatemanager-getallusertrustedcertificates-f.md#getAllUserTrustedCertificates) |
| [getAllUserTrustedCertificates](arkts-devicecertificate-certificatemanager-getallusertrustedcertificates-f.md#getAllUserTrustedCertificates) |
| [getCertificateStorePath](arkts-devicecertificate-certificatemanager-getcertificatestorepath-f.md#getCertificateStorePath) |
| [getPrivateCertificate](arkts-devicecertificate-certificatemanager-getprivatecertificate-f.md#getPrivateCertificate) |
| [getPrivateCertificate](arkts-devicecertificate-certificatemanager-getprivatecertificate-f.md#getPrivateCertificate) |
| [getPrivateCertificates](arkts-devicecertificate-certificatemanager-getprivatecertificates-f.md#getPrivateCertificates) |
| [getPublicCertificate](arkts-devicecertificate-certificatemanager-getpubliccertificate-f.md#getPublicCertificate) |
| [getUkeyCertificate](arkts-devicecertificate-certificatemanager-getukeycertificate-f.md#getUkeyCertificate) |
| [getUkeyCertificateList](arkts-devicecertificate-certificatemanager-getukeycertificatelist-f.md#getUkeyCertificateList) |
| [getUserTrustedCertificate](arkts-devicecertificate-certificatemanager-getusertrustedcertificate-f.md#getUserTrustedCertificate) |
| [importUkeyCertificate](arkts-devicecertificate-certificatemanager-importukeycertificate-f.md#importUkeyCertificate) |
| [init](arkts-devicecertificate-certificatemanager-init-f.md#init) |
| [init](arkts-devicecertificate-certificatemanager-init-f.md#init) |
| [installPrivateCertificate](arkts-devicecertificate-certificatemanager-installprivatecertificate-f.md#installPrivateCertificate) |
| [installPrivateCertificate](arkts-devicecertificate-certificatemanager-installprivatecertificate-f.md#installPrivateCertificate) |
| [installPrivateCertificate](arkts-devicecertificate-certificatemanager-installprivatecertificate-f.md#installPrivateCertificate) |
| [installUserTrustedCertificate](arkts-devicecertificate-certificatemanager-installusertrustedcertificate-f.md#installUserTrustedCertificate) |
| [installUserTrustedCertificateSync](arkts-devicecertificate-certificatemanager-installusertrustedcertificatesync-f.md#installUserTrustedCertificateSync) |
| [isAuthorizedApp](arkts-devicecertificate-certificatemanager-isauthorizedapp-f.md#isAuthorizedApp) |
| [uninstallPrivateCertificate](arkts-devicecertificate-certificatemanager-uninstallprivatecertificate-f.md#uninstallPrivateCertificate) |
| [uninstallPrivateCertificate](arkts-devicecertificate-certificatemanager-uninstallprivatecertificate-f.md#uninstallPrivateCertificate) |
| [uninstallUserTrustedCertificateSync](arkts-devicecertificate-certificatemanager-uninstallusertrustedcertificatesync-f.md#uninstallUserTrustedCertificateSync) |
| [update](arkts-devicecertificate-certificatemanager-update-f.md#update) |
| [update](arkts-devicecertificate-certificatemanager-update-f.md#update) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getAllAppPrivateCertificates](arkts-devicecertificate-certificatemanager-getallappprivatecertificates-f-sys.md#getAllAppPrivateCertificates（系统接口）) |
| [getAllAppPrivateCertificates](arkts-devicecertificate-certificatemanager-getallappprivatecertificates-f-sys.md#getAllAppPrivateCertificates（系统接口）) |
| [getAllAppPrivateCertificatesByUid](arkts-devicecertificate-certificatemanager-getallappprivatecertificatesbyuid-f-sys.md#getAllAppPrivateCertificatesByUid（系统接口）) |
| [getAllPublicCertificates](arkts-devicecertificate-certificatemanager-getallpubliccertificates-f-sys.md#getAllPublicCertificates（系统接口）) |
| [getAllSystemAppCertificates](arkts-devicecertificate-certificatemanager-getallsystemappcertificates-f-sys.md#getAllSystemAppCertificates（系统接口）) |
| [getAuthorizedAppList](arkts-devicecertificate-certificatemanager-getauthorizedapplist-f-sys.md#getAuthorizedAppList（系统接口）) |
| [getSystemAppCertificate](arkts-devicecertificate-certificatemanager-getsystemappcertificate-f-sys.md#getSystemAppCertificate（系统接口）) |
| [getSystemTrustedCertificate](arkts-devicecertificate-certificatemanager-getsystemtrustedcertificate-f-sys.md#getSystemTrustedCertificate（系统接口）) |
| [getSystemTrustedCertificateList](arkts-devicecertificate-certificatemanager-getsystemtrustedcertificatelist-f-sys.md#getSystemTrustedCertificateList（系统接口）) |
| [grantPublicCertificate](arkts-devicecertificate-certificatemanager-grantpubliccertificate-f-sys.md#grantPublicCertificate（系统接口）) |
| [installPublicCertificate](arkts-devicecertificate-certificatemanager-installpubliccertificate-f-sys.md#installPublicCertificate（系统接口）) |
| [installSystemAppCertificate](arkts-devicecertificate-certificatemanager-installsystemappcertificate-f-sys.md#installSystemAppCertificate（系统接口）) |
| [removeGrantedPublicCertificate](arkts-devicecertificate-certificatemanager-removegrantedpubliccertificate-f-sys.md#removeGrantedPublicCertificate（系统接口）) |
| [setCertificateStatus](arkts-devicecertificate-certificatemanager-setcertificatestatus-f-sys.md#setCertificateStatus（系统接口）) |
| [uninstallAllAppCertificate](arkts-devicecertificate-certificatemanager-uninstallallappcertificate-f-sys.md#uninstallAllAppCertificate（系统接口）) |
| [uninstallAllUserTrustedCertificate](arkts-devicecertificate-certificatemanager-uninstallallusertrustedcertificate-f-sys.md#uninstallAllUserTrustedCertificate（系统接口）) |
| [uninstallPublicCertificate](arkts-devicecertificate-certificatemanager-uninstallpubliccertificate-f-sys.md#uninstallPublicCertificate（系统接口）) |
| [uninstallSystemAppCertificate](arkts-devicecertificate-certificatemanager-uninstallsystemappcertificate-f-sys.md#uninstallSystemAppCertificate（系统接口）) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [CMHandle](arkts-devicecertificate-certificatemanager-cmhandle-i.md) |
| [CMResult](arkts-devicecertificate-certificatemanager-cmresult-i.md) |
| [CMSignatureSpec](arkts-devicecertificate-certificatemanager-cmsignaturespec-i.md) |
| [CertAbstract](arkts-devicecertificate-certificatemanager-certabstract-i.md) |
| [CertBlob](arkts-devicecertificate-certificatemanager-certblob-i.md) |
| [CertInfo](arkts-devicecertificate-certificatemanager-certinfo-i.md) |
| [CertStoreProperty](arkts-devicecertificate-certificatemanager-certstoreproperty-i.md) |
| [Credential](arkts-devicecertificate-certificatemanager-credential-i.md) |
| [CredentialAbstract](arkts-devicecertificate-certificatemanager-credentialabstract-i.md) |
| [UkeyInfo](arkts-devicecertificate-certificatemanager-ukeyinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [AuthStorageLevel](arkts-devicecertificate-certificatemanager-authstoragelevel-e.md) |
| [CMErrorCode](arkts-devicecertificate-certificatemanager-cmerrorcode-e.md) |
| [CertAlgorithm](arkts-devicecertificate-certificatemanager-certalgorithm-e.md) |
| [CertFileFormat](arkts-devicecertificate-certificatemanager-certfileformat-e.md) |
| [CertScope](arkts-devicecertificate-certificatemanager-certscope-e.md) |
| [CertType](arkts-devicecertificate-certificatemanager-certtype-e.md) |
| [CertificatePurpose](arkts-devicecertificate-certificatemanager-certificatepurpose-e.md) |
| [CmKeyDigest](arkts-devicecertificate-certificatemanager-cmkeydigest-e.md) |
| [CmKeyPadding](arkts-devicecertificate-certificatemanager-cmkeypadding-e.md) |
| [CmKeyPurpose](arkts-devicecertificate-certificatemanager-cmkeypurpose-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [CMErrorCode](arkts-devicecertificate-certificatemanager-cmerrorcode-e-sys.md) |
<!--DelEnd-->
