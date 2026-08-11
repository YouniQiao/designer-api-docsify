# getScannerParameter

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## getScannerParameter

```TypeScript
function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>
```

Obtains scanner parameters. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>--><!--Device-scan-function getScannerParameter(scannerId: string): Promise<ScannerParameter[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scannerId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ScannerParameter[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

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
