# removeSlot

## 导入模块

```TypeScript
```

## removeSlot

```TypeScript
function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void
```

删除当前应用指定类型的通知渠道。使用callback异步回调。 删除后，对应类型的通知渠道及其配置将被永久移除，后续发布该类型通知时系统将自动创建默认渠道。 已通过该渠道发布的通知不受影响，仍可在通知中心查看。 适用于需要重新配置渠道时先删除再创建的场景。

**起始版本：** 23

<!--Device-notificationManager-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

getSlot 获取指定类型的通知渠道。

removeAllSlots 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// removeSlot回调
let removeSlotCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in removing slot.`);
  }
}
let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.removeSlot(slotType, removeSlotCallback);
```


## removeSlot

```TypeScript
function removeSlot(slotType: SlotType): Promise<void>
```

删除当前应用指定类型的通知渠道。使用Promise异步回调。 删除后，对应类型的通知渠道及其配置将被永久移除，后续发布该类型通知时系统将自动创建默认渠道。 已通过该渠道发布的通知不受影响，仍可在通知中心查看。 适用于需要重新配置渠道时先删除再创建的场景。

**起始版本：** 23

<!--Device-notificationManager-function removeSlot(slotType: SlotType): Promise<void>--><!--Device-notificationManager-function removeSlot(slotType: SlotType): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

getSlot 获取指定类型的通知渠道。

removeAllSlots 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let slotType: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
notificationManager.removeSlot(slotType).then(() => {
  console.info(`Succeeded in removing slot.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove slot. Code is ${err.code}, message is ${err.message}`);
});
```
