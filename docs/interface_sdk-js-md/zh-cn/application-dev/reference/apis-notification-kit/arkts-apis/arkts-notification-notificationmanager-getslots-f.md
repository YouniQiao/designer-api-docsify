# getSlots

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getSlots

```TypeScript
function getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void
```

获取当前应用的所有通知渠道。使用callback异步回调。用于批量查询当前应用已创建的所有通知渠道的配置信息，包括各渠道的类型、提醒方式、级别等设置。 适用于需要查看所有渠道配置的场景。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

removeSlot 删除指定类型的通知渠道。

removeAllSlots 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;NotificationSlot&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |


## getSlots

```TypeScript
function getSlots(): Promise<Array<NotificationSlot>>
```

获取当前应用的所有通知渠道。使用Promise异步回调。用于批量查询当前应用已创建的所有通知渠道的配置信息，包括各渠道的类型、提醒方式、级别等设置。 适用于需要查看所有渠道配置的场景。需先通过addSlot创建对应类型的通知渠道，否则获取结果为空。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

removeSlot 删除指定类型的通知渠道。

removeAllSlots 删除所有通知渠道。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;NotificationSlot & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
