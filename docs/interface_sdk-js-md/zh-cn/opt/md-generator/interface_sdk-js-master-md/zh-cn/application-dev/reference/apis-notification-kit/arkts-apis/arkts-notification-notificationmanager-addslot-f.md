# addSlot

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## addSlot

```TypeScript
function addSlot(type: SlotType, callback: AsyncCallback<void>): void
```

创建指定类型的通知渠道。使用callback异步回调。 通知渠道NotificationSlot定义了通知的提醒方式（如提示音、振动、横幅等）和级别。 发布通知前，应用需先创建对应类型的通知渠道，或者发布通知时系统将自动创建对应类型的通知渠道。 同一类型的通知渠道只能创建一个。

**起始版本：** 23

**废弃版本：** -1

<!--Device-notificationManager-function addSlot(type: SlotType, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function addSlot(type: SlotType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

getSlot 获取指定类型的通知渠道。

removeSlot 删除当前应用指定类型的通知渠道。

removeAllSlots 删除所有渠道通知。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// addSlot回调
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

创建指定类型的通知渠道。使用Promise异步回调。 通知渠道NotificationSlot定义了通知的提醒方式（如提示音、振动、横幅等）和级别。 发布通知前，应用需先创建对应类型的通知渠道，或者发布通知时系统将自动创建对应类型的通知渠道。 同一类型的通知渠道只能创建一个。

**起始版本：** 23

**废弃版本：** -1

<!--Device-notificationManager-function addSlot(type: SlotType): Promise<void>--><!--Device-notificationManager-function addSlot(type: SlotType): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

getSlot 获取指定类型的通知渠道。

removeSlot 删除当前应用指定类型的通知渠道。

removeAllSlots 删除当前应用的所有渠道通知。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.addSlot(notificationManager.SlotType.SOCIAL_COMMUNICATION).then(() => {
  console.info(`Succeeded in adding slot.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to add slot. Code is ${err.code}, message is ${err.message}`);
});
```
