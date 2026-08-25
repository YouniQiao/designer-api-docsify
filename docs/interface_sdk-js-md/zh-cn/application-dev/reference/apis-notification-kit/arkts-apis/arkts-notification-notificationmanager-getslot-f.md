# getSlot

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getSlot

```TypeScript
function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void
```

获取指定类型的通知渠道。使用callback异步回调。用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。 需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

removeSlot 删除指定类型的通知渠道。

removeAllSlots 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NotificationSlot&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |


## getSlot

```TypeScript
function getSlot(slotType: SlotType): Promise<NotificationSlot>
```

获取指定类型的通知渠道。使用Promise异步回调。用于查询已创建的通知渠道的详细配置信息，包括提醒方式、级别、锁屏显示等设置。 需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

removeSlot 删除指定类型的通知渠道。

removeAllSlots 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotType | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;NotificationSlot & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
