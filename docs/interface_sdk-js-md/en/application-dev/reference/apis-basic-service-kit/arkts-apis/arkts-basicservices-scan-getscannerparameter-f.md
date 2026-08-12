# getScannerParameter

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## getScannerParameter

```TypeScript
function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>
```

Obtains scanner parameters. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>--><!--Device-scan-function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scannerId | string | Yes | Scanner ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ScannerParameter](arkts-basicservices-scan-scannerparameter-i.md)[]&gt; | Promise used to return the scanner parameters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let scannerId: string = 'scanner_001';
scan.getScannerParameter(scannerId).then((parameters: scan.ScannerParameter[]) => {
    console.info('get scanner parameters success: ' + JSON.stringify(parameters));
}).catch((error: BusinessError) => {
    console.error('get scanner parameters failed: ' + JSON.stringify(error));
})
```

