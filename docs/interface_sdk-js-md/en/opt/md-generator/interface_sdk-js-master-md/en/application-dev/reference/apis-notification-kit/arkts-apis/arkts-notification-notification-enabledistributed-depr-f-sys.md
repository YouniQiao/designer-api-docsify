# enableDistributed (System API)

## enableDistributed

```TypeScript
function enableDistributed(enable: boolean, callback: AsyncCallback<void>): void
```

Sets whether this device supports distributed notifications. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setDistributedEnable-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function enableDistributed(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-notification-function enableDistributed(enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## enableDistributed

```TypeScript
function enableDistributed(enable: boolean): Promise<void>
```

Sets whether this device supports distributed notifications. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setDistributedEnable](arkts-notification-notificationmanager-setdistributedenable-f-sys.md#setDistributedEnable-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function enableDistributed(enable: boolean): Promise<void>--><!--Device-notification-function enableDistributed(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
