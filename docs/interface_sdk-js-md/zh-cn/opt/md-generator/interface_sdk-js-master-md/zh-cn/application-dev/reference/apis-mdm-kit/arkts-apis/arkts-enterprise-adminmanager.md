# @ohos.enterprise.adminManager(admin权限管理)

本模块为企业MDM应用提供admin权限管理能力，包括激活/解除激活admin权限、事件订阅、委托授权等。

> **说明：**
> 
> 本模块接口仅对设备管理应用开放，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

<!--Device-unnamed-declare namespace adminManager--><!--Device-unnamed-declare namespace adminManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 汇总

### 函数

| 名称 |
| --- |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f.md#authorizeadmin) |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f.md#authorizeadmin-1) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableadmin) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableadmin-1) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableadmin-2) |
| [disableDeviceAdmin](arkts-mdm-adminmanager-disabledeviceadmin-f.md#disabledeviceadmin) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f.md#disablesuperadmin) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f.md#disablesuperadmin-1) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f.md#enableadmin) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f.md#enableadmin-1) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f.md#enableadmin-2) |
| [enableDeviceAdmin](arkts-mdm-adminmanager-enabledeviceadmin-f.md#enabledeviceadmin) |
| [enableSelfDeviceAdmin](arkts-mdm-adminmanager-enableselfdeviceadmin-f.md#enableselfdeviceadmin) |
| [getAdmins](arkts-mdm-adminmanager-getadmins-f.md#getadmins) |
| [getDelegatedBundleNames](arkts-mdm-adminmanager-getdelegatedbundlenames-f.md#getdelegatedbundlenames) |
| [getDelegatedPolicies](arkts-mdm-adminmanager-getdelegatedpolicies-f.md#getdelegatedpolicies) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f.md#getenterpriseinfo) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f.md#getenterpriseinfo-1) |
| [getEnterpriseManagedTips](arkts-mdm-adminmanager-getenterprisemanagedtips-f.md#getenterprisemanagedtips) |
| [getSuperAdmin](arkts-mdm-adminmanager-getsuperadmin-f.md#getsuperadmin) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f.md#isadminenabled) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f.md#isadminenabled-1) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f.md#isadminenabled-2) |
| [isByodAdmin](arkts-mdm-adminmanager-isbyodadmin-f.md#isbyodadmin) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f.md#issuperadmin) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f.md#issuperadmin-1) |
| [replaceSuperAdmin](arkts-mdm-adminmanager-replacesuperadmin-f.md#replacesuperadmin) |
| [setAdminRunningMode](arkts-mdm-adminmanager-setadminrunningmode-f.md#setadminrunningmode) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f.md#setdelegatedpolicies) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f.md#setdelegatedpolicies-1) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f.md#setenterpriseinfo) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f.md#setenterpriseinfo-1) |
| [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startadminprovision) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f.md#subscribemanagedevent) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f.md#subscribemanagedevent-1) |
| [subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md#subscribemanagedeventsync) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f.md#unsubscribemanagedevent) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f.md#unsubscribemanagedevent-1) |
| [unsubscribeManagedEventSync](arkts-mdm-adminmanager-unsubscribemanagedeventsync-f.md#unsubscribemanagedeventsync) |

### 接口

| 名称 |
| --- |
| [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [AdminType](arkts-mdm-adminmanager-admintype-e.md) |
| [ManagedEvent](arkts-mdm-adminmanager-managedevent-e.md) |
| [Policy](arkts-mdm-adminmanager-policy-e.md) |
| [RunningMode](arkts-mdm-adminmanager-runningmode-e.md) |
