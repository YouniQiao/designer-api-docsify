# supportDoNotDisturbMode (System API)

## supportDoNotDisturbMode

```TypeScript
function supportDoNotDisturbMode(callback: AsyncCallback<boolean>): void
```

查询是否支持免打扰功能（Callback形式）。

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
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 查询是否支持免打扰功能回调函数。 |


## supportDoNotDisturbMode

```TypeScript
function supportDoNotDisturbMode(): Promise<boolean>
```

查询是否支持免打扰功能（Promise形式）。

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
| Promise&lt;boolean&gt; | 以Promise形式返回获取是否支持免打扰功能的结果。 |

