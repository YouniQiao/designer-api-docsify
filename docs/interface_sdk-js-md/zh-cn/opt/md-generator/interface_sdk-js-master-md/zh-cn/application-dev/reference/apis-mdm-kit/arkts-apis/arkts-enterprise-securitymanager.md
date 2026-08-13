# @ohos.enterprise.securityManager(安全管理)

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


**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace securityManager--><!--Device-unnamed-declare namespace securityManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [getDeviceEncryptionStatus](arkts-mdm-securitymanager-getdeviceencryptionstatus-f-sys.md#getDeviceEncryptionStatus（系统接口）) |
| [getPasswordPolicy](arkts-mdm-securitymanager-getpasswordpolicy-f-sys.md#getPasswordPolicy（系统接口）) |
| [getSecurityPatchTag](arkts-mdm-securitymanager-getsecuritypatchtag-f-sys.md#getSecurityPatchTag（系统接口）) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [ApplicationInstance](arkts-mdm-securitymanager-applicationinstance-i.md) |
| [CertBlob](arkts-mdm-securitymanager-certblob-i.md) |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |
| [WatermarkProperties](arkts-mdm-securitymanager-watermarkproperties-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DeviceEncryptionStatus](arkts-mdm-securitymanager-deviceencryptionstatus-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ClipboardPolicy](arkts-mdm-securitymanager-clipboardpolicy-e.md) |
| [PasswordAlgs](arkts-mdm-securitymanager-passwordalgs-e.md) |
| [PermissionManagedState](arkts-mdm-securitymanager-permissionmanagedstate-e.md) |
