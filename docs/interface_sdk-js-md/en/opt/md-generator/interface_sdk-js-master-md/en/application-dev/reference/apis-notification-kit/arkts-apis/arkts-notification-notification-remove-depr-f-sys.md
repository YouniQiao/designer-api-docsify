# remove (System API)

## remove

```TypeScript
function remove(
    bundle: BundleOption,
    notificationKey: NotificationKey,
    reason: RemoveReason,
    callback: AsyncCallback<void>
  ): void
```

Removes a notification for a specified bundle. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md#remove-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function remove(    bundle: BundleOption,    notificationKey: NotificationKey,    reason: RemoveReason,    callback: AsyncCallback<void>  ): void--><!--Device-notification-function remove(    bundle: BundleOption,    notificationKey: NotificationKey,    reason: RemoveReason,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |
| [notificationKey](arkts-notification-notificationrequest-notificationfilter-i-sys.md) | [NotificationKey](arkts-notification-notificationsubscribe-notificationkey-i-sys.md) | Yes |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## remove

```TypeScript
function remove(bundle: BundleOption, notificationKey: NotificationKey, reason: RemoveReason): Promise<void>
```

Removes a notification for a specified bundle. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md#remove-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function remove(bundle: BundleOption, notificationKey: NotificationKey, reason: RemoveReason): Promise<void>--><!--Device-notification-function remove(bundle: BundleOption, notificationKey: NotificationKey, reason: RemoveReason): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |
| [notificationKey](arkts-notification-notificationrequest-notificationfilter-i-sys.md) | [NotificationKey](arkts-notification-notificationsubscribe-notificationkey-i-sys.md) | Yes |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |


## remove

```TypeScript
function remove(hashCode: string, reason: RemoveReason, callback: AsyncCallback<void>): void
```

Removes a notification for a specified bundle. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md#remove-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function remove(hashCode: string, reason: RemoveReason, callback: AsyncCallback<void>): void--><!--Device-notification-function remove(hashCode: string, reason: RemoveReason, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hashCode | string | Yes |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## remove

```TypeScript
function remove(hashCode: string, reason: RemoveReason): Promise<void>
```

Removes a notification for a specified bundle. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md#remove-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function remove(hashCode: string, reason: RemoveReason): Promise<void>--><!--Device-notification-function remove(hashCode: string, reason: RemoveReason): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hashCode | string | Yes |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
