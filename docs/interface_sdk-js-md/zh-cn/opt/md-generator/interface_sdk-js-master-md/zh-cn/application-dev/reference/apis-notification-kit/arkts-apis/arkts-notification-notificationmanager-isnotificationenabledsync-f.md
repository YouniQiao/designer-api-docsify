# isNotificationEnabledSync

## 导入模块

```TypeScript
```

## isNotificationEnabledSync

```TypeScript
function isNotificationEnabledSync(): boolean
```

同步查询当前应用通知授权状态。 用于在发布通知前快速检查当前应用是否被允许发送通知。此接口为同步接口， 调用后立即返回结果，适用于需要在同步代码流程中获取使能状态的场景。

**起始版本：** 23

<!--Device-notificationManager-function isNotificationEnabledSync(): boolean--><!--Device-notificationManager-function isNotificationEnabledSync(): boolean-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

requestEnableNotification 请求通知使能。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

**示例**

```TypeScript
let enabled: boolean = notificationManager.isNotificationEnabledSync();
console.info(`isNotificationEnabledSync success, data is : ${JSON.stringify(enabled)}`);
```
