# @ohos.enterprise.securityManager(Security Management)

This module provides enterprise device security management capabilities, including certificate management, device security policy management, password policy management, clipboard policy management, watermark policy management, and permission management. Enterprises can use this module to monitor the device security status in real time, manage the lifecycle of enterprise certificates, configure device password policies in a unified manner, control the use of the app clipboard, set screen and app watermarks to prevent information leakage, and implement refined management of app permissions. This helps enterprises enhance device security protection capabilities and reduce data leakage risks.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedPermissionBundle(Security Management)](arkts-mdm-securitymanager-addallowedpermissionbundle-f.md) |
| [cancelScreenWatermarkImage(Security Management)](arkts-mdm-securitymanager-cancelscreenwatermarkimage-f.md) |
| [cancelWatermarkImage(Security Management)](arkts-mdm-securitymanager-cancelwatermarkimage-f.md) |
| [getAllowedPermissionBundles(Security Management)](arkts-mdm-securitymanager-getallowedpermissionbundles-f.md) |
| [getAppClipboardPolicy(Security Management)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getAppClipboardPolicy(Security Management)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getAppClipboardPolicy(Security Management)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getAppClipboardPolicy(Security Management)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getDisallowedPermissions(Security Management)](arkts-mdm-securitymanager-getdisallowedpermissions-f.md) |
| [getExternalSourceExtensionsPolicy(Security Management)](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md) |
| [getExternalSourceExtensionsPolicy(Security Management)](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md) |
| [getPasswordPolicy(Security Management)](arkts-mdm-securitymanager-getpasswordpolicy-f.md) |
| [getPasswordPolicy(Security Management)](arkts-mdm-securitymanager-getpasswordpolicy-f.md) |
| [getPermissionManagedState(Security Management)](arkts-mdm-securitymanager-getpermissionmanagedstate-f.md) |
| [getSecurityStatus(Security Management)](arkts-mdm-securitymanager-getsecuritystatus-f.md) |
| [getUserCertificates(Security Management)](arkts-mdm-securitymanager-getusercertificates-f.md) |
| [getWatermarkImageApps(Security Management)](arkts-mdm-securitymanager-getwatermarkimageapps-f.md) |
| [installEnterpriseReSignatureCertificate(Security Management)](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md) |
| [installUserCertificate(Security Management)](arkts-mdm-securitymanager-installusercertificate-f.md) |
| [installUserCertificate(Security Management)](arkts-mdm-securitymanager-installusercertificate-f.md) |
| [isScreenLockDisabledForAccount(Security Management)](arkts-mdm-securitymanager-isscreenlockdisabledforaccount-f.md) |
| [removeAllowedPermissionBundle(Security Management)](arkts-mdm-securitymanager-removeallowedpermissionbundle-f.md) |
| [setAppClipboardPolicy(Security Management)](arkts-mdm-securitymanager-setappclipboardpolicy-f.md) |
| [setAppClipboardPolicy(Security Management)](arkts-mdm-securitymanager-setappclipboardpolicy-f.md) |
| [setDisallowedPermission(Security Management)](arkts-mdm-securitymanager-setdisallowedpermission-f.md) |
| [setExternalSourceExtensionsPolicy(Security Management)](arkts-mdm-securitymanager-setexternalsourceextensionspolicy-f.md) |
| [setPasswordPolicy(Security Management)](arkts-mdm-securitymanager-setpasswordpolicy-f.md) |
| [setPermissionManagedState(Security Management)](arkts-mdm-securitymanager-setpermissionmanagedstate-f.md) |
| [setScreenLockDisabledForAccount(Security Management)](arkts-mdm-securitymanager-setscreenlockdisabledforaccount-f.md) |
| [setScreenWatermarkImage(Security Management)](arkts-mdm-securitymanager-setscreenwatermarkimage-f.md) |
| [setWatermarkImage(Security Management)](arkts-mdm-securitymanager-setwatermarkimage-f.md) |
| [setWatermarkImage(Security Management)](arkts-mdm-securitymanager-setwatermarkimage-f.md) |
| [uninstallEnterpriseReSignatureCertificate(Security Management)](arkts-mdm-securitymanager-uninstallenterpriseresignaturecertificate-f.md) |
| [uninstallUserCertificate(Security Management)](arkts-mdm-securitymanager-uninstallusercertificate-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getDeviceEncryptionStatus(Security Management)](arkts-mdm-securitymanager-getdeviceencryptionstatus-f-sys.md) |
| [getPasswordPolicy(Security Management)](arkts-mdm-securitymanager-getpasswordpolicy-f-sys.md) |
| [getSecurityPatchTag(Security Management)](arkts-mdm-securitymanager-getsecuritypatchtag-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationInstance(Security Management)](arkts-mdm-securitymanager-applicationinstance-i.md) |
| [CertBlob(Security Management)](arkts-mdm-securitymanager-certblob-i.md) |
| [PasswordPolicy(Security Management)](arkts-mdm-securitymanager-passwordpolicy-i.md) |
| [WatermarkProperties(Security Management)](arkts-mdm-securitymanager-watermarkproperties-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceEncryptionStatus(Security Management)](arkts-mdm-securitymanager-deviceencryptionstatus-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ClipboardPolicy(Security Management)](arkts-mdm-securitymanager-clipboardpolicy-e.md) |
| [PasswordAlgs(Security Management)](arkts-mdm-securitymanager-passwordalgs-e.md) |
| [PermissionManagedState(Security Management)](arkts-mdm-securitymanager-permissionmanagedstate-e.md) |
