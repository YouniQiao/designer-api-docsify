# subscribeSelf（系统接口）

## 导入模块

```TypeScript
import { notificationSubscribe } from '@kit.NotificationKit';
```

## subscribeSelf

```TypeScript
function subscribeSelf(subscriber: NotificationSubscriber): Promise<void>
```

订阅本应用的通知并指定订阅信息。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-notificationSubscribe-function subscribeSelf(subscriber: NotificationSubscriber): Promise<void>--><!--Device-notificationSubscribe-function subscribeSelf(subscriber: NotificationSubscriber): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subscriber | NotificationSubscriber | 是 | 通知订阅对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [1600012](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-内存空间不足) | No memory space. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) | Internal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not system application to call the interface. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-序列化或反序列化错误) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) | Failed to connect to the service. |

## 示例

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let onConsumeCallback = (data: notificationSubscribe.SubscribeCallbackData) => {
  console.info('Consume callback: ' + JSON.stringify(data));
}
let subscriber: notificationSubscribe.NotificationSubscriber = {
  onConsume: onConsumeCallback
};
notificationSubscribe.subscribeSelf(subscriber).then(() => {
  console.info('subscribeSelf success');
}).catch((err: Error): void => {
  let error: BusinessError = err as BusinessError;
  console.error(`subscribeSelf failed, code is ${error.code}, message is ${error.message}`);
});
```

