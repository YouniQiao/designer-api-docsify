# snoozeNotification（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## snoozeNotification

```TypeScript
function snoozeNotification(hashCode: string, delayTime: number): Promise<void>
```

设置通知稍后提醒。该通知在指定时间后再次提醒，每次设置只会提醒一次，提醒方式与该通知相同。 设置后该通知被删除。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-notificationManager-function snoozeNotification(hashCode: string, delayTime: long): Promise<void>--><!--Device-notificationManager-function snoozeNotification(hashCode: string, delayTime: long): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hashCode | string | 是 |
| delayTime | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600028](../errorcode-notification.md#1600028-当前通知不支持该接口) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 此处应改为开发者需要设定稍后提醒通知的唯一标识
let hashCode: string = 'hashCode';
let delayTime: number = 60;
notificationManager.snoozeNotification(hashCode, delayTime).then(() => {
  console.info('snoozeNotification success.')
}).catch((err: BusinessError):void => {
  console.error(`snoozeNotification failed, code is ${err.code}, message is ${err.message}`);
});
```
