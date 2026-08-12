# @ohos.enterprise.adminManager(Administrator Permission Management)

The **adminManager** module provides administrator permission management capabilities for enterprise MDM applications, including enabling or disabling administrator permissions, subscribing to events, delegating applications, and granting permissions.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace adminManager--><!--Device-unnamed-declare namespace adminManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f.md#authorizeadmin) | Authorizes the administrator permission to a specified application. This API uses an asynchronous callback to return the result. |
| [authorizeAdmin](arkts-mdm-adminmanager-authorizeadmin-f.md#authorizeadmin-1) | Authorizes the administrator permission to a specified application. This API uses a promise to return the result. |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableadmin) | Disables a common device administrator application for the current user. This API uses an asynchronous callback to return the result. |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableadmin-1) | Disables a common device administrator application for the user specified by **userId**. This API uses an asynchronous callback to return the result. |
| [disableAdmin](arkts-mdm-adminmanager-disableadmin-f.md#disableadmin-2) | Disables a device administrator application for the specified user. This API uses a promise to return the result.After this API is called successfully, the specified device administrator application will be deactivated and no longer have the device management capability. |
| [disableDeviceAdmin](arkts-mdm-adminmanager-disabledeviceadmin-f.md#disabledeviceadmin) | Disables a [DA](../../../mdm/mdm-kit-term.md#device-admin-da) application by a  [SDA](../../../mdm/mdm-kit-term.md#super-device-admin-sda) application. This API uses a promise to return the result. After this API is called successfully, the specified device administrator application is disabled and no longer has the device management capability. This API can be called only by super device administrator applications. |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f.md#disablesuperadmin) | Disables a super device administrator application based on **bundleName**. This API uses an asynchronous callback to return the result. |
| [disableSuperAdmin](arkts-mdm-adminmanager-disablesuperadmin-f.md#disablesuperadmin-1) | Disables a super device administrator application based on **bundleName**. This API uses a promise to return the result. |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f.md#enableadmin) | Enables a device administrator application. The super device administrator application can be enabled only for the first user (u100). After the application is enabled, it cannot be uninstalled. Its  [EnterpriseAdminExtensionAbility](../../../mdm/mdm-kit-term.md#enterpriseadminextensionability) component will automatically start upon device startup and user switching. This API uses an asynchronous callback to return the result. |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f.md#enableadmin-1) | Enables a device administrator application for a user (specified by **userId**). The super device administrator application can be enabled only for the first user (u100). This API uses an asynchronous callback to return the result. |
| [enableAdmin](arkts-mdm-adminmanager-enableadmin-f.md#enableadmin-2) | Enables the device administrator application for the current or specified user. The super device administrator application can be enabled only for the first user (u100). This API uses a promise to return the result. |
| [enableDeviceAdmin](arkts-mdm-adminmanager-enabledeviceadmin-f.md#enabledeviceadmin) | Enables a [DA](../../../mdm/mdm-kit-term.md#device-admin-da) application by a  [SDA](../../../mdm/mdm-kit-term.md#super-device-admin-sda) application. This API uses a promise to return the result. After the API is successfully called, the specified DA application is enabled and granted device management capabilities. This API can be called only by super device administrator applications. |
| [enableSelfDeviceAdmin](arkts-mdm-adminmanager-enableselfdeviceadmin-f.md#enableselfdeviceadmin) | Allows an MDM application to enable itself in scenarios where it is not pre-enabled on the enterprise device. This API supports enablement of the MDM application itself only, and cannot be used to enable other MDM applications.The supported enablement types include super device administrator application and normal device administrator application. |
| [getAdmins](arkts-mdm-adminmanager-getadmins-f.md#getadmins) | Queries all device administrator applications of the current user. This API uses a promise to return the result. |
| [getDelegatedBundleNames](arkts-mdm-adminmanager-getdelegatedbundlenames-f.md#getdelegatedbundlenames) | Queries the delegated applications that can access a delegation policy and output the list of delegated applications. |
| [getDelegatedPolicies](arkts-mdm-adminmanager-getdelegatedpolicies-f.md#getdelegatedpolicies) | Queries the list of policies that can be accessed by the delegated application. |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f.md#getenterpriseinfo) | Obtains the enterprise information of the device administrator application. This API uses an asynchronous callback to return the result. |
| [getEnterpriseInfo](arkts-mdm-adminmanager-getenterpriseinfo-f.md#getenterpriseinfo-1) | Obtains the enterprise information of the device administrator application. This API uses a promise to return the result. |
| [getEnterpriseManagedTips](arkts-mdm-adminmanager-getenterprisemanagedtips-f.md#getenterprisemanagedtips) | Gets enterprise message tips. |
| [getSuperAdmin](arkts-mdm-adminmanager-getsuperadmin-f.md#getsuperadmin) | Queries the super device administrator application of this first user (u100). This API uses a promise to return the result. |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f.md#isadminenabled) | Checks whether a device administrator application of the current user is enabled. This API uses an asynchronous callback to return the result. |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f.md#isadminenabled-1) | Checks whether a device administrator application of the specified user is enabled. This API uses an asynchronous callback to return the result. |
| [isAdminEnabled](arkts-mdm-adminmanager-isadminenabled-f.md#isadminenabled-2) | Checks whether a device administrator application of the current or specified user is enabled. This API uses a promise to return the result. |
| [isByodAdmin](arkts-mdm-adminmanager-isbyodadmin-f.md#isbyodadmin) | Checks whether the current application is activated as a BYOD device administrator application based on the  **EnterpriseAdminExtensionAbility** component. |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f.md#issuperadmin) | Checks whether the super device administrator application of the first user (u100) is enabled based on  **bundleName**. This API uses an asynchronous callback to return the result. |
| [isSuperAdmin](arkts-mdm-adminmanager-issuperadmin-f.md#issuperadmin-1) | Checks whether the super device administrator application of the first user (u100) is enabled based on  **bundleName**. This API uses a promise to return the result. |
| [replaceSuperAdmin](arkts-mdm-adminmanager-replacesuperadmin-f.md#replacesuperadmin) | Replaces a specified application with a super device administrator application. |
| [setAdminRunningMode](arkts-mdm-adminmanager-setadminrunningmode-f.md#setadminrunningmode) | Sets the running mode of the device administrator application. |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f.md#setdelegatedpolicies) | Delegates other applications to set device management policies. The applications must request the permissions required. |
| [setDelegatedPolicies](arkts-mdm-adminmanager-setdelegatedpolicies-f.md#setdelegatedpolicies-1) | Delegates other applications to set device management policies. The applications must request the permissions required. |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f.md#setenterpriseinfo) | Sets the enterprise information of the device administrator application. This API uses an asynchronous callback to return the result. |
| [setEnterpriseInfo](arkts-mdm-adminmanager-setenterpriseinfo-f.md#setenterpriseinfo-1) | Sets the enterprise information of the device administrator application. This API uses a promise to return the result. |
| [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startadminprovision) | Enables the device administrator application to open a page for the BYOD administrator to perform activation. |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f.md#subscribemanagedevent) | Subscribes to system management events. This API uses an asynchronous callback to return the result. |
| [subscribeManagedEvent](arkts-mdm-adminmanager-subscribemanagedevent-f.md#subscribemanagedevent-1) | Subscribes to system management events. This API uses a promise to return the result. |
| [subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md#subscribemanagedeventsync) | Subscribes to system management events. After the call is successful, the device administrator application will receive a notification when a subscribed system management event occurs.  Since API version 26.0.0, error code 9200002 is returned when a non-super device administrator application calls this API to subscribe to the [MANAGED_EVENT_POLICIES_CHANGED](arkts-mdm-adminmanager-managedevent-e.md#ManagedEvent) event. |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f.md#unsubscribemanagedevent) | Unsubscribes from system management events. This API uses an asynchronous callback to return the result. |
| [unsubscribeManagedEvent](arkts-mdm-adminmanager-unsubscribemanagedevent-f.md#unsubscribemanagedevent-1) | Unsubscribes from system management events. This API uses a promise to return the result. |
| [unsubscribeManagedEventSync](arkts-mdm-adminmanager-unsubscribemanagedeventsync-f.md#unsubscribemanagedeventsync) | Unsubscribes from system management events. After the API is successfully called, no notifications for the unsubscribed system management events will be received. |

### Interfaces

| Name | Description |
| --- | --- |
| [EnterpriseInfo](arkts-mdm-adminmanager-enterpriseinfo-i.md) | Represents the enterprise information of a device administrator application. |

### Enums

| Name | Description |
| --- | --- |
| [AdminType](arkts-mdm-adminmanager-admintype-e.md) | Enumerates the types of device administrator applications. |
| [ManagedEvent](arkts-mdm-adminmanager-managedevent-e.md) | Enumerates the system management events that can be subscribed to. |
| [Policy](arkts-mdm-adminmanager-policy-e.md) | Defines the policy type for the trustlist or blocklist. |
| [RunningMode](arkts-mdm-adminmanager-runningmode-e.md) | Represents the running mode of a device administrator application. |

