# getSlot

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getSlot

```TypeScript
function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void
```

Obtains a notification slot of a specified type. This API uses an asynchronous callback to return the result.

This API is used to query the detailed configuration information of a created notification slot,including settings such as reminder method, level, and lock screen display. A corresponding type of notification slot must be created first through addSlot, otherwise the obtained result will be empty.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void--><!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[addSlot](notificationManager.addSlot(slotType: SlotType,callback: AsyncCallback<void>): void) adds a notification

[removeSlot](notificationManager.removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void) removes a notification slot of

[removeAllSlots](notificationManager.removeAllSlots(callback: AsyncCallback): void) removes all notification slots

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | SlotType | Yes | Notification slot type, such as social communication, service reminder, and content consultation. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;NotificationSlot&gt; | Yes | Callback used to return the result. If the notification slot is obtained successfully, **err** is **undefined** and **data** is the obtained **NotificationSlot**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// getSlot callback
let getSlotCallback = (err: BusinessError, data: notificationManager.NotificationSlot): void => {
  if (err) {
    console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
  }
}
let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.getSlot(slotType, getSlotCallback);
```


## getSlot

```TypeScript
function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot|null>): void
```

Obtains a notification slot of a specified type. This API uses an asynchronous callback to return the result.

This API is used to query the detailed configuration information of a created notification slot,including settings such as reminder method, level, and lock screen display. A corresponding type of notification slot must be created first through addSlot, otherwise the obtained result will be empty.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot|null>): void--><!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot|null>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[addSlot](notificationManager.addSlot(slotType: SlotType,callback: AsyncCallback<void>): void) adds a notification

[removeSlot](notificationManager.removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void) removes a notification slot of

[removeAllSlots](notificationManager.removeAllSlots(callback: AsyncCallback): void) removes all notification slots

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | SlotType | Yes | Notification slot type, such as social communication, service reminder, and content consultation. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;NotificationSlot \| null&gt; | Yes | Callback used to return the result. If the notification slot is obtained successfully, **err** is **undefined** and **data** is the obtained **NotificationSlot**; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |


## getSlot

```TypeScript
function getSlot(slotType: SlotType): Promise<NotificationSlot>
```

Obtains a notification slot of a specified type. This API uses a promise to return the result.

This API is used to query the detailed configuration information of a created notification slot,including settings such as reminder method, level, and lock screen display. A corresponding type of notification slot must be created first through addSlot, otherwise the obtained result will be empty.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot>--><!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[addSlot](notificationManager.addSlot(slotType: SlotType): Promise<void>) adds a notification slot of a specified type.

[removeSlot](notificationManager.removeSlot(slotType: SlotType): Promise<void>) removes a notification

[removeAllSlots](notificationManager.removeAllSlots(): Promise<void>) removes all

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | SlotType | Yes | Notification slot type, such as social communication, service reminder, and content consultation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationSlot&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.getSlot(slotType).then((data: notificationManager.NotificationSlot) => {
  console.info(`Succeeded in getting slot, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get slot. Code is ${err.code}, message is ${err.message}`);
});
```


## getSlot

```TypeScript
function getSlot(slotType: SlotType): Promise<NotificationSlot|null>
```

Obtains a notification slot of a specified type. This API uses a promise to return the result.

This API is used to query the detailed configuration information of a created notification slot,including settings such as reminder method, level, and lock screen display. A corresponding type of notification slot must be created first through addSlot, otherwise the obtained result will be empty.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot|null>--><!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot|null>-End-->

**System capability:** SystemCapability.Notification.Notification

**See also:**

[addSlot](notificationManager.addSlot(slotType: SlotType): Promise<void>) adds a notification slot of

[removeSlot](notificationManager.removeSlot(slotType: SlotType): Promise<void>) removes a notification slot of a

[removeAllSlots](notificationManager.removeAllSlots(): Promise<void>) removes all notification slots for

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | SlotType | Yes | Notification slot type, such as social communication, service reminder, and content consultation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationSlot \| null&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |

