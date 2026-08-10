# getDoNotDisturbDate (System API)

## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void
```

查询免打扰时间（Callback形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void--><!--Device-notification-function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DoNotDisturbDate&gt; | Yes | 查询免打扰时间回调函数。 |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(): Promise<DoNotDisturbDate>
```

查询免打扰时间（Promise形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(): Promise<DoNotDisturbDate>--><!--Device-notification-function getDoNotDisturbDate(): Promise<DoNotDisturbDate>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DoNotDisturbDate&gt; | 以Promise形式返回查询到的免打扰时间。 |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void
```

查询指定用户的免打扰时间（Callback形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void--><!--Device-notification-function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | 用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DoNotDisturbDate&gt; | Yes | 查询免打扰时间回调函数。 |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>
```

查询指定用户的免打扰时间（Promise形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>--><!--Device-notification-function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | 用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DoNotDisturbDate&gt; | 以Promise形式返回查询到的免打扰时间。 |

