# isUserGranted

## 导入模块

```TypeScript
import { notificationExtensionSubscription } from 'kits/@kit.NotificationKit';
```

## isUserGranted

```TypeScript
function isUserGranted(): Promise<boolean>
```

查询“允许获取本机通知”的开关状态。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.SUBSCRIBE_NOTIFICATION

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
