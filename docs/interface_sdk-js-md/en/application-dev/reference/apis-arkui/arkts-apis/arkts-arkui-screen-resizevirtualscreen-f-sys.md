# resizeVirtualScreen (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## resizeVirtualScreen

```TypeScript
function resizeVirtualScreen(screenId:long, width: long, height: long): Promise<void>
```

修改指定虚拟屏的尺寸，使用Promise异步回调。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-screen-function resizeVirtualScreen(screenId:long, width: long, height: long): Promise<void>--><!--Device-screen-function resizeVirtualScreen(screenId:long, width: long, height: long): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| screenId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 要修改的虚拟屏的屏幕ID，取值范围为[1000, 2147483647]的正整数，超出有效范围时返回错误码1400004。 |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 虚拟屏的新宽度，单位为px，取值范围为[1, 65536]的正整数，超出有效范围时返回错误码1400004。 |
| height | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes | 虚拟屏的新高度，单位为px，取值范围为[1, 65536]的正整数，超出有效范围时返回错误码1400004。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Function can not work because the current device does not support this ability. |
| 1400004 | Parameter error. Possible cause: 1. Invalid parameter range. |
| 1400001 | Invalid display or screen. |
| 1400003 | This display manager service works abnormally. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

