# setNotificationSwitch（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setNotificationSwitch

```TypeScript
function setNotificationSwitch(switchName: string, switchState: boolean, userId: number): Promise<void>
```

设置通知开关状态。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-notificationManager-function setNotificationSwitch(switchName: string, switchState: boolean, userId: int): Promise<void>--><!--Device-notificationManager-function setNotificationSwitch(switchName: string, switchState: boolean, userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [switchName](arkts-notification-notificationsubscriber-notificationswitchchangedcallbackdata-i-sys.md) | string | 是 |
| switchState | boolean | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600008-用户不存在) |
| [1600012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-内存空间不足) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let switchName: string = 'DEAL';
let switchState: boolean = true;
let userId: number = 100;

notificationManager.setNotificationSwitch(switchName, switchState, userId).then(() => {
    console.info('setNotificationSwitch success');
}).catch((err: BusinessError) => {
    console.error(`setNotificationSwitch failed, code is ${err.code}, message is ${err.message}`);
});
```
