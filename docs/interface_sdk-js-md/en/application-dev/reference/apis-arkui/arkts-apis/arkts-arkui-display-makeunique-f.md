# makeUnique

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## makeUnique

```TypeScript
function makeUnique(screenId: long): Promise<void>
```

将屏幕设置为异源模式，使用Promise异步回调。

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_VIRTUAL_SCREEN

<!--Device-display-function makeUnique(screenId: long): Promise<void>--><!--Device-display-function makeUnique(screenId: long): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 要设置成异源模式的屏幕ID。其中id应为大于0的整数，否则返回401错误码。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. Function makeUnique can not work correctly due to limited device capabilities. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

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

