# getScannerCurrentSetting

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## getScannerCurrentSetting

```TypeScript
function getScannerCurrentSetting(scannerId: string, optionIndex: int): Promise<ScannerOptionValue>
```

获取当前扫描仪设置。使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function getScannerCurrentSetting(scannerId: string, optionIndex: int): Promise<ScannerOptionValue>--><!--Device-scan-function getScannerCurrentSetting(scannerId: string, optionIndex: int): Promise<ScannerOptionValue>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scannerId | string | Yes | 扫描仪的ID。 |
| optionIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要获取的选项的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ScannerOptionValue&gt; | Promise对象，返回扫描仪选项值。 |

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
scan.getScannerCurrentSetting(scannerId, optionIndex).then((value: scan.ScannerOptionValue) => {
    console.info('get scanner current setting success: ' + JSON.stringify(value));
}).catch((error: BusinessError) => {
    console.error('get scanner current setting failed: ' + JSON.stringify(error));
})
```

