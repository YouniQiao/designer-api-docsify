# @ohos.enterprise.adminManager

本模块为企业MDM应用提供admin权限管理能力，包括激活/解除激活admin权限、事件订阅、委托授权等。 > **说明：** > > 本模块接口仅对设备管理应用开放，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace adminManager--><!--Device-unnamed-declare namespace adminManager-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 汇总

### 函数

| 名称 |
| --- |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableAdmin) |
| [disableDeviceAdmin](arkts-mdm-adminmanager-disabledeviceadmin-f.md#disableDeviceAdmin) |
| [enableDeviceAdmin](arkts-mdm-adminmanager-enabledeviceadmin-f.md#enableDeviceAdmin) |
| [enableSelfDeviceAdmin](arkts-mdm-adminmanager-enableselfdeviceadmin-f.md#enableSelfDeviceAdmin) |
| [getDelegatedBundleNames](arkts-mdm-adminmanager-getdelegatedbundlenames-f.md#getDelegatedBundleNames) |
| [getDelegatedPolicies](arkts-mdm-adminmanager-getdelegatedpolicies-f.md#getDelegatedPolicies) |
| [isByodAdmin](arkts-mdm-adminmanager-isbyodadmin-f.md#isByodAdmin) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f.md#setDelegatedPolicies) |
| [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startAdminProvision) |
| [subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md#subscribeManagedEventSync) |
| [unsubscribeManagedEventSync](arkts-mdm-adminmanager-unsubscribemanagedeventsync-f.md#unsubscribeManagedEventSync) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeAdmin（系统接口）) |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeAdmin（系统接口）) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableAdmin（系统接口）) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableAdmin（系统接口）) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disableSuperAdmin（系统接口）) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disableSuperAdmin（系统接口）) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableAdmin（系统接口）) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableAdmin（系统接口）) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableAdmin（系统接口）) |
| [getAdmins](arkts-mdm-adminmanager-getadmins-f-sys.md#getAdmins（系统接口）) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getEnterpriseInfo（系统接口）) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getEnterpriseInfo（系统接口）) |
| [getEnterpriseManagedTips](arkts-mdm-adminmanager-getenterprisemanagedtips-f-sys.md#getEnterpriseManagedTips（系统接口）) |
| [getSuperAdmin](arkts-mdm-adminmanager-getsuperadmin-f-sys.md#getSuperAdmin（系统接口）) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isAdminEnabled（系统接口）) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isAdminEnabled（系统接口）) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isAdminEnabled（系统接口）) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#isSuperAdmin（系统接口）) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#isSuperAdmin（系统接口）) |
| [replaceSuperAdmin](arkts-mdm-adminmanager-replacesuperadmin-f-sys.md#replaceSuperAdmin（系统接口）) |
| [setAdminRunningMode](arkts-mdm-adminmanager-setadminrunningmode-f-sys.md#setAdminRunningMode（系统接口）) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f-sys.md#setDelegatedPolicies（系统接口）) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setEnterpriseInfo（系统接口）) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setEnterpriseInfo（系统接口）) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribeManagedEvent（系统接口）) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribeManagedEvent（系统接口）) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribeManagedEvent（系统接口）) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribeManagedEvent（系统接口）) |
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
