# cancel

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## cancel

```TypeScript
function cancel(id: int, callback: AsyncCallback<void>): void
```

根据指定的通知ID取消已发布的通知。使用callback异步回调。

取消后，对应的通知将从通知中心、状态栏等位置移除，用户不再可见。与带label参数的notificationManager.cancel(id, label, callback)相比，此接口不传入label，将取消与指定ID匹配的通知。当发布通知，label不为空时，则需使用接口notificationManager.cancel(id, label, callback)取消通知。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-notificationManager-function cancel(id: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancel(id: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 通知ID，用于标识目标通知。该值由发布通知时NotificationRequest的id字段指定。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当取消已发布的通知成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// cancel callback
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
function cancel(id: int, label: string, callback: AsyncCallback<void>): void
```

根据通知ID和标签取消已发布的通知。使用callback异步回调。

取消后，对应的通知将从通知中心、状态栏等位置移除，用户不再可见。适用于需要精确取消某一条带有特定标签的通知的场景。与仅传入通知ID的notificationManager.cancel(id, callback)相比，此接口额外传入label参数，可精确取消同一ID，不同标签的通知。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-notificationManager-function cancel(id: int, label: string, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function cancel(id: int, label: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 通知ID，用于标识目标通知。该值由发布通知时NotificationRequest的id字段指定。 |
| label | string | Yes | 通知标签。该值由发布通知时NotificationRequest的label字段指定。 - 若标签为空，则取消与指定通知ID匹配，标签为空的已发布通知。 - 若标签不为空，则取消与指定通知ID和标签同时匹配的已发布通知。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。根据通知ID和标签取消已发布的通知成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// cancel callback
let cancelCallback = (err: BusinessError): void => {
  if (err) {
    console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`Succeeded in canceling notification.`);
  } 
}
notificationManager.cancel(0, "label", cancelCallback);
```


## cancel

```TypeScript
function cancel(id: int, label?: string): Promise<void>
```

根据通知ID和标签label取消已发布的通知。使用Promise异步回调。

取消后，对应的通知将从通知中心、状态栏等位置移除，用户不再可见。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-notificationManager-function cancel(id: int, label?: string): Promise<void>--><!--Device-notificationManager-function cancel(id: int, label?: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 通知ID，用于标识目标通知。该值由发布通知时NotificationRequest的id字段指定。 |
| label | string | No | 通知标签，默认为空。该值由发布通知时NotificationRequest的label字段指定。 - 若标签为空，则取消与指定通知ID匹配，标签为空的已发布通知。 - 若标签不为空，则取消与指定通知ID和标签同时匹配的已发布通知。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.cancel(0).then(() => {
  console.info(`Succeeded in canceling notification.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to cancel notification. Code is ${err.code}, message is ${err.message}`);
});
```

