# setScanAutoOption

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## setScanAutoOption

```TypeScript
function setScanAutoOption(scannerId: string, optionIndex: int): Promise<void>
```

设置扫描选项为自动模式。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function setScanAutoOption(scannerId: string, optionIndex: int): Promise<void>--><!--Device-scan-function setScanAutoOption(scannerId: string, optionIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scannerId | string | Yes | 扫描仪的ID。 |
| optionIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要设置为自动的选项的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let optionIndex: number = 1;
scan.setScanAutoOption(scannerId, optionIndex).then(() => {
    console.info('set scan auto option success');
}).catch((error: BusinessError) => {
    console.error('set scan auto option failed: ' + JSON.stringify(error));
})
```

