# openSubscriptionSettings

## Modules to Import

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## openSubscriptionSettings

```TypeScript
function openSubscriptionSettings(context: UIAbilityContext): Promise<void>
```

Opens the settings screen of notification extension subscription in a semi-modal dialog box. On this screen, the user can toggle on the **Allow access to notifications on this device** switch and grant access to notifications for specified applications. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.SUBSCRIBE_NOTIFICATION

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600018](../errorcode-notification.md#1600018-notification-settings-page-already-displayed) |
| [1600023](../errorcode-notification.md#1600023-notificationsubscriberextensionability-not-implemented) |
