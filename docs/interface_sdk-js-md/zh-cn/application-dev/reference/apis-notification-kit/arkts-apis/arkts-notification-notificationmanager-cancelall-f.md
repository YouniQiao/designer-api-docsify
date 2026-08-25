# cancelAll

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## cancelAll

```TypeScript
function cancelAll(callback: AsyncCallback<void>): void
```

取消当前应用所有已发布的通知。使用callback异步回调。取消后，当前应用的所有通知将从通知中心、状态栏等位置移除，用户不再可见。 适用于应用退出或用户手动清除全部通知的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

publish 发布通知。

cancel 取消已发布的通知。

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


## cancelAll

```TypeScript
function cancelAll(): Promise<void>
```

取消当前应用所有已发布的通知。使用Promise异步回调。取消后，当前应用的所有通知将从通知中心、状态栏等位置移除，用户不再可见。 适用于应用退出或用户手动清除全部通知的场景。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.Notification

**参见：**

publish 发布通知。

cancel 根据指定的通知ID取消已发布的通知。

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
