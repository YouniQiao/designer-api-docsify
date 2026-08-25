# EnterpriseAdminExtensionAbility

This module provides the [enterprise device management extension ability](../../../mdm/mdm-kit-term.md#enterpriseadminextensionability) and is the core component of the enterprise device administrator application.  
**Main functions**:  
- Provides lifecycle management capabilities for device administrator applications (enabling, disabling, startup, and  
so on).  
- Provides application lifecycle event listening capabilities (installation, uninstallation, startup, stop, update).  
- Provides system account management event listening capabilities (account addition, switch, removal).  
- Provides system-level event callbacks for Kiosk mode, key events, log collection, and system updates.  
- Provides policy change event listening capabilities.  
**Use cases:** Enterprise device administrator application development, enterprise application lifecycle management, device security control, account management, and device O&M monitoring.To have the capabilities provided by this module, for example, to receive a notification when a device administrator application is enabled or disabled, you need to create an **EnterpriseAdminExtensionAbility** instance for the device administrator application and overload related APIs.

**Since:** 12

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { EnterpriseAdminExtensionAbility } from 'kits/@kit.MDMKit';
```

## onAccountAdded

```TypeScript
onAccountAdded(accountId: number): void
```

Called when a system account is added. You should register the **MANAGED_EVENT_ACCOUNT_ADDED** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to system account add events. When a system account is added to an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | number | Yes |

## onAccountRemoved

```TypeScript
onAccountRemoved(accountId: number): void
```

Called when the system account is removed. You should register the **MANAGED_EVENT_ACCOUNT_REMOVED** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to system account removal events. When a system account is removed, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | number | Yes |

## onAccountSwitched

```TypeScript
onAccountSwitched(accountId: number): void
```

Called when the system account is switched. You should register the **MANAGED_EVENT_ACCOUNT_SWITCHED** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to system account switch events. When a system account is switched, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | number | Yes |

## onAdminDisabled

```TypeScript
onAdminDisabled(): void
```

Called when the device administrator application is disabled. After an enterprise administrator or employee disables the device administrator application, the system notifies the application that the admin permission has been revoked. The device administrator application can use this callback to notify the enterprise administrator that the device is no longer under management. No registration is required. This callback is triggered by default after the device administrator application is disabled.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## onAdminEnabled

```TypeScript
onAdminEnabled(): void
```

Called when the device administrator application is enabled. After an enterprise administrator or employee deploys and enables the device administrator application, the system notifies the device administrator application that the admin permission has been granted. The device administrator application can initialize policies within this callback. No registration is required. This callback is triggered by default after the device administrator application is enabled.Differences from onDeviceAdminEnabled:  
- **onAdminEnabled**: Triggered when the device administrator application itself is enabled, and used for the  
device administrator application to initialize its own policies.  
- **onDeviceAdminEnabled**: Triggered when a super device administrator application listens for the enabling of a  
normal device administrator application, and used for the super device administrator application to manage normal device administrator applications.You should choose the appropriate method based on the application type and listening scenario: normal device administrator applications should use **onAdminEnabled**, while super device administrator applications listening for the enabling of other applications should use **onDeviceAdminEnabled**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## onAdminPolicyChanged

```TypeScript
onAdminPolicyChanged(event: common.PolicyChangedEvent): void
```

Defines the policy change event. The super device administrator application can receive this callback after registering the MANAGED_EVENT_POLICIES_CHANGED event via [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). In the enterprise device management scenario, when any MDM application calls an API in [Policy Change Reporting List](../../../mdm/mdm-kit-appendix.md#policy-change-reporting-list), the system notifies the super device administrator application of the current user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | common.PolicyChangedEvent | Yes |

## onAppStart

```TypeScript
onAppStart(bundleName: string): void
```

Called when an application is started. You should register the **MANAGED_EVENT_APP_START** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to application start events. When an application is started on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

## onAppStop

```TypeScript
onAppStop(bundleName: string): void
```

Called when an application is stopped. You should register the **MANAGED_EVENT_APP_STOP** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to application stop events. When an application is stopped on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

## onBundleAdded

```TypeScript
onBundleAdded(bundleName: string): void
```

Called when applications are installed. The application bundle name is included. You should register the **MANAGED_EVENT_BUNDLE_ADDED** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to application installation events. When an application is installed on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

## onBundleAdded

```TypeScript
onBundleAdded(bundleName: string, accountId: number): void
```

Called when applications are installed. The application bundle name and account ID are included. You should register the **MANAGED_EVENT_BUNDLE_ADDED** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to application installation events. When an application is installed on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |

## onBundleRemoved

```TypeScript
onBundleRemoved(bundleName: string): void
```

Called when applications are uninstalled. The application bundle name is included. You should register the **MANAGED_EVENT_BUNDLE_REMOVED** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to application uninstallation events. When an application is uninstalled from an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

## onBundleRemoved

```TypeScript
onBundleRemoved(bundleName: string, accountId: number): void
```

Called when applications are uninstalled. The application bundle name and account ID are included. You should register the **MANAGED_EVENT_BUNDLE_REMOVED** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to application uninstallation events. When an application is uninstalled from an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |

## onBundleUpdated

```TypeScript
onBundleUpdated(bundleName: string, accountId: number): void
```

Callback for application update events. The callback contains the application package name and user ID. You can receive this callback only after you register the **MANAGED_EVENT_BUNDLE_UPDATED** event through the [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) API. In enterprise device management scenarios, the device administrator application can subscribe to application update events of all users. When an application update event is triggered, the device administrator application of the current user is notified. Then the device administrator application can report the event in this callback function to notify the enterprise administrator under the main user.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |

## onDeviceAdminDisabled

```TypeScript
onDeviceAdminDisabled(bundleName: string): void
```

Called only for the super device administrator application when the device administrator application is disabled. After an enterprise administrator or employee disables the device administrator application, the system notifies the super device administrator application that the admin permission has been revoked. The super device administrator application can use this callback to notify the enterprise administrator that the device is no longer under management. No registration is required. This callback is triggered by default after the device administrator application is disabled.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

## onDeviceAdminEnabled

```TypeScript
onDeviceAdminEnabled(bundleName: string): void
```

Called only for the super device administrator application when the device administrator application is enabled. After an enterprise administrator or employee deploys and enables the device administrator application, the system notifies the super device administrator application that the admin permission has been granted. The super device administrator application can initialize policies within this callback. No registration is required. This callback is triggered by default after the device administrator application is enabled.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

## onDeviceBootCompleted

```TypeScript
onDeviceBootCompleted(): void
```

Callback for the device startup completion event. You can receive this callback only after you register the **MANAGED_EVENT_BOOT_COMPLETED** event through the [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) API. The enterprise administrator application can subscribe to device startup completion events. When an enterprise device has finished starting up, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## onKeyEvent

```TypeScript
onKeyEvent(keyEvent: systemManager.KeyEvent): void
```

Defines the [key event](arkts-mdm-systemmanager-keyevent-i.md) callback. The MDM application needs to deliver key event handling policies via the [systemManager.addKeyEventPolicies](arkts-mdm-systemmanager-addkeyeventpolicies-f.md) API. When a system key event is triggered, if the event matches the delivered policy, this callback will be invoked. The callback parameter [keyEvent](arkts-mdm-systemmanager-keyevent-i.md) contains information about currently triggered key events, which are introduced below.Single-key event. When a single key on the device is triggered, the [onKeyEvent](#onkeyevent) callback will be invoked twice (once on key press and once on key release). You can determine whether the key is pressed or released based on the **keyAction** property in [keyEvent](arkts-mdm-systemmanager-keyevent-i.md). The **keyItems** property in [keyEvent](arkts-mdm-systemmanager-keyevent-i.md) can be ignored for single-key events.Combined-key event. Only the power button, volume up button, and volume down button can be combined. When a user presses a key combination, the callback for the subsequently pressed key will carry information about all currently pressed keys via the **keyItems** property in [keyEvent](arkts-mdm-systemmanager-keyevent-i.md). All other response logic is consistent with that of single-key events.Long-press event. When a single key or key combination is pressed for an extended period, the [onKeyEvent](#onkeyevent) callback will be triggered continuously at an interval of 50 ms (the actual interval may be slightly longer depending on system status and performance). For each callback event, the **actionTime** property in [keyEvent](arkts-mdm-systemmanager-keyevent-i.md) remains the same as the **actionTime** property in the [keyEvent](arkts-mdm-systemmanager-keyevent-i.md) of the initial key press callback. All other response logic is consistent with that of single-key and combined key events.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [keyEvent](../../apis-input-kit/arkts-apis/arkts-input-inputeventclient-keyeventdata-i-sys.md) | systemManager.KeyEvent | Yes |

## onKioskModeEntering

```TypeScript
onKioskModeEntering(bundleName: string, accountId: number): void
```

Called when an application enters the kiosk mode. This callback contains the application bundle name and account ID.Kiosk mode is a system-level runtime mode that restricts a device to a single application or a set of applications. It controls the lock screen, status bar, gestures, and key features to prevent users from launching other applications or performing other operations on the device.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |

## onKioskModeExiting

```TypeScript
onKioskModeExiting(bundleName: string, accountId: number): void
```

Called when an application exits the kiosk mode. This callback contains the application bundle name and account ID.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| accountId | number | Yes |

## onLogCollected

```TypeScript
onLogCollected(result: common.Result): void
```

Callback triggered upon completion of log collection, after a log collection task is successfully created via the [systemManager.startCollectLog](arkts-mdm-systemmanager-startcollectlog-f.md) API. It contains the log collection result.

> **NOTE：**&gt;
> When log collection succeeds, the app must access the sandbox directory (**\/data/edm/log**) in its
> **EnterpriseAdminExtensionAbility** to retrieve the logs. For details about how to obtain logs, see the following
> sample code. After the app obtains the logs, you are advised to call
> [systemManager.finishLogCollected](arkts-mdm-systemmanager-finishlogcollected-f.md) to
> remove the collected logs.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | common.Result | Yes |

## onMarketAppInstallResult

```TypeScript
onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void
```

Called when an application is installed via the [bundleManager.installMarketApps](arkts-mdm-bundlemanager-installmarketapps-f.md) API. This callback contains the application bundle name and installation result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| result | common.InstallationResult | Yes |

## onStart

```TypeScript
onStart(): void
```

Called when EnterpriseAdminExtensionAbility starts.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## onStartupGuideCompleted

```TypeScript
onStartupGuideCompleted(scene: common.StartupScene): void
```

Callback for the startup wizard completion event. You can receive this callback only after you register the **MANAGED_EVENT_STARTUP_GUIDE_COMPLETED** event through the [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md) API. The device administrator application can subscribe to startup wizard completion events. When the initial switch to a sub-user (only on PCs), OTA upgrade, and first-time startup wizard are complete on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scene | common.StartupScene | Yes |

## onSystemUpdate

```TypeScript
onSystemUpdate(systemUpdateInfo: systemManager.SystemUpdateInfo): void
```

Called to report a system update event. You should register the **MANAGED_EVENT_SYSTEM_UPDATE** event through [adminManager.subscribeManagedEventSync](arkts-mdm-adminmanager-subscribemanagedeventsync-f.md). The enterprise administrator application can subscribe to application update events. When an application is updated on an enterprise device, the device administrator application reports the event in this callback to notify the enterprise administrator.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| systemUpdateInfo | systemManager.SystemUpdateInfo | Yes |

## context

```TypeScript
context: EnterpriseAdminExtensionContext
```

Context of **EnterpriseAdminExtensionAbility**. It inherits from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md).

**Type:** [EnterpriseAdminExtensionContext](arkts-mdm-enterpriseadminextensioncontext-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager
