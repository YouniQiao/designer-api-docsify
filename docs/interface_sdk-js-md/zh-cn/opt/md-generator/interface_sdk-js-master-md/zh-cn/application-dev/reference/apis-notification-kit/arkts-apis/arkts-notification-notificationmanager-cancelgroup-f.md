# cancelGroup

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## cancelGroup

```TypeScript
function cancelGroup(groupName: string, callback: AsyncCallback<void>): void
```

取消当前应用指定组下的通知。使用callback异步回调。 通知组groupName是在发布通知时通过NotificationRequest的groupName字段指定的分组标识。 取消后，该组下所有通知将从通知中心移除。适用于需要按业务分组批量取消通知的场景。

**起始版本：** 23

**废弃版本：** -1

<!--Device-notificationManager-function cancelGroup(groupName: string, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancelGroup(groupName: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| groupName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let cancelGroupCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel group. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling group.`);
  }
}
let groupName: string = 'GroupName';
notificationManager.cancelGroup(groupName, cancelGroupCallback);
```


## cancelGroup

```TypeScript
function cancelGroup(groupName: string): Promise<void>
```

取消当前应用指定组下的通知。使用Promise异步回调。 通知组groupName是在发布通知时通过NotificationRequest的groupName字段指定的分组标识。 取消后，该组下所有通知将从通知中心移除。适用于需要按业务分组批量取消通知的场景。

**起始版本：** 23

**废弃版本：** -1

<!--Device-notificationManager-function cancelGroup(groupName: string): Promise<void>--><!--Device-notificationManager-function cancelGroup(groupName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| groupName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let groupName: string = 'GroupName';
notificationManager.cancelGroup(groupName).then(() => {
  console.info(`Succeeded in canceling group.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel group. Code is ${err.code}, message is ${err.message}`);
});
```
