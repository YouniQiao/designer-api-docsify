# addPrinterToCups (System API)

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## addPrinterToCups

```TypeScript
function addPrinterToCups(printerUri: string, printerName: string, printerMake: string): Promise<boolean>
```

Add a printer to cups.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function addPrinterToCups(printerUri: string, printerName: string, printerMake: string): Promise<boolean>--><!--Device-print-function addPrinterToCups(printerUri: string, printerName: string, printerMake: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerUri | string | Yes |
| printerName | string | Yes |
| [printerMake](arkts-basicservices-print-printerinformation-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13100003](../../apis-basic-services-kit/errorcode-print.md#13100003-print-service-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerUri : string = "testPrinterUri";
let printerName : string = "testPrinterName";
let printerMake : string = "testPrinterMake";

print.addPrinterToCups(printerUri, printerName, printerMake).then((result: boolean) => {
    console.info('addPrinterToCups success' + JSON.stringify(result));
}).catch((error: BusinessError) => {
    console.error('addPrinterToCups error : ' + JSON.stringify(error));
})
```
