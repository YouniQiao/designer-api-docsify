# getNotificationSetting

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getNotificationSetting

```TypeScript
function getNotificationSetting(): Promise<NotificationSetting>
```

获取应用的通知设置，包括锁屏通知、横幅通知、桌面角标、振动、铃声等 开关状态。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Notification.Notification

**参见：**

openNotificationSettings 拉起

isNotificationEnabled 获取指定应用的通知使能状态。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[NotificationSetting](arkts-notification-notificationmanager-notificationsetting-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
