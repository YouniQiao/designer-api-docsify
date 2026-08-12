# setScannerParameter

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## setScannerParameter

```TypeScript
function setScannerParameter(scannerId: string, optionIndex: int, value: ScannerOptionValue): Promise<void>
```

Sets scanner parameters. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function setScannerParameter(scannerId: string, optionIndex: int, value: ScannerOptionValue): Promise<void>--><!--Device-scan-function setScannerParameter(scannerId: string, optionIndex: int, value: ScannerOptionValue): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scannerId | string | Yes | Scanner ID. |
| optionIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Index of the option to be set. |
| value | [ScannerOptionValue](arkts-basicservices-scan-scanneroptionvalue-i.md) | Yes | Value to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
let optionIndex: number = 1;
let value: scan.ScannerOptionValue = {
    valueType: scan.OptionValueType.SCAN_TYPE_INT,
    numValue: 100
};
scan.setScannerParameter(scannerId, optionIndex, value).then(() => {
    console.info('set scanner parameter success');
}).catch((error: BusinessError) => {
    console.error('set scanner parameter failed: ' + JSON.stringify(error));
})
```

