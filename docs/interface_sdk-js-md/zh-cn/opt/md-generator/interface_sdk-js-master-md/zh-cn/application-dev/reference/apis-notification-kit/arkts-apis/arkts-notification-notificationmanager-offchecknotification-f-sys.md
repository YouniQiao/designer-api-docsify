# offCheckNotification（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## offCheckNotification

```TypeScript
function offCheckNotification(
    callback?: (checkInfo: NotificationCheckInfo) => NotificationCheckResult
  ): void
```

通知监听回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function offCheckNotification(    callback?: (checkInfo: NotificationCheckInfo) => NotificationCheckResult  ): void--><!--Device-notificationManager-function offCheckNotification(    callback?: (checkInfo: NotificationCheckInfo) => NotificationCheckResult  ): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (checkInfo: NotificationCheckInfo) = & gt; NotificationCheckResult | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
