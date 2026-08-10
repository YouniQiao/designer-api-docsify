# on (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void
```

开启屏幕状态变化的监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | 回调函数。返回屏幕的id，该参数为整数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// Subscribe to the screen connection event.
screen.on('connect', callback);
```


## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void
```

开启屏幕状态变化的监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | 回调函数。返回屏幕的id，该参数为整数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// Subscribe to the screen connection event.
screen.on('connect', callback);
```


## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void
```

开启屏幕状态变化的监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | Yes | 回调函数。返回屏幕的id，该参数为整数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// Subscribe to the screen connection event.
screen.on('connect', callback);
```

