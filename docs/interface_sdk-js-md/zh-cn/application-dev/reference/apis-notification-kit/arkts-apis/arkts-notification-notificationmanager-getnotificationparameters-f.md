# getNotificationParameters

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getNotificationParameters

```TypeScript
function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>
```

获取通知[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md)中wantAgent字段的部分信息。使用Promise异 步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| label | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;NotificationParameters & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |
