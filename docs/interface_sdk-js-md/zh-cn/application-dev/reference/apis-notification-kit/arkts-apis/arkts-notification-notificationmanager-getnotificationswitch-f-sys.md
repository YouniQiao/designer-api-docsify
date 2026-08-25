# getNotificationSwitch（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getNotificationSwitch

```TypeScript
function getNotificationSwitch(switchName: string, userId: number): Promise<SwitchState>
```

获取通知开关状态。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [switchName](arkts-notification-notificationsubscriber-notificationswitchchangedcallbackdata-i-sys.md) | string | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SwitchState](arkts-notification-notificationmanager-switchstate-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
