# @ohos.enterprise.securityManager(Security Management)

This module provides enterprise device security management capabilities, including certificate management, device security policy management, password policy management, clipboard policy management, watermark policy management, and permission management. Enterprises can use this module to monitor the device security status in real time, manage the lifecycle of enterprise certificates, configure device password policies in a unified manner, control the use of the app clipboard, set screen and app watermarks to prevent information leakage, and implement refined management of app permissions. This helps enterprises enhance device security protection capabilities and reduce data leakage risks.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace securityManager--><!--Device-unnamed-declare namespace securityManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedPermissionBundle](arkts-mdm-securitymanager-addallowedpermissionbundle-f.md#addallowedpermissionbundle) |
| [cancelScreenWatermarkImage](arkts-mdm-securitymanager-cancelscreenwatermarkimage-f.md#cancelscreenwatermarkimage) |
| [cancelWatermarkImage](arkts-mdm-securitymanager-cancelwatermarkimage-f.md#cancelwatermarkimage) |
| [getAllowedPermissionBundles](arkts-mdm-securitymanager-getallowedpermissionbundles-f.md#getallowedpermissionbundles) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getappclipboardpolicy) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getappclipboardpolicy-1) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getappclipboardpolicy-2) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getappclipboardpolicy-3) |
| [getDeviceEncryptionStatus](arkts-mdm-securitymanager-getdeviceencryptionstatus-f.md#getdeviceencryptionstatus) |
| [getDisallowedPermissions](arkts-mdm-securitymanager-getdisallowedpermissions-f.md#getdisallowedpermissions) |
| [getExternalSourceExtensionsPolicy](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md#getexternalsourceextensionspolicy) |
| [getExternalSourceExtensionsPolicy](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md#getexternalsourceextensionspolicy-1) |
| [getPasswordPolicy](arkts-mdm-securitymanager-getpasswordpolicy-f.md#getpasswordpolicy) |
| [getPasswordPolicy](arkts-mdm-securitymanager-getpasswordpolicy-f.md#getpasswordpolicy-1) |
| [getPasswordPolicy](arkts-mdm-securitymanager-getpasswordpolicy-f.md#getpasswordpolicy-2) |
| [getPermissionManagedState](arkts-mdm-securitymanager-getpermissionmanagedstate-f.md#getpermissionmanagedstate) |
| [getSecurityPatchTag](arkts-mdm-securitymanager-getsecuritypatchtag-f.md#getsecuritypatchtag) |
| [getSecurityStatus](arkts-mdm-securitymanager-getsecuritystatus-f.md#getsecuritystatus) |
| [getUserCertificates](arkts-mdm-securitymanager-getusercertificates-f.md#getusercertificates) |
| [getWatermarkImageApps](arkts-mdm-securitymanager-getwatermarkimageapps-f.md#getwatermarkimageapps) |
| [installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md#installenterpriseresignaturecertificate) |
| [installUserCertificate](arkts-mdm-securitymanager-installusercertificate-f.md#installusercertificate) |
| [installUserCertificate](arkts-mdm-securitymanager-installusercertificate-f.md#installusercertificate-1) |
| [isScreenLockDisabledForAccount](arkts-mdm-securitymanager-isscreenlockdisabledforaccount-f.md#isscreenlockdisabledforaccount) |
| [removeAllowedPermissionBundle](arkts-mdm-securitymanager-removeallowedpermissionbundle-f.md#removeallowedpermissionbundle) |
| [setAppClipboardPolicy](arkts-mdm-securitymanager-setappclipboardpolicy-f.md#setappclipboardpolicy) |
| [setAppClipboardPolicy](arkts-mdm-securitymanager-setappclipboardpolicy-f.md#setappclipboardpolicy-1) |
| [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setdisallowedpermission) |
| [setExternalSourceExtensionsPolicy](arkts-mdm-securitymanager-setexternalsourceextensionspolicy-f.md#setexternalsourceextensionspolicy) |
| [setPasswordPolicy](arkts-mdm-securitymanager-setpasswordpolicy-f.md#setpasswordpolicy) |
| [setPermissionManagedState](arkts-mdm-securitymanager-setpermissionmanagedstate-f.md#setpermissionmanagedstate) |
| [setScreenLockDisabledForAccount](arkts-mdm-securitymanager-setscreenlockdisabledforaccount-f.md#setscreenlockdisabledforaccount) |
| [setScreenWatermarkImage](arkts-mdm-securitymanager-setscreenwatermarkimage-f.md#setscreenwatermarkimage) |
| [setWatermarkImage](arkts-mdm-securitymanager-setwatermarkimage-f.md#setwatermarkimage) |
| [setWatermarkImage](arkts-mdm-securitymanager-setwatermarkimage-f.md#setwatermarkimage-1) |
| [uninstallEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-uninstallenterpriseresignaturecertificate-f.md#uninstallenterpriseresignaturecertificate) |
| [uninstallUserCertificate](arkts-mdm-securitymanager-uninstallusercertificate-f.md#uninstallusercertificate) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationInstance](arkts-mdm-securitymanager-applicationinstance-i.md) |
| [CertBlob](arkts-mdm-securitymanager-certblob-i.md) |
| [DeviceEncryptionStatus](arkts-mdm-securitymanager-deviceencryptionstatus-i.md) |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |
| [WatermarkProperties](arkts-mdm-securitymanager-watermarkproperties-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ClipboardPolicy](arkts-mdm-securitymanager-clipboardpolicy-e.md) |
| [PasswordAlgs](arkts-mdm-securitymanager-passwordalgs-e.md) |
| [PermissionManagedState](arkts-mdm-securitymanager-permissionmanagedstate-e.md) |
