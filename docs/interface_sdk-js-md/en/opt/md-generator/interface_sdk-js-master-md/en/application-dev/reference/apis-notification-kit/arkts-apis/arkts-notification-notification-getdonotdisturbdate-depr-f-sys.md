# getDoNotDisturbDate (System API)

## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void
```

Obtains the DND time. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDoNotDisturbDate](ohos.notificationManager/notificationManager#getDoNotDisturbDate)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void--><!--Device-notification-function getDoNotDisturbDate(callback: AsyncCallback<DoNotDisturbDate>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DoNotDisturbDate&gt; | Yes |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(): Promise<DoNotDisturbDate>
```

Obtains the DND time. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDoNotDisturbDate](ohos.notificationManager/notificationManager#getDoNotDisturbDate)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(): Promise<DoNotDisturbDate>--><!--Device-notification-function getDoNotDisturbDate(): Promise<DoNotDisturbDate>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DoNotDisturbDate & gt; |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void
```

Obtains the DND time of a specified user. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDoNotDisturbDate](ohos.notificationManager/notificationManager#getDoNotDisturbDate)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void--><!--Device-notification-function getDoNotDisturbDate(userId: number, callback: AsyncCallback<DoNotDisturbDate>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DoNotDisturbDate&gt; | Yes |


## getDoNotDisturbDate

```TypeScript
function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>
```

Obtains the DND time of a specified user. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getDoNotDisturbDate](ohos.notificationManager/notificationManager#getDoNotDisturbDate)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>--><!--Device-notification-function getDoNotDisturbDate(userId: number): Promise<DoNotDisturbDate>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DoNotDisturbDate & gt; |
