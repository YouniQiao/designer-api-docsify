# removeAllSlots

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## removeAllSlots

```TypeScript
function removeAllSlots(callback: AsyncCallback<void>): void
```

删除当前应用所有通知渠道。使用callback异步回调。删除后，当前应用的所有通知渠道及其配置将被永久移除，后续发布通知时系统将自动创建对应类型的渠道。 已通过这些渠道发布的通知不受影响，仍可在通知中心查看。 适用于需要一次性清除所有渠道配置的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

getSlot 获取指定类型的通知渠道。

removeSlot 删除所有通知渠道。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |


## removeAllSlots

```TypeScript
function removeAllSlots(): Promise<void>
```

删除当前应用所有通知渠道。使用Promise异步回调。删除后，当前应用的所有通知渠道及其配置将被永久移除，后续发布通知时系统将自动创建对应类型的渠道。 已通过这些渠道发布的通知不受影响，仍可在通知中心查看。 适用于需要一次性清除所有渠道配置的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

addSlot 创建通知频道。

getSlot 获取指定类型的通知渠道。

removeSlot 删除指定类型的通知渠道。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
