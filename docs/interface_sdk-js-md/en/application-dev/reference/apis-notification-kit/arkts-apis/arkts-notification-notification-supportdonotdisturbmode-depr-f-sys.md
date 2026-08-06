# supportDoNotDisturbMode (System API)

## supportDoNotDisturbMode

```TypeScript
function supportDoNotDisturbMode(callback: AsyncCallback<boolean>): void
```

Checks whether DND mode is supported. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#isSupportDoNotDisturbMode

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function supportDoNotDisturbMode(callback: AsyncCallback<boolean>): void--><!--Device-notification-function supportDoNotDisturbMode(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;boolean&gt; | Yes | Callback used to return the result. |


## supportDoNotDisturbMode

```TypeScript
function supportDoNotDisturbMode(): Promise<boolean>
```

Checks whether DND mode is supported. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#isSupportDoNotDisturbMode

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function supportDoNotDisturbMode(): Promise<boolean>--><!--Device-notification-function supportDoNotDisturbMode(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. |

