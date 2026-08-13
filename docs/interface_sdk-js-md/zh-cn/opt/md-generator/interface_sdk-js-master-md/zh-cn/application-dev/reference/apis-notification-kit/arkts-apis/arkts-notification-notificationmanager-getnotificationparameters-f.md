# getNotificationParameters

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getNotificationParameters

```TypeScript
function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>
```

获取通知[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md#NotificationRequest)中wantAgent字段的部分信息。使用Promise异 步回调。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-notificationManager-function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>--><!--Device-notificationManager-function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>-End-->

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

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id: number = 0;
let label: string = '';
notificationManager.getNotificationParameters(id, label).then((data: notificationManager.NotificationParameters) => {
  console.info(`Succeeded in getting notification parameters, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get notification parameters. Code is ${err.code}, message is ${err.message}`);
});
```


## getNotificationParameters

```TypeScript
function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters | null>
```

获取通知[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md#NotificationRequest)中wantAgent字段的部分信息。使用Promise异 步回调。

**起始版本：** 24

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-notificationManager-function getNotificationParameters(id: int, label?: string): Promise<NotificationParameters | null>--><!--Device-notificationManager-function getNotificationParameters(id: int, label?: string): Promise<NotificationParameters | null>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| label | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;NotificationParameters \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |
