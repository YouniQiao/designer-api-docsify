# getAddedScanners (System API)

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## getAddedScanners

```TypeScript
function getAddedScanners(): Promise<ScannerDevice[]>
```

Obtains the added scanners. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function getAddedScanners(): Promise<ScannerDevice[]>--><!--Device-scan-function getAddedScanners(): Promise<ScannerDevice[]>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.getAddedScanners().then((scanners: scan.ScannerDevice[]) => {
    console.info('get added scanners success: ' + JSON.stringify(scanners));
}).catch((error: BusinessError) => {
    console.error('get added scanners failed: ' + JSON.stringify(error));
})
```
