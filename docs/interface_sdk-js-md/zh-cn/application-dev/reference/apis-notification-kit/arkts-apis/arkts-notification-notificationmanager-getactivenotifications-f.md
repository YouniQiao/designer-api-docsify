# getActiveNotifications

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getActiveNotifications

```TypeScript
function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void
```

获取当前应用未删除的通知列表。使用callback异步回调。用于查询当前应用在通知中心中所有存量通知的详细信息列表，包括每条通知的ID、标签、内容、创建时间等。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

setBadgeNumber 设置角标个数。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;NotificationRequest&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |


## getActiveNotifications

```TypeScript
function getActiveNotifications(): Promise<Array<NotificationRequest>>
```

获取当前应用未删除的通知列表。使用Promise异步回调。用于查询当前应用在通知中心中所有存量通知的详细信息列表，包括每条通知的ID、标签、内容、创建时间等。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

setBadgeNumber 设置角标个数。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;NotificationRequest & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
