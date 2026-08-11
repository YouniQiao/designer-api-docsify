# @ohos.security.certManager

The **certManager** module provides system-level certificate management capabilities to implement management and secure use of certificates throughout their lifecycle (installation, storage, use, and destruction).

It can be used to verify the HTTPS certificate chain of the application server , and log in to the website or application server using two-way HTTPS.

**Since:** 11

<!--Device-unnamed-declare namespace certificateManager--><!--Device-unnamed-declare namespace certificateManager-End-->

**System capability:** SystemCapability.Security.CertificateManager

## Modules to Import

```TypeScript
import { certificateManager } from 'kits/@kit.DeviceCertificateKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [abort](arkts-devicecertificate-certificatemanager-abort-f.md#abort) |
| [abort](arkts-devicecertificate-certificatemanager-abort-f.md#abort-1) |
| [finish](arkts-devicecertificate-certificatemanager-finish-f.md#finish) |
| [finish](arkts-devicecertificate-certificatemanager-finish-f.md#finish-1) |
| [finish](arkts-devicecertificate-certificatemanager-finish-f.md#finish-2) |
| [getAllUserTrustedCertificates](arkts-devicecertificate-certificatemanager-getallusertrustedcertificates-f.md#getallusertrustedcertificates) |
| [getAllUserTrustedCertificates](arkts-devicecertificate-certificatemanager-getallusertrustedcertificates-f.md#getallusertrustedcertificates-1) |
| [getCertificateStorePath](arkts-devicecertificate-certificatemanager-getcertificatestorepath-f.md#getcertificatestorepath) |
| [getPrivateCertificate](arkts-devicecertificate-certificatemanager-getprivatecertificate-f.md#getprivatecertificate) |
| [getPrivateCertificate](arkts-devicecertificate-certificatemanager-getprivatecertificate-f.md#getprivatecertificate-1) |
| [getPrivateCertificates](arkts-devicecertificate-certificatemanager-getprivatecertificates-f.md#getprivatecertificates) |
| [getPublicCertificate](arkts-devicecertificate-certificatemanager-getpubliccertificate-f.md#getpubliccertificate) |
| [getUkeyCertificate](arkts-devicecertificate-certificatemanager-getukeycertificate-f.md#getukeycertificate) |
| [getUkeyCertificateList](arkts-devicecertificate-certificatemanager-getukeycertificatelist-f.md#getukeycertificatelist) |
| [getUserTrustedCertificate](arkts-devicecertificate-certificatemanager-getusertrustedcertificate-f.md#getusertrustedcertificate) |
| [importUkeyCertificate](arkts-devicecertificate-certificatemanager-importukeycertificate-f.md#importukeycertificate) |
| [init](arkts-devicecertificate-certificatemanager-init-f.md#init) |
| [init](arkts-devicecertificate-certificatemanager-init-f.md#init-1) |
| [installPrivateCertificate](arkts-devicecertificate-certificatemanager-installprivatecertificate-f.md#installprivatecertificate) |
| [installPrivateCertificate](arkts-devicecertificate-certificatemanager-installprivatecertificate-f.md#installprivatecertificate-1) |
| [installPrivateCertificate](arkts-devicecertificate-certificatemanager-installprivatecertificate-f.md#installprivatecertificate-2) |
| [installUserTrustedCertificate](arkts-devicecertificate-certificatemanager-installusertrustedcertificate-f.md#installusertrustedcertificate) |
| [installUserTrustedCertificateSync](arkts-devicecertificate-certificatemanager-installusertrustedcertificatesync-f.md#installusertrustedcertificatesync) |
| [isAuthorizedApp](arkts-devicecertificate-certificatemanager-isauthorizedapp-f.md#isauthorizedapp) |
| [uninstallPrivateCertificate](arkts-devicecertificate-certificatemanager-uninstallprivatecertificate-f.md#uninstallprivatecertificate) |
| [uninstallPrivateCertificate](arkts-devicecertificate-certificatemanager-uninstallprivatecertificate-f.md#uninstallprivatecertificate-1) |
| [uninstallUserTrustedCertificateSync](arkts-devicecertificate-certificatemanager-uninstallusertrustedcertificatesync-f.md#uninstallusertrustedcertificatesync) |
| [update](arkts-devicecertificate-certificatemanager-update-f.md#update) |
| [update](arkts-devicecertificate-certificatemanager-update-f.md#update-1) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAllAppPrivateCertificates](arkts-devicecertificate-certificatemanager-getallappprivatecertificates-f-sys.md#getallappprivatecertificates) |
| [getAllAppPrivateCertificates](arkts-devicecertificate-certificatemanager-getallappprivatecertificates-f-sys.md#getallappprivatecertificates-1) |
| [getAllAppPrivateCertificatesByUid](arkts-devicecertificate-certificatemanager-getallappprivatecertificatesbyuid-f-sys.md#getallappprivatecertificatesbyuid) |
| [getAllPublicCertificates](arkts-devicecertificate-certificatemanager-getallpubliccertificates-f-sys.md#getallpubliccertificates) |
| [getAllSystemAppCertificates](arkts-devicecertificate-certificatemanager-getallsystemappcertificates-f-sys.md#getallsystemappcertificates) |
| [getAuthorizedAppList](arkts-devicecertificate-certificatemanager-getauthorizedapplist-f-sys.md#getauthorizedapplist) |
| [getSystemAppCertificate](arkts-devicecertificate-certificatemanager-getsystemappcertificate-f-sys.md#getsystemappcertificate) |
| [getSystemTrustedCertificate](arkts-devicecertificate-certificatemanager-getsystemtrustedcertificate-f-sys.md#getsystemtrustedcertificate) |
| [getSystemTrustedCertificateList](arkts-devicecertificate-certificatemanager-getsystemtrustedcertificatelist-f-sys.md#getsystemtrustedcertificatelist) |
| [grantPublicCertificate](arkts-devicecertificate-certificatemanager-grantpubliccertificate-f-sys.md#grantpubliccertificate) |
| [installPublicCertificate](arkts-devicecertificate-certificatemanager-installpubliccertificate-f-sys.md#installpubliccertificate) |
| [installSystemAppCertificate](arkts-devicecertificate-certificatemanager-installsystemappcertificate-f-sys.md#installsystemappcertificate) |
| [removeGrantedPublicCertificate](arkts-devicecertificate-certificatemanager-removegrantedpubliccertificate-f-sys.md#removegrantedpubliccertificate) |
| [setCertificateStatus](arkts-devicecertificate-certificatemanager-setcertificatestatus-f-sys.md#setcertificatestatus) |
| [uninstallAllAppCertificate](arkts-devicecertificate-certificatemanager-uninstallallappcertificate-f-sys.md#uninstallallappcertificate) |
| [uninstallAllUserTrustedCertificate](arkts-devicecertificate-certificatemanager-uninstallallusertrustedcertificate-f-sys.md#uninstallallusertrustedcertificate) |
| [uninstallPublicCertificate](arkts-devicecertificate-certificatemanager-uninstallpubliccertificate-f-sys.md#uninstallpubliccertificate) |
| [uninstallSystemAppCertificate](arkts-devicecertificate-certificatemanager-uninstallsystemappcertificate-f-sys.md#uninstallsystemappcertificate) |
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
