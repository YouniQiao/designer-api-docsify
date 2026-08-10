# getSlot

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getSlot

```TypeScript
function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void
```

获取指定类型的通知渠道。使用callback异步回调。

用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void--><!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes | 通知渠道类型，例如社交通讯、服务提醒、内容咨询等类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NotificationSlot&gt; | Yes | 回调函数。当获取通知渠道成功， err为undefined，data为获取到的NotificationSlot，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

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

获取指定类型的通知渠道。使用callback异步回调。

用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot|null>): void--><!--Device-notificationManager-function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot|null>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes | 通知渠道类型，例如社交通讯、服务提醒、内容咨询等类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NotificationSlot \| null&gt; | Yes | 回调函数。当获取通知渠道成功， err为undefined，data为获取到的NotificationSlot，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |


## getSlot

```TypeScript
function getSlot(slotType: SlotType): Promise<NotificationSlot>
```

获取指定类型的通知渠道。使用Promise异步回调。

用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot>--><!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes | 通知渠道类型，例如社交通讯、服务提醒、内容咨询等类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationSlot&gt; | Promise对象，返回通知渠道对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

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

获取指定类型的通知渠道。使用Promise异步回调。

用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot|null>--><!--Device-notificationManager-function getSlot(slotType: SlotType): Promise<NotificationSlot|null>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes | 通知渠道类型，例如社交通讯、服务提醒、内容咨询等类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationSlot \| null&gt; | Promise对象，返回通知渠道对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

