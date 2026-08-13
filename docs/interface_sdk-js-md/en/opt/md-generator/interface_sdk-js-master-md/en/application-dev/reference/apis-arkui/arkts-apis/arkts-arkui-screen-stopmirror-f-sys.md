# stopMirror (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<number>, callback: AsyncCallback<void>): void
```

Stops mirror mode. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-screen-function stopMirror(mirrorScreen:Array<long>, callback: AsyncCallback<void>): void--><!--Device-screen-function stopMirror(mirrorScreen:Array<long>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mirrorScreen | Array & lt;number & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the screen ID using getAllScreens().
let mirrorScreenIds: Array<number> = [1, 2, 3]; // ID array of mirrored screens.
// Stop the mirror mode.
screen.stopMirror(mirrorScreenIds, (err: BusinessError) => {
  const errCode: number = err.code;
  if (errCode) {
    console.error(`Failed to stop mirror screens. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in stopping mirror screens.');
});
```


## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<number>): Promise<void>
```

Stops mirror mode. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-screen-function stopMirror(mirrorScreen:Array<long>): Promise<void>--><!--Device-screen-function stopMirror(mirrorScreen:Array<long>): Promise<void>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mirrorScreen | Array & lt;number & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the screen ID using getAllScreens().
let mirrorScreenIds: Array<number> = [1, 2, 3]; // ID array of mirrored screens.
// Stop the mirror mode.
screen.stopMirror(mirrorScreenIds).then(() => {
  console.info('Succeeded in stopping mirror screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to stop mirror screens. Code: ${err.code}, message: ${err.message}`);
});
```
