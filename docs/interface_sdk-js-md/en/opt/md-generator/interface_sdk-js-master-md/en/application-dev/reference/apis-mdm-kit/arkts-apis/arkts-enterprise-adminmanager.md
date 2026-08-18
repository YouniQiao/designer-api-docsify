# @ohos.enterprise.adminManager

The **adminManager** module provides administrator permission management capabilities for enterprise MDM applications, including enabling or disabling administrator permissions, subscribing to events, delegating applications, and granting permissions. > **NOTE：**> > The APIs of this module can be called only by a device administrator application. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 23

<!--Device-unnamed-declare namespace adminManager--><!--Device-unnamed-declare namespace adminManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeadmin-system-api) |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeadmin-system-api) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableadmin-system-api) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableadmin-system-api) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disablesuperadmin-system-api) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disablesuperadmin-system-api) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableadmin-system-api) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableadmin-system-api) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableadmin-system-api) |
| [getAdmins](arkts-mdm-adminmanager-getadmins-f-sys.md#getadmins-system-api) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getenterpriseinfo-system-api) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getenterpriseinfo-system-api) |
| [getEnterpriseManagedTips](arkts-mdm-adminmanager-getenterprisemanagedtips-f-sys.md#getenterprisemanagedtips-system-api) |
| [getSuperAdmin](arkts-mdm-adminmanager-getsuperadmin-f-sys.md#getsuperadmin-system-api) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isadminenabled-system-api) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isadminenabled-system-api) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isadminenabled-system-api) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#issuperadmin-system-api) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#issuperadmin-system-api) |
| [replaceSuperAdmin](arkts-mdm-adminmanager-replacesuperadmin-f-sys.md#replacesuperadmin-system-api) |
| [setAdminRunningMode](arkts-mdm-adminmanager-setadminrunningmode-f-sys.md#setadminrunningmode-system-api) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f-sys.md#setdelegatedpolicies-system-api) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setenterpriseinfo-system-api) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setenterpriseinfo-system-api) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribemanagedevent-system-api) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribemanagedevent-system-api) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribemanagedevent-system-api) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribemanagedevent-system-api) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdminType](arkts-mdm-adminmanager-admintype-e.md) |
| [ManagedEvent](arkts-mdm-adminmanager-managedevent-e.md) |
| [Policy](arkts-mdm-adminmanager-policy-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdminType](arkts-mdm-adminmanager-admintype-e-sys.md) |
| [RunningMode](arkts-mdm-adminmanager-runningmode-e-sys.md) |
<!--DelEnd-->
