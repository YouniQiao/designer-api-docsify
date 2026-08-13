# @ohos.security.certManager

The **certManager** module provides system-level certificate management capabilities to implement management and secure use of certificates throughout their lifecycle (installation, storage, use, and destruction). It can be used to verify the HTTPS certificate chain of the application server , and log in to the website or application server using two-way HTTPS.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace certificateManager--><!--Device-unnamed-declare namespace certificateManager-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAllAppPrivateCertificates](arkts-devicecertificate-certificatemanager-getallappprivatecertificates-f-sys.md#getAllAppPrivateCertificates-(System-API)) |
| [getAllAppPrivateCertificates](arkts-devicecertificate-certificatemanager-getallappprivatecertificates-f-sys.md#getAllAppPrivateCertificates-(System-API)) |
| [getAllAppPrivateCertificatesByUid](arkts-devicecertificate-certificatemanager-getallappprivatecertificatesbyuid-f-sys.md#getAllAppPrivateCertificatesByUid-(System-API)) |
| [getAllPublicCertificates](arkts-devicecertificate-certificatemanager-getallpubliccertificates-f-sys.md#getAllPublicCertificates-(System-API)) |
| [getAllSystemAppCertificates](arkts-devicecertificate-certificatemanager-getallsystemappcertificates-f-sys.md#getAllSystemAppCertificates-(System-API)) |
| [getAuthorizedAppList](arkts-devicecertificate-certificatemanager-getauthorizedapplist-f-sys.md#getAuthorizedAppList-(System-API)) |
| [getSystemAppCertificate](arkts-devicecertificate-certificatemanager-getsystemappcertificate-f-sys.md#getSystemAppCertificate-(System-API)) |
| [getSystemTrustedCertificate](arkts-devicecertificate-certificatemanager-getsystemtrustedcertificate-f-sys.md#getSystemTrustedCertificate-(System-API)) |
| [getSystemTrustedCertificateList](arkts-devicecertificate-certificatemanager-getsystemtrustedcertificatelist-f-sys.md#getSystemTrustedCertificateList-(System-API)) |
| [grantPublicCertificate](arkts-devicecertificate-certificatemanager-grantpubliccertificate-f-sys.md#grantPublicCertificate-(System-API)) |
| [installPublicCertificate](arkts-devicecertificate-certificatemanager-installpubliccertificate-f-sys.md#installPublicCertificate-(System-API)) |
| [installSystemAppCertificate](arkts-devicecertificate-certificatemanager-installsystemappcertificate-f-sys.md#installSystemAppCertificate-(System-API)) |
| [removeGrantedPublicCertificate](arkts-devicecertificate-certificatemanager-removegrantedpubliccertificate-f-sys.md#removeGrantedPublicCertificate-(System-API)) |
| [setCertificateStatus](arkts-devicecertificate-certificatemanager-setcertificatestatus-f-sys.md#setCertificateStatus-(System-API)) |
| [uninstallAllAppCertificate](arkts-devicecertificate-certificatemanager-uninstallallappcertificate-f-sys.md#uninstallAllAppCertificate-(System-API)) |
| [uninstallAllUserTrustedCertificate](arkts-devicecertificate-certificatemanager-uninstallallusertrustedcertificate-f-sys.md#uninstallAllUserTrustedCertificate-(System-API)) |
| [uninstallPublicCertificate](arkts-devicecertificate-certificatemanager-uninstallpubliccertificate-f-sys.md#uninstallPublicCertificate-(System-API)) |
| [uninstallSystemAppCertificate](arkts-devicecertificate-certificatemanager-uninstallsystemappcertificate-f-sys.md#uninstallSystemAppCertificate-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CMErrorCode](arkts-devicecertificate-certificatemanager-cmerrorcode-e-sys.md) |
<!--DelEnd-->
