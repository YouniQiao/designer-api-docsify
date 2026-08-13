# makeUnique

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## makeUnique

```TypeScript
function makeUnique(screenId: long): Promise<void>
```

Sets the screen to independent display mode. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_VIRTUAL_SCREEN

<!--Device-display-function makeUnique(screenId: long): Promise<void>--><!--Device-display-function makeUnique(screenId: long): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | long | Yes | ID of the screen. Each ID must be an integer greater than 0; otherwise, error code 401 is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Function makeUnique can not work correctly due to limited device capabilities. |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) | Invalid display or screen. |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 0;
display.makeUnique(screenId).then(() => {
  console.info('Succeeded in making unique screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to make unique screens. Code:${err.code},message is ${err.message}`);
});
```

