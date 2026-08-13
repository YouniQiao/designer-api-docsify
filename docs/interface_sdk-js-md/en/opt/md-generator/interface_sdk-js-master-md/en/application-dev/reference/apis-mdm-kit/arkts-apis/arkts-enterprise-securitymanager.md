# @ohos.enterprise.securityManager(Security Management)

/*
 Copyright (c) 2023-2024 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace securityManager--><!--Device-unnamed-declare namespace securityManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { securityManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedPermissionBundle](arkts-mdm-securitymanager-addallowedpermissionbundle-f.md#addAllowedPermissionBundle) |
| [cancelScreenWatermarkImage](arkts-mdm-securitymanager-cancelscreenwatermarkimage-f.md#cancelScreenWatermarkImage) |
| [cancelWatermarkImage](arkts-mdm-securitymanager-cancelwatermarkimage-f.md#cancelWatermarkImage) |
| [getAllowedPermissionBundles](arkts-mdm-securitymanager-getallowedpermissionbundles-f.md#getAllowedPermissionBundles) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getAppClipboardPolicy) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getAppClipboardPolicy) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getAppClipboardPolicy) |
| [getAppClipboardPolicy](arkts-mdm-securitymanager-getappclipboardpolicy-f.md#getAppClipboardPolicy) |
| [getDisallowedPermissions](arkts-mdm-securitymanager-getdisallowedpermissions-f.md#getDisallowedPermissions) |
| [getExternalSourceExtensionsPolicy](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md#getExternalSourceExtensionsPolicy) |
| [getExternalSourceExtensionsPolicy](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md#getExternalSourceExtensionsPolicy) |
| [getPasswordPolicy](arkts-mdm-securitymanager-getpasswordpolicy-f.md#getPasswordPolicy) |
| [getPasswordPolicy](arkts-mdm-securitymanager-getpasswordpolicy-f.md#getPasswordPolicy) |
| [getPermissionManagedState](arkts-mdm-securitymanager-getpermissionmanagedstate-f.md#getPermissionManagedState) |
| [getSecurityStatus](arkts-mdm-securitymanager-getsecuritystatus-f.md#getSecurityStatus) |
| [getUserCertificates](arkts-mdm-securitymanager-getusercertificates-f.md#getUserCertificates) |
| [getWatermarkImageApps](arkts-mdm-securitymanager-getwatermarkimageapps-f.md#getWatermarkImageApps) |
| [installEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md#installEnterpriseReSignatureCertificate) |
| [installUserCertificate](arkts-mdm-securitymanager-installusercertificate-f.md#installUserCertificate) |
| [installUserCertificate](arkts-mdm-securitymanager-installusercertificate-f.md#installUserCertificate) |
| [isScreenLockDisabledForAccount](arkts-mdm-securitymanager-isscreenlockdisabledforaccount-f.md#isScreenLockDisabledForAccount) |
| [removeAllowedPermissionBundle](arkts-mdm-securitymanager-removeallowedpermissionbundle-f.md#removeAllowedPermissionBundle) |
| [setAppClipboardPolicy](arkts-mdm-securitymanager-setappclipboardpolicy-f.md#setAppClipboardPolicy) |
| [setAppClipboardPolicy](arkts-mdm-securitymanager-setappclipboardpolicy-f.md#setAppClipboardPolicy) |
| [setDisallowedPermission](arkts-mdm-securitymanager-setdisallowedpermission-f.md#setDisallowedPermission) |
| [setExternalSourceExtensionsPolicy](arkts-mdm-securitymanager-setexternalsourceextensionspolicy-f.md#setExternalSourceExtensionsPolicy) |
| [setPasswordPolicy](arkts-mdm-securitymanager-setpasswordpolicy-f.md#setPasswordPolicy) |
| [setPermissionManagedState](arkts-mdm-securitymanager-setpermissionmanagedstate-f.md#setPermissionManagedState) |
| [setScreenLockDisabledForAccount](arkts-mdm-securitymanager-setscreenlockdisabledforaccount-f.md#setScreenLockDisabledForAccount) |
| [setScreenWatermarkImage](arkts-mdm-securitymanager-setscreenwatermarkimage-f.md#setScreenWatermarkImage) |
| [setWatermarkImage](arkts-mdm-securitymanager-setwatermarkimage-f.md#setWatermarkImage) |
| [setWatermarkImage](arkts-mdm-securitymanager-setwatermarkimage-f.md#setWatermarkImage) |
| [uninstallEnterpriseReSignatureCertificate](arkts-mdm-securitymanager-uninstallenterpriseresignaturecertificate-f.md#uninstallEnterpriseReSignatureCertificate) |
| [uninstallUserCertificate](arkts-mdm-securitymanager-uninstallusercertificate-f.md#uninstallUserCertificate) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getDeviceEncryptionStatus](arkts-mdm-securitymanager-getdeviceencryptionstatus-f-sys.md#getDeviceEncryptionStatus-(System-API)) |
| [getPasswordPolicy](arkts-mdm-securitymanager-getpasswordpolicy-f-sys.md#getPasswordPolicy-(System-API)) |
| [getSecurityPatchTag](arkts-mdm-securitymanager-getsecuritypatchtag-f-sys.md#getSecurityPatchTag-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationInstance](arkts-mdm-securitymanager-applicationinstance-i.md) |
| [CertBlob](arkts-mdm-securitymanager-certblob-i.md) |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |
| [WatermarkProperties](arkts-mdm-securitymanager-watermarkproperties-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceEncryptionStatus](arkts-mdm-securitymanager-deviceencryptionstatus-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ClipboardPolicy](arkts-mdm-securitymanager-clipboardpolicy-e.md) |
| [PasswordAlgs](arkts-mdm-securitymanager-passwordalgs-e.md) |
| [PermissionManagedState](arkts-mdm-securitymanager-permissionmanagedstate-e.md) |
