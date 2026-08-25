# @ohos.enterprise.adminManager(Administrator Permission Management)

The **adminManager** module provides administrator permission management capabilities for enterprise MDM applications, including enabling or disabling administrator permissions, subscribing to events, delegating applications, and granting permissions.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [disableAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-disableadmin-f.md) |
| [disableDeviceAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-disabledeviceadmin-f.md) |
| [enableDeviceAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-enabledeviceadmin-f.md) |
| [enableSelfDeviceAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-enableselfdeviceadmin-f.md) |
| [getDelegatedBundleNames(Administrator Permission Management)](arkts-mdm-adminmanager-getdelegatedbundlenames-f.md) |
| [getDelegatedPolicies(Administrator Permission Management)](arkts-mdm-adminmanager-getdelegatedpolicies-f.md) |
| [isByodAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-isbyodadmin-f.md) |
| [setDelegatedPolicies(Administrator Permission Management)](arkts-mdm-adminmanager-setdelegatedpolicies-f.md) |
| [startAdminProvision(Administrator Permission Management)](arkts-mdm-adminmanager-startadminprovision-f.md) |
| [subscribeManagedEventSync(Administrator Permission Management)](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) |
| [unsubscribeManagedEventSync(Administrator Permission Management)](arkts-mdm-adminmanager-unsubscribemanagedeventsync-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [authorizeAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-authorizeadmin-f-sys.md) |
| [authorizeAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-authorizeadmin-f-sys.md) |
| [disableAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-disableadmin-f-sys.md) |
| [disableAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-disableadmin-f-sys.md) |
| [disableSuperAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md) |
| [disableSuperAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md) |
| [enableAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-enableadmin-f-sys.md) |
| [enableAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-enableadmin-f-sys.md) |
| [enableAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-enableadmin-f-sys.md) |
| [getAdmins(Administrator Permission Management)](arkts-mdm-adminmanager-getadmins-f-sys.md) |
| [getEnterpriseInfo(Administrator Permission Management)](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md) |
| [getEnterpriseInfo(Administrator Permission Management)](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md) |
| [getEnterpriseManagedTips(Administrator Permission Management)](arkts-mdm-adminmanager-getenterprisemanagedtips-f-sys.md) |
| [getSuperAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-getsuperadmin-f-sys.md) |
| [isAdminEnabled(Administrator Permission Management)](arkts-mdm-adminmanager-isadminenabled-f-sys.md) |
| [isAdminEnabled(Administrator Permission Management)](arkts-mdm-adminmanager-isadminenabled-f-sys.md) |
| [isAdminEnabled(Administrator Permission Management)](arkts-mdm-adminmanager-isadminenabled-f-sys.md) |
| [isSuperAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-issuperadmin-f-sys.md) |
| [isSuperAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-issuperadmin-f-sys.md) |
| [replaceSuperAdmin(Administrator Permission Management)](arkts-mdm-adminmanager-replacesuperadmin-f-sys.md) |
| [setAdminRunningMode(Administrator Permission Management)](arkts-mdm-adminmanager-setadminrunningmode-f-sys.md) |
| [setDelegatedPolicies(Administrator Permission Management)](arkts-mdm-adminmanager-setdelegatedpolicies-f-sys.md) |
| [setEnterpriseInfo(Administrator Permission Management)](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md) |
| [setEnterpriseInfo(Administrator Permission Management)](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md) |
| [subscribeManagedEvent(Administrator Permission Management)](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md) |
| [subscribeManagedEvent(Administrator Permission Management)](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md) |
| [unsubscribeManagedEvent(Administrator Permission Management)](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md) |
| [unsubscribeManagedEvent(Administrator Permission Management)](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EnterpriseInfo(Administrator Permission Management)](arkts-mdm-adminmanager-enterpriseinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdminType(Administrator Permission Management)](arkts-mdm-adminmanager-admintype-e.md) |
| [ManagedEvent(Administrator Permission Management)](arkts-mdm-adminmanager-managedevent-e.md) |
| [Policy(Administrator Permission Management)](arkts-mdm-adminmanager-policy-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AdminType(Administrator Permission Management)](arkts-mdm-adminmanager-admintype-e-sys.md) |
| [RunningMode(Administrator Permission Management)](arkts-mdm-adminmanager-runningmode-e-sys.md) |
<!--DelEnd-->
