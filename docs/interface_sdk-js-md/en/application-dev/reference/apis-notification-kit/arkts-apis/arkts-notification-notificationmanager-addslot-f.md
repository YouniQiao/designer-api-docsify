# addSlot

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## addSlot

```TypeScript
function addSlot(type: SlotType, callback: AsyncCallback<void>): void
```

创建指定类型的通知渠道。使用callback异步回调。

通知渠道NotificationSlot定义了通知的提醒方式（如提示音、振动、横幅等）和级别。发布通知前，应用需先创建对应类型的通知渠道，或者发布通知时系统将自动创建对应类型的通知渠道。同一类型的通知渠道只能创建一个。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-notificationManager-function addSlot(type: SlotType, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function addSlot(type: SlotType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes | 要创建的通知渠道的类型。不同的渠道类型对应不同的默认SlotLevel， 影响通知的提醒方式。例如SOCIAL_COMMUNICATION对应LEVEL_HIGH （状态栏图标+横幅+提示音），CONTENT_INFORMATION对应LEVEL_MIN （状态栏不显示图标+无横幅+无提示音）。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当创建指定类型的通知渠道成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600012 | No memory space. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// addSlot callback
let addSlotCallBack = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in adding slot.`);
  }
}
notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION, addSlotCallBack);
```


## addSlot

```TypeScript
function addSlot(type: SlotType): Promise<void>
```

创建指定类型的通知渠道。使用Promise异步回调。

通知渠道NotificationSlot定义了通知的提醒方式（如提示音、振动、横幅等）和级别。发布通知前，应用需先创建对应类型的通知渠道，或者发布通知时系统将自动创建对应类型的通知渠道。同一类型的通知渠道只能创建一个。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-notificationManager-function addSlot(type: SlotType): Promise<void>--><!--Device-notificationManager-function addSlot(type: SlotType): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | Yes | 要创建的通知渠道的类型。不同的渠道类型对应不同的默认SlotLevel， 影响通知的提醒方式。例如SOCIAL_COMMUNICATION对应LEVEL_HIGH （状态栏图标+横幅+提示音），CONTENT_INFORMATION对应LEVEL_MIN （状态栏不显示图标+无横幅+无提示音）。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600012 | No memory space. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION).then(() => {
  console.info(`Succeeded in adding slot.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
});
```

