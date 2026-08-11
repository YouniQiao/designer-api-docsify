# cancelAll

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## cancelAll

```TypeScript
function cancelAll(callback: AsyncCallback<void>): void
```

取消当前应用所有已发布的通知。使用callback异步回调。

取消后，当前应用的所有通知将从通知中心、状态栏等位置移除，用户不再可见。适用于应用退出或用户手动清除全部通知的场景。

**起始版本：** 9

<!--Device-notificationManager-function cancelAll(callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancelAll(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// cancelAll回调
let cancelAllCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling all notification.`);
  }
}
notificationManager.cancelAll(cancelAllCallback);
```


## cancelAll

```TypeScript
function cancelAll(): Promise<void>
```

取消当前应用所有已发布的通知。使用Promise异步回调。

取消后，当前应用的所有通知将从通知中心、状态栏等位置移除，用户不再可见。适用于应用退出或用户手动清除全部通知的场景。

**起始版本：** 9

<!--Device-notificationManager-function cancelAll(): Promise<void>--><!--Device-notificationManager-function cancelAll(): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancelAll().then(() => {
  console.info(`Succeeded in canceling all notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel all notification. Code is ${err.code}, message is ${err.message}`);
});
```
