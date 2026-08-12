# setBadgeNumber

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void
```

设定角标个数，在应用的桌面图标上呈现。使用callback异步回调。

角标是应用桌面图标右上角显示的数字标识，用于提示用户有未处理的通知数量。 设定后，桌面图标将显示对应角标数字。适用于需要在桌面图标上提示用户 待处理消息数量的场景，如未读消息数、待办事项数等。

**起始版本：** 10

<!--Device-notificationManager-function setBadgeNumber(badgeNumber: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function setBadgeNumber(badgeNumber: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[getActiveNotificationCount](notificationManager.getActiveNotificationCount(callback: AsyncCallback<long>): void) 获取当前应用的通知数量。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| badgeNumber | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [1600012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-内存空间不足) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let setBadgeNumberCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in setting badge number.`);
  }
}
let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber, setBadgeNumberCallback);
```


## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: number): Promise<void>
```

设定角标个数，在应用的桌面图标上呈现。使用Promise异步回调。

角标是应用桌面图标右上角显示的数字标识，用于提示用户有未处理的通知数量。 设定后，桌面图标将显示对应角标数字。适用于需要在桌面图标上提示用户 待处理消息数量的场景，如未读消息数、待办事项数等。

**起始版本：** 10

<!--Device-notificationManager-function setBadgeNumber(badgeNumber: int): Promise<void>--><!--Device-notificationManager-function setBadgeNumber(badgeNumber: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[getActiveNotificationCount](notificationManager.getActiveNotificationCount(callback: AsyncCallback<long>): void) 获取当前应用的通知数量。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| badgeNumber | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [1600012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-内存空间不足) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let badgeNumber: number = 10;
notificationManager.setBadgeNumber(badgeNumber).then(() => {
  console.info(`Succeeded in setting badge number.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set badge number. Code is ${err.code}, message is ${err.message}`);
});
```
