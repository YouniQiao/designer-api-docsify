# makeUnique

## Modules to Import

```TypeScript
```

## makeUnique

```TypeScript
function makeUnique(screenId: number): Promise<void>
```

Sets the screen to independent display mode. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_VIRTUAL_SCREEN

<!--Device-display-function makeUnique(screenId: long): Promise<void>--><!--Device-display-function makeUnique(screenId: long): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| screenId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 0;
// Set the screen to independent mode.
display.makeUnique(screenId).then(() => {
  console.info('Succeeded in making unique screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to make unique screens. Code: ${err.code}, message: ${err.message}`);
});
```
