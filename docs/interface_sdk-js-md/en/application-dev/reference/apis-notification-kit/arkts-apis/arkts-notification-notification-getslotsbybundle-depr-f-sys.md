# getSlotsByBundle (System API)

## getSlotsByBundle

```TypeScript
function getSlotsByBundle(bundle: BundleOption, callback: AsyncCallback<Array<NotificationSlot>>): void
```

Obtains the notification slots of a specified application.This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [getSlotsByBundle](ohos.notificationManager/notificationManager#getSlotsByBundle)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getSlotsByBundle(bundle: BundleOption, callback: AsyncCallback<Array<NotificationSlot>>): void--><!--Device-notification-function getSlotsByBundle(bundle: BundleOption, callback: AsyncCallback<Array<NotificationSlot>>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt;&gt; | Yes | Callback used to return the result. |


## getSlotsByBundle

```TypeScript
function getSlotsByBundle(bundle: BundleOption): Promise<Array<NotificationSlot>>
```

Obtains the notification slots of a specified application. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [getSlotsByBundle](ohos.notificationManager/notificationManager#getSlotsByBundle)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getSlotsByBundle(bundle: BundleOption): Promise<Array<NotificationSlot>>--><!--Device-notification-function getSlotsByBundle(bundle: BundleOption): Promise<Array<NotificationSlot>>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt;&gt; | Promise used to return the result. |

