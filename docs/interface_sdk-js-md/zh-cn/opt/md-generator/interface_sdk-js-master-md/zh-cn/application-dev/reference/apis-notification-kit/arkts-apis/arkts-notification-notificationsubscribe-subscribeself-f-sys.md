# subscribeSelf（系统接口）

## 导入模块

```TypeScript
import { notificationSubscribe } from 'kits/@kit.NotificationKit';
```

## subscribeSelf

```TypeScript
function subscribeSelf(subscriber: NotificationSubscriber): Promise<void>
```

订阅本应用的通知并指定订阅信息。使用Promise异步回调。

**起始版本：** 11

<!--Device-notificationSubscribe-function subscribeSelf(subscriber: NotificationSubscriber): Promise<void>--><!--Device-notificationSubscribe-function subscribeSelf(subscriber: NotificationSubscriber): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [NotificationSubscriber](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let onConsumeCallback = (data: notificationSubscribe.SubscribeCallbackData) => {
  console.info(`Consume callback:  ${JSON.stringify(data)}`);
}
let subscriber: notificationSubscribe.NotificationSubscriber = {
  onConsume: onConsumeCallback
};
notificationSubscribe.subscribeSelf(subscriber).then(() => {
  console.info('subscribeSelf success');
}).catch((err: BusinessError) => {
  console.error(`subscribeSelf failed, code is ${err.code}, message is ${err.message}`);
});
```
