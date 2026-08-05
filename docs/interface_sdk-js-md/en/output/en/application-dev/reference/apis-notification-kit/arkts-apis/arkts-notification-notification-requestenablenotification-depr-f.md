# requestEnableNotification

## requestEnableNotification

```TypeScript
function requestEnableNotification(callback: AsyncCallback<void>): void
```

Requests notification to be enabled for this application. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#requestEnableNotification

<!--Device-notification-function requestEnableNotification(callback: AsyncCallback<void>): void--><!--Device-notification-function requestEnableNotification(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |


## requestEnableNotification

```TypeScript
function requestEnableNotification(): Promise<void>
```

Requests notification to be enabled for this application. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#requestEnableNotification

<!--Device-notification-function requestEnableNotification(): Promise<void>--><!--Device-notification-function requestEnableNotification(): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

