# @ohos.enterprise.securityManager(安全管理)

本模块提供企业设备安全管理能力，支持证书管理、设备安全策略管理、口令策略管理、剪贴板策略管理、水印策略管理、权限管理等功能。企业可使用本模块实现设备安全状态的实时监控、企业证书的生命周期管理、设备口令策略的统一配置、应用剪贴板使用行为 的管控、屏幕和应用水印的设置以防止信息泄露、以及应用权限的精细化管理等场景，帮助企业提升设备安全防护能力，降低数据泄露风险。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addAllowedPermissionBundle(安全管理)](arkts-mdm-securitymanager-addallowedpermissionbundle-f.md) |
| [cancelScreenWatermarkImage(安全管理)](arkts-mdm-securitymanager-cancelscreenwatermarkimage-f.md) |
| [cancelWatermarkImage(安全管理)](arkts-mdm-securitymanager-cancelwatermarkimage-f.md) |
| [getAllowedPermissionBundles(安全管理)](arkts-mdm-securitymanager-getallowedpermissionbundles-f.md) |
| [getAppClipboardPolicy(安全管理)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getAppClipboardPolicy(安全管理)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getAppClipboardPolicy(安全管理)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getAppClipboardPolicy(安全管理)](arkts-mdm-securitymanager-getappclipboardpolicy-f.md) |
| [getDisallowedPermissions(安全管理)](arkts-mdm-securitymanager-getdisallowedpermissions-f.md) |
| [getExternalSourceExtensionsPolicy(安全管理)](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md) |
| [getExternalSourceExtensionsPolicy(安全管理)](arkts-mdm-securitymanager-getexternalsourceextensionspolicy-f.md) |
| [getPasswordPolicy(安全管理)](arkts-mdm-securitymanager-getpasswordpolicy-f.md) |
| [getPasswordPolicy(安全管理)](arkts-mdm-securitymanager-getpasswordpolicy-f.md) |
| [getPermissionManagedState(安全管理)](arkts-mdm-securitymanager-getpermissionmanagedstate-f.md) |
| [getSecurityStatus(安全管理)](arkts-mdm-securitymanager-getsecuritystatus-f.md) |
| [getUserCertificates(安全管理)](arkts-mdm-securitymanager-getusercertificates-f.md) |
| [getWatermarkImageApps(安全管理)](arkts-mdm-securitymanager-getwatermarkimageapps-f.md) |
| [installEnterpriseReSignatureCertificate(安全管理)](arkts-mdm-securitymanager-installenterpriseresignaturecertificate-f.md) |
| [installUserCertificate(安全管理)](arkts-mdm-securitymanager-installusercertificate-f.md) |
| [installUserCertificate(安全管理)](arkts-mdm-securitymanager-installusercertificate-f.md) |
| [isScreenLockDisabledForAccount(安全管理)](arkts-mdm-securitymanager-isscreenlockdisabledforaccount-f.md) |
| [removeAllowedPermissionBundle(安全管理)](arkts-mdm-securitymanager-removeallowedpermissionbundle-f.md) |
| [setAppClipboardPolicy(安全管理)](arkts-mdm-securitymanager-setappclipboardpolicy-f.md) |
| [setAppClipboardPolicy(安全管理)](arkts-mdm-securitymanager-setappclipboardpolicy-f.md) |
| [setDisallowedPermission(安全管理)](arkts-mdm-securitymanager-setdisallowedpermission-f.md) |
| [setExternalSourceExtensionsPolicy(安全管理)](arkts-mdm-securitymanager-setexternalsourceextensionspolicy-f.md) |
| [setPasswordPolicy(安全管理)](arkts-mdm-securitymanager-setpasswordpolicy-f.md) |
| [setPermissionManagedState(安全管理)](arkts-mdm-securitymanager-setpermissionmanagedstate-f.md) |
| [setScreenLockDisabledForAccount(安全管理)](arkts-mdm-securitymanager-setscreenlockdisabledforaccount-f.md) |
| [setScreenWatermarkImage(安全管理)](arkts-mdm-securitymanager-setscreenwatermarkimage-f.md) |
| [setWatermarkImage(安全管理)](arkts-mdm-securitymanager-setwatermarkimage-f.md) |
| [setWatermarkImage(安全管理)](arkts-mdm-securitymanager-setwatermarkimage-f.md) |
| [uninstallEnterpriseReSignatureCertificate(安全管理)](arkts-mdm-securitymanager-uninstallenterpriseresignaturecertificate-f.md) |
| [uninstallUserCertificate(安全管理)](arkts-mdm-securitymanager-uninstallusercertificate-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getDeviceEncryptionStatus(安全管理)](arkts-mdm-securitymanager-getdeviceencryptionstatus-f-sys.md) |
| [getPasswordPolicy(安全管理)](arkts-mdm-securitymanager-getpasswordpolicy-f-sys.md) |
| [getSecurityPatchTag(安全管理)](arkts-mdm-securitymanager-getsecuritypatchtag-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [ApplicationInstance(安全管理)](arkts-mdm-securitymanager-applicationinstance-i.md) |
| [CertBlob(安全管理)](arkts-mdm-securitymanager-certblob-i.md) |
| [PasswordPolicy(安全管理)](arkts-mdm-securitymanager-passwordpolicy-i.md) |
| [WatermarkProperties(安全管理)](arkts-mdm-securitymanager-watermarkproperties-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DeviceEncryptionStatus(安全管理)](arkts-mdm-securitymanager-deviceencryptionstatus-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ClipboardPolicy(安全管理)](arkts-mdm-securitymanager-clipboardpolicy-e.md) |
| [PasswordAlgs(安全管理)](arkts-mdm-securitymanager-passwordalgs-e.md) |
| [PermissionManagedState(安全管理)](arkts-mdm-securitymanager-permissionmanagedstate-e.md) |
