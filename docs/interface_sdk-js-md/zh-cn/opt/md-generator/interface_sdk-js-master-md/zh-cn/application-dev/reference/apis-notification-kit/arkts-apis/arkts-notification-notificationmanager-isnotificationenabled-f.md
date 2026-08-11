# isNotificationEnabled

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isNotificationEnabled

```TypeScript
function isNotificationEnabled(callback: AsyncCallback<boolean>): void
```

查询当前应用通知授权状态。使用callback异步回调。

用于在发布通知前检查当前应用是否被允许发送通知，避免在通知授权关闭时发布导致失败。

**起始版本：** 11

**需要权限：** 
- API版本9 - 10：ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isNotificationEnabled(callback: AsyncCallback<boolean>): void--><!--Device-notificationManager-function isNotificationEnabled(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let isNotificationEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`isNotificationEnabled success, data is ${JSON.stringify(data)}`);
  }
}

notificationManager.isNotificationEnabled(isNotificationEnabledCallback);
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(): Promise<boolean>
```

查询当前应用通知授权状态。使用Promise异步回调。

用于在发布通知前检查当前应用是否被允许发送通知，避免在通知使能关闭时发布导致失败。

**起始版本：** 11

**需要权限：** 
- API版本9 - 10：ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isNotificationEnabled(): Promise<boolean>--><!--Device-notificationManager-function isNotificationEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isNotificationEnabled().then((data: boolean) => {
  console.info(`isNotificationEnabled success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```
