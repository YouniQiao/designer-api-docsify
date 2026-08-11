# @ohos.enterprise.securityManager(安全管理)

本模块提供企业设备安全管理能力，支持证书管理、设备安全策略管理、口令策略管理、剪贴板策略管理、水印策略管理、权限管理等功能。企业可使用本模块实现设备安全状态的实时监控、企业证书的生命周期管理、设备口令策略的统一配置、应用剪贴板使用行为的管控、屏幕和应用水印的设置以防止信息泄露、以及应用权限的精细化管理等场景，帮助企业提升设备安全防护能力，降低数据泄露风险。

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace securityManager--><!--Device-unnamed-declare namespace securityManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
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

### 接口

| 名称 |
| --- |
| [ApplicationInstance](arkts-mdm-securitymanager-applicationinstance-i.md) |
| [CertBlob](arkts-mdm-securitymanager-certblob-i.md) |
| [DeviceEncryptionStatus](arkts-mdm-securitymanager-deviceencryptionstatus-i.md) |
| [PasswordPolicy](arkts-mdm-securitymanager-passwordpolicy-i.md) |
| [WatermarkProperties](arkts-mdm-securitymanager-watermarkproperties-i.md) |

### 枚举

| 名称 |
| --- |
| [ClipboardPolicy](arkts-mdm-securitymanager-clipboardpolicy-e.md) |
| [PasswordAlgs](arkts-mdm-securitymanager-passwordalgs-e.md) |
| [PermissionManagedState](arkts-mdm-securitymanager-permissionmanagedstate-e.md) |
