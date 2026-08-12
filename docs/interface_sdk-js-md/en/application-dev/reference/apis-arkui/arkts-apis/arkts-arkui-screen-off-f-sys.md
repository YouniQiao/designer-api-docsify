# off (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## off

```TypeScript
function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void
```

Unsubscribes from events related to the screen state.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void--><!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes | Event type.&lt;br&gt;- **connect**: an event indicating that the screen is connected.&lt;br&gt;- **disconnect**: an event indicating that the screen is disconnected.&lt;br&gt;- **change**: an event indicating that the screen state changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;long&gt; | No | Callback used to return the screen ID, which is an integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for screen changes. Data: ${data}`)
};
screen.off('connect', callback);
screen.off('connect');
```


## off

```TypeScript
function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void
```

Unsubscribes from events related to the screen state.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void--><!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes | Event type.&lt;br&gt;- **connect**: an event indicating that the screen is connected.&lt;br&gt;- **disconnect**: an event indicating that the screen is disconnected.&lt;br&gt;- **change**: an event indicating that the screen state changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;long&gt; | No | Callback used to return the screen ID, which is an integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for screen changes. Data: ${data}`)
};
screen.off('connect', callback);
screen.off('connect');
```


## off

```TypeScript
function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void
```

Unsubscribes from events related to the screen state.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void--><!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes | Event type.&lt;br&gt;- **connect**: an event indicating that the screen is connected.&lt;br&gt;- **disconnect**: an event indicating that the screen is disconnected.&lt;br&gt;- **change**: an event indicating that the screen state changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;long&gt; | No | Callback used to return the screen ID, which is an integer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for screen changes. Data: ${data}`)
};
screen.off('connect', callback);
screen.off('connect');
```

