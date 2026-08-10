# getDeviceRemindType (System API)

## getDeviceRemindType

```TypeScript
function getDeviceRemindType(callback: AsyncCallback<DeviceRemindType>): void
```

获取通知的提醒方式（Callback形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getDeviceRemindType

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDeviceRemindType(callback: AsyncCallback<DeviceRemindType>): void--><!--Device-notification-function getDeviceRemindType(callback: AsyncCallback<DeviceRemindType>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DeviceRemindType&gt; | Yes | 获取通知提醒方式的回调函数。 |


## getDeviceRemindType

```TypeScript
function getDeviceRemindType(): Promise<DeviceRemindType>
```

获取通知的提醒方式（Promise形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getDeviceRemindType

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDeviceRemindType(): Promise<DeviceRemindType>--><!--Device-notification-function getDeviceRemindType(): Promise<DeviceRemindType>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DeviceRemindType&gt; | Promise方式返回获取通知提醒方式的结果。 |

