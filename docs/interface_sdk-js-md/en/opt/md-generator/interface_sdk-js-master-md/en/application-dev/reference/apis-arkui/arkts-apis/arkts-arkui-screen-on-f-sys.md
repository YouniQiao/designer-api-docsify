# on (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<number>): void
```

Subscribes to events related to the screen state.

**Since:** 9

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<number>): void
```

Subscribes to events related to the screen state.

**Since:** 9

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<number>): void
```

Subscribes to events related to the screen state.

**Since:** 9

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// Subscribe to the screen connection event.
screen.on('connect', callback);
```
