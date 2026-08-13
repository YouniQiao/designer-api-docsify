# cancel

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## cancel

```TypeScript
function cancel(id: number, callback: AsyncCallback<void>): void
```

根据指定的通知ID取消已发布的通知。使用callback异步回调。 取消后，对应的通知将从通知中心、状态栏等位置移除，用户不再可见。 与带label参数的notificationManager.cancel(id, label, callback)相比， 此接口不传入label，将取消与指定ID匹配的通知。当发布通知， label不为空时，则需使用接口notificationManager.cancel(id, label, callback)取消通知。

**起始版本：** 23

**废弃版本：** -1

<!--Device-notificationManager-function cancel(id: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancel(id: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

publish 发布通知。

cancelAll 取消当前应用所有已发布的通知。

cancelGroup 取消当前应用指定组下的通知。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// cancel回调
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling notification.`);
  }
}
notificationManager.cancel(0, cancelCallback);
```


## cancel

```TypeScript
function cancel(id: number, label: string, callback: AsyncCallback<void>): void
```

根据通知ID和标签取消已发布的通知。使用callback异步回调。 取消后，对应的通知将从通知中心、状态栏等位置移除，用户不再可见。 适用于需要精确取消某一条带有特定标签的通知的场景。 与仅传入通知ID的notificationManager.cancel(id, callback)相比， 此接口额外传入label参数，可精确取消同一ID，不同标签的通知。

**起始版本：** 23

**废弃版本：** -1

<!--Device-notificationManager-function cancel(id: int, label: string, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancel(id: int, label: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

publish 发布通知。

cancelAll 取消当前应用所有已发布的通知。

cancelGroup 取消当前应用指定组下的通知。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| label | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// cancel回调
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling notification.`);
  } 
}
notificationManager.cancel(0, 'label', cancelCallback);
```


## cancel

```TypeScript
function cancel(id: number, label?: string): Promise<void>
```

根据通知ID和标签label取消已发布的通知。使用Promise异步回调。 取消后，对应的通知将从通知中心、状态栏等位置移除，用户不再可见。

**起始版本：** 23

**废弃版本：** -1

<!--Device-notificationManager-function cancel(id: int, label?: string): Promise<void>--><!--Device-notificationManager-function cancel(id: int, label?: string): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**参见：**

publish 发布通知。

cancelAll 取消当前应用所有已发布的通知。

cancelGroup 取消当前应用指定组下的通知。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| label | string | 否 |

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
| [1600007](../errorcode-notification.md#1600007-通知不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancel(0).then(() => {
  console.info(`Succeeded in canceling notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
});
```
