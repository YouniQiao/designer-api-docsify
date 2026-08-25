# @ohos.enterprise.adminManager(admin权限管理)

本模块为企业MDM应用提供admin权限管理能力，包括激活/解除激活admin权限、事件订阅、委托授权等。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [disableAdmin(admin权限管理)](arkts-mdm-adminmanager-disableadmin-f.md) |
| [disableDeviceAdmin(admin权限管理)](arkts-mdm-adminmanager-disabledeviceadmin-f.md) |
| [enableDeviceAdmin(admin权限管理)](arkts-mdm-adminmanager-enabledeviceadmin-f.md) |
| [enableSelfDeviceAdmin(admin权限管理)](arkts-mdm-adminmanager-enableselfdeviceadmin-f.md) |
| [getDelegatedBundleNames(admin权限管理)](arkts-mdm-adminmanager-getdelegatedbundlenames-f.md) |
| [getDelegatedPolicies(admin权限管理)](arkts-mdm-adminmanager-getdelegatedpolicies-f.md) |
| [isByodAdmin(admin权限管理)](arkts-mdm-adminmanager-isbyodadmin-f.md) |
| [setDelegatedPolicies(admin权限管理)](arkts-mdm-adminmanager-setdelegatedpolicies-f.md) |
| [startAdminProvision(admin权限管理)](arkts-mdm-adminmanager-startadminprovision-f.md) |
| [subscribeManagedEventSync(admin权限管理)](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) |
| [unsubscribeManagedEventSync(admin权限管理)](arkts-mdm-adminmanager-unsubscribemanagedeventsync-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [authorizeAdmin(admin权限管理)](arkts-mdm-adminmanager-authorizeadmin-f-sys.md) |
| [authorizeAdmin(admin权限管理)](arkts-mdm-adminmanager-authorizeadmin-f-sys.md) |
| [disableAdmin(admin权限管理)](arkts-mdm-adminmanager-disableadmin-f-sys.md) |
| [disableAdmin(admin权限管理)](arkts-mdm-adminmanager-disableadmin-f-sys.md) |
| [disableSuperAdmin(admin权限管理)](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md) |
| [disableSuperAdmin(admin权限管理)](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md) |
| [enableAdmin(admin权限管理)](arkts-mdm-adminmanager-enableadmin-f-sys.md) |
| [enableAdmin(admin权限管理)](arkts-mdm-adminmanager-enableadmin-f-sys.md) |
| [enableAdmin(admin权限管理)](arkts-mdm-adminmanager-enableadmin-f-sys.md) |
| [getAdmins(admin权限管理)](arkts-mdm-adminmanager-getadmins-f-sys.md) |
| [getEnterpriseInfo(admin权限管理)](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md) |
| [getEnterpriseInfo(admin权限管理)](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md) |
| [getEnterpriseManagedTips(admin权限管理)](arkts-mdm-adminmanager-getenterprisemanagedtips-f-sys.md) |
| [getSuperAdmin(admin权限管理)](arkts-mdm-adminmanager-getsuperadmin-f-sys.md) |
| [isAdminEnabled(admin权限管理)](arkts-mdm-adminmanager-isadminenabled-f-sys.md) |
| [isAdminEnabled(admin权限管理)](arkts-mdm-adminmanager-isadminenabled-f-sys.md) |
| [isAdminEnabled(admin权限管理)](arkts-mdm-adminmanager-isadminenabled-f-sys.md) |
| [isSuperAdmin(admin权限管理)](arkts-mdm-adminmanager-issuperadmin-f-sys.md) |
| [isSuperAdmin(admin权限管理)](arkts-mdm-adminmanager-issuperadmin-f-sys.md) |
| [replaceSuperAdmin(admin权限管理)](arkts-mdm-adminmanager-replacesuperadmin-f-sys.md) |
| [setAdminRunningMode(admin权限管理)](arkts-mdm-adminmanager-setadminrunningmode-f-sys.md) |
| [setDelegatedPolicies(admin权限管理)](arkts-mdm-adminmanager-setdelegatedpolicies-f-sys.md) |
| [setEnterpriseInfo(admin权限管理)](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md) |
| [setEnterpriseInfo(admin权限管理)](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md) |
| [subscribeManagedEvent(admin权限管理)](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md) |
| [subscribeManagedEvent(admin权限管理)](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md) |
| [unsubscribeManagedEvent(admin权限管理)](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md) |
| [unsubscribeManagedEvent(admin权限管理)](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [EnterpriseInfo(admin权限管理)](arkts-mdm-adminmanager-enterpriseinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AdminType(admin权限管理)](arkts-mdm-adminmanager-admintype-e.md) |
| [ManagedEvent(admin权限管理)](arkts-mdm-adminmanager-managedevent-e.md) |
| [Policy(admin权限管理)](arkts-mdm-adminmanager-policy-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AdminType(admin权限管理)](arkts-mdm-adminmanager-admintype-e-sys.md) |
| [RunningMode(admin权限管理)](arkts-mdm-adminmanager-runningmode-e-sys.md) |
<!--DelEnd-->
