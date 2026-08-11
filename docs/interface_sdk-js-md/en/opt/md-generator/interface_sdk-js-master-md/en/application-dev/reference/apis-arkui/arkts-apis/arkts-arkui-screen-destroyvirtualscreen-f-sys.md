# destroyVirtualScreen (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## destroyVirtualScreen

```TypeScript
function destroyVirtualScreen(screenId:number, callback: AsyncCallback<void>): void
```

Destroys a virtual screen. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-screen-function destroyVirtualScreen(screenId:long, callback: AsyncCallback<void>): void--><!--Device-screen-function destroyVirtualScreen(screenId:long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| screenId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400002](../errorcode-display.md#1400002-unauthorized-operation) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the screen ID using getAllScreens() or from the return value of createVirtualScreen().
let screenId: number = 1; // Virtual screen ID.
// Destroy the virtual screen.
screen.destroyVirtualScreen(screenId, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to destroy the virtual screen. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in destroying the virtual screen.');
});
```


## destroyVirtualScreen

```TypeScript
function destroyVirtualScreen(screenId:number): Promise<void>
```

Destroys a virtual screen. This API uses a promise to return the result.

**Since:** 9

<!--Device-screen-function destroyVirtualScreen(screenId:long): Promise<void>--><!--Device-screen-function destroyVirtualScreen(screenId:long): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| screenId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400002](../errorcode-display.md#1400002-unauthorized-operation) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the screen ID using getAllScreens() or from the return value of createVirtualScreen().
let screenId: number = 1; // Virtual screen ID.
// Destroy the virtual screen.
screen.destroyVirtualScreen(screenId).then(() => {
  console.info('Succeeded in destroying the virtual screen.');
}).catch((err: BusinessError) => {
  console.error(`Failed to destroy the virtual screen. Code: ${err.code}, message: ${err.message}`);
});
```
