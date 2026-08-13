# @ohos.enterprise.adminManager

The **adminManager** module provides administrator permission management capabilities for enterprise MDM applications, including enabling or disabling administrator permissions, subscribing to events, delegating applications, and granting permissions. > **NOTE：**> > The APIs of this module can be called only by a device administrator application. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace adminManager--><!--Device-unnamed-declare namespace adminManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeAdmin-(System-API)) |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f-sys.md#authorizeAdmin-(System-API)) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableAdmin-(System-API)) |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f-sys.md#disableAdmin-(System-API)) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disableSuperAdmin-(System-API)) |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f-sys.md#disableSuperAdmin-(System-API)) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableAdmin-(System-API)) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableAdmin-(System-API)) |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f-sys.md#enableAdmin-(System-API)) |
| [getAdmins](arkts-mdm-adminmanager-getadmins-f-sys.md#getAdmins-(System-API)) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getEnterpriseInfo-(System-API)) |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f-sys.md#getEnterpriseInfo-(System-API)) |
| [getEnterpriseManagedTips](arkts-mdm-adminmanager-getenterprisemanagedtips-f-sys.md#getEnterpriseManagedTips-(System-API)) |
| [getSuperAdmin](arkts-mdm-adminmanager-getsuperadmin-f-sys.md#getSuperAdmin-(System-API)) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isAdminEnabled-(System-API)) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isAdminEnabled-(System-API)) |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f-sys.md#isAdminEnabled-(System-API)) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#isSuperAdmin-(System-API)) |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f-sys.md#isSuperAdmin-(System-API)) |
| [replaceSuperAdmin](arkts-mdm-adminmanager-replacesuperadmin-f-sys.md#replaceSuperAdmin-(System-API)) |
| [setAdminRunningMode](arkts-mdm-adminmanager-setadminrunningmode-f-sys.md#setAdminRunningMode-(System-API)) |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f-sys.md#setDelegatedPolicies-(System-API)) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setEnterpriseInfo-(System-API)) |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f-sys.md#setEnterpriseInfo-(System-API)) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribeManagedEvent-(System-API)) |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f-sys.md#subscribeManagedEvent-(System-API)) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribeManagedEvent-(System-API)) |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f-sys.md#unsubscribeManagedEvent-(System-API)) |
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
