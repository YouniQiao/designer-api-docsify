# getActiveNotificationCount

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(callback: AsyncCallback<number>): void
```

获取当前应用的通知数量。使用callback异步回调。

用于查询当前应用在通知中心中已发布的存量通知数量。适用于需要展示未读通知数量提示的场景。

**起始版本：** 9

<!--Device-notificationManager-function getActiveNotificationCount(callback: AsyncCallback<long>): void--><!--Device-notificationManager-function getActiveNotificationCount(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[setBadgeNumber](notificationManager.setBadgeNumber(badgeNumber: int,callback: AsyncCallback<void>): void) 设置角标个数。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let getActiveNotificationCountCallback = (err: BusinessError, data: number): void => {
  if (err) {
    console.error(`Failed to get active notification count. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in getting active notification count, data is ${JSON.stringify(data)}`);
  }
}

notificationManager.getActiveNotificationCount(getActiveNotificationCountCallback);
```


## getActiveNotificationCount

```TypeScript
function getActiveNotificationCount(): Promise<number>
```

获取当前应用的通知数量。使用Promise异步回调。

用于查询当前应用在通知中心中已发布的存量通知数量。适用于需要展示未读通知数量提示的场景。

**起始版本：** 9

<!--Device-notificationManager-function getActiveNotificationCount(): Promise<long>--><!--Device-notificationManager-function getActiveNotificationCount(): Promise<long>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

[setBadgeNumber](notificationManager.setBadgeNumber(badgeNumber: int): Promise<void>) 设置角标个数。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getActiveNotificationCount().then((data: number) => {
  console.info(`Succeeded in getting active notification count, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get active notification count. Code is ${err.code}, message is ${err.message}`);
});
```
