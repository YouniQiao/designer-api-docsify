# setStaticSubscriberState (System API)

## Modules to Import

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## setStaticSubscriberState

```TypeScript
function setStaticSubscriberState(enable: boolean, callback: AsyncCallback<void>): void
```

为当前应用设置静态订阅事件使能或去使能状态。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 表示静态订阅事件使能状态。true：使能，false：去使能。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当设置静态订阅事件使能状态成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1500007 | Failed to send the message to the common event service. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 1500008 | Failed to initialize the common event service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

commonEventManager.setStaticSubscriberState(true, (err: BusinessError) => {
  if (err.code != 0) {
    console.error(`setStaticSubscriberState failed, errCode: ${err.code}, errMsg: ${err.message}`);
    return;
  }
  console.info(`setStaticSubscriberState success`);
});
```


## setStaticSubscriberState

```TypeScript
function setStaticSubscriberState(enable: boolean): Promise<void>
```

为当前应用设置静态订阅事件使能或去使能状态。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean): Promise<void>--><!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 表示静态订阅事件使能状态。true：使能，false：去使能。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1500007 | Failed to send the message to the common event service. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 1500008 | Failed to initialize the common event service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

commonEventManager.setStaticSubscriberState(false).then(() => {
  console.info(`setStaticSubscriberState success`);
}).catch((err: BusinessError) => {
  console.error(`setStaticSubscriberState failed, errCode: ${err.code}, errMsg: ${err.message}`);
});
```


## setStaticSubscriberState

```TypeScript
function setStaticSubscriberState(enable: boolean, events?: Array<string>): Promise<void>
```

设置当前应用的静态订阅公共事件的使能状态。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, events?: Array<string>): Promise<void>--><!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, events?: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 表示静态订阅事件使能状态。true：使能，false：去使能。 |
| events | Array&lt;string&gt; | No | 表示需要设置的公共事件名称列表，默认为空列表，表示设置当前应用所有的 静态订阅公共事件状态。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1500007 | Failed to send the message to the common event service. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 1500008 | Failed to initialize the common event service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let eventName: string[] = ['usual.event.SEND_DATA'];
commonEventManager.setStaticSubscriberState(true, eventName).then(() => {
  console.info(`setStaticSubscriberState success`);
}).catch((err: BusinessError) => {
  console.error(`setStaticSubscriberState failed, errCode: ${err.code}, errMsg: ${err.message}`);
});
```


## setStaticSubscriberState

```TypeScript
function setStaticSubscriberState(enable: boolean, events: Array<string>): Promise<void>
```

为当前应用设置静态订阅事件的使能状态，并且记录事件名称。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, events: Array<string>): Promise<void>--><!--Device-commonEventManager-function setStaticSubscriberState(enable: boolean, events: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Notification.CommonEvent

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 表示静态订阅事件使能状态。 true：使能 false：去使能。 |
| events | Array&lt;string&gt; | Yes | 表示记录事件名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1500007 | Failed to send the message to the common event service. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 1500008 | Failed to initialize the common event service. |

