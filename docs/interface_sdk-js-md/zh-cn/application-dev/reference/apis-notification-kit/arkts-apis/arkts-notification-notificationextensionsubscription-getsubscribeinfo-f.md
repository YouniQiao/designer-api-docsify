# getSubscribeInfo

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## getSubscribeInfo

```TypeScript
function getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>
```

获取当前应用的通知扩展订阅信息。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.SUBSCRIBE_NOTIFICATION

**系统能力：** SystemCapability.Notification.Notification

**参见：**

subscribe 订阅通知扩展。

**返回值：**

| 类型 |
| --- |
| Promise & lt;NotificationExtensionSubscriptionInfo[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
