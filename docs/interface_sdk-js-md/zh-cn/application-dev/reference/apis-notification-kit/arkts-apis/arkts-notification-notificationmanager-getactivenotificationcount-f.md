# getActiveNotificationCount

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(callback: AsyncCallback<number>): void
```

获取当前应用的通知数量。使用callback异步回调。用于查询当前应用在通知中心中已发布的存量通知数量。适用于需要展示未读通知数量提示的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

setBadgeNumber 设置角标个数。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |


## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(): Promise<number>
```

获取当前应用的通知数量。使用Promise异步回调。用于查询当前应用在通知中心中已发布的存量通知数量。适用于需要展示未读通知数量提示的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

setBadgeNumber 设置角标个数。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
