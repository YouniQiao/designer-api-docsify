# @ohos.enterprise.adminManager(Administrator Permission Management)

The **adminManager** module provides administrator permission management capabilities for enterprise MDM applications, including enabling or disabling administrator permissions, subscribing to events, delegating applications, and granting permissions.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

<!--Device-unnamed-declare namespace adminManager--><!--Device-unnamed-declare namespace adminManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdminType](arkts-mdm-adminmanager-admintype-e.md) |
| [ManagedEvent](arkts-mdm-adminmanager-managedevent-e.md) |
| [Policy](arkts-mdm-adminmanager-policy-e.md) |
| [RunningMode](arkts-mdm-adminmanager-runningmode-e.md) |
