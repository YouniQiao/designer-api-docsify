# resizeVirtualScreen (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## resizeVirtualScreen

```TypeScript
function resizeVirtualScreen(screenId:number, width: number, height: number): Promise<void>
```

Resizes the virtual screen. This API uses a promise to return the result.

**Since:** 24

**Deprecated since:** -1

<!--Device-screen-function resizeVirtualScreen(screenId:long, width: long, height: long): Promise<void>--><!--Device-screen-function resizeVirtualScreen(screenId:long, width: long, height: long): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| screenId | number | Yes |
| width | number | Yes |
| height | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400004](../errorcode-display.md#1400004-parameter-error) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the virtual screen ID from the return value of createVirtualScreen().
let screenId: number = 1000; // Virtual screen ID.
let width: number = 1920;
let height: number = 1080;
// Resize the virtual screen.
screen.resizeVirtualScreen(screenId, width, height).then(() => {
  console.info(`Succeeded in resizing virtual screen: screenId=${screenId}, width=${width}, height=${height}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set screen area mirroring. Code: ${err.code}, message: ${err.message}`);
});
```
