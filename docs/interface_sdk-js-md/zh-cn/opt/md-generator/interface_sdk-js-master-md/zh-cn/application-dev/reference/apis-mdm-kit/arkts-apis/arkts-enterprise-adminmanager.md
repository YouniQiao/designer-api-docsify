# @ohos.enterprise.adminManager

本模块为企业MDM应用提供admin权限管理能力，包括激活/解除激活admin权限、事件订阅、委托授权等。 > **说明：** > > 本模块接口仅对设备管理应用开放，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 23

<!--Device-unnamed-declare namespace adminManager--><!--Device-unnamed-declare namespace adminManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableadmin) |
| [disableDeviceAdmin](arkts-mdm-adminmanager-disabledeviceadmin-f.md#disabledeviceadmin) |
| [enableDeviceAdmin](arkts-mdm-adminmanager-enabledeviceadmin-f.md#enabledeviceadmin) |
| [enableSelfDeviceAdmin](arkts-mdm-adminmanager-enableselfdeviceadmin-f.md#enableselfdeviceadmin) |
| [getDelegatedBundleNames](arkts-mdm-adminmanager-getdelegatedbundlenames-f.md#getdelegatedbundlenames) |
| [getDelegatedPolicies](arkts-mdm-adminmanager-getdelegatedpolicies-f.md#getdelegatedpolicies) |
| [isByodAdmin](arkts-mdm-adminmanager-isbyodadmin-f.md#isbyodadmin) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f.md#setdelegatedpolicies) |
| [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startadminprovision) |
| [subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md#subscribemanagedeventsync) |
| [unsubscribeManagedEventSync](arkts-mdm-adminmanager-unsubscribemanagedeventsync-f.md#unsubscribemanagedeventsync) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeadmin系统接口) |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeadmin系统接口) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableadmin系统接口) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableadmin系统接口) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disablesuperadmin系统接口) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disablesuperadmin系统接口) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableadmin系统接口) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableadmin系统接口) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableadmin系统接口) |
| [getAdmins](arkts-mdm-adminmanager-getadmins-f-sys.md#getadmins系统接口) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getenterpriseinfo系统接口) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getenterpriseinfo系统接口) |
| [getEnterpriseManagedTips](arkts-mdm-adminmanager-getenterprisemanagedtips-f-sys.md#getenterprisemanagedtips系统接口) |
| [getSuperAdmin](arkts-mdm-adminmanager-getsuperadmin-f-sys.md#getsuperadmin系统接口) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isadminenabled系统接口) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isadminenabled系统接口) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isadminenabled系统接口) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#issuperadmin系统接口) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#issuperadmin系统接口) |
| [replaceSuperAdmin](arkts-mdm-adminmanager-replacesuperadmin-f-sys.md#replacesuperadmin系统接口) |
| [setAdminRunningMode](arkts-mdm-adminmanager-setadminrunningmode-f-sys.md#setadminrunningmode系统接口) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f-sys.md#setdelegatedpolicies系统接口) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setenterpriseinfo系统接口) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setenterpriseinfo系统接口) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribemanagedevent系统接口) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribemanagedevent系统接口) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribemanagedevent系统接口) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribemanagedevent系统接口) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [AdminType](arkts-mdm-adminmanager-admintype-e.md) |
| [ManagedEvent](arkts-mdm-adminmanager-managedevent-e.md) |
| [Policy](arkts-mdm-adminmanager-policy-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AdminType](arkts-mdm-adminmanager-admintype-e-sys.md) |
| [RunningMode](arkts-mdm-adminmanager-runningmode-e-sys.md) |
<!--DelEnd-->
