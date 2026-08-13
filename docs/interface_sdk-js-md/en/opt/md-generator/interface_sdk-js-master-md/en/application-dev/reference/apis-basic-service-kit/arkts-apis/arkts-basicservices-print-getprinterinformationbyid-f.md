# getPrinterInformationById

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## getPrinterInformationById

```TypeScript
function getPrinterInformationById(printerId: string): Promise<PrinterInformation>
```

Obtains printer information based on the printer ID. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function getPrinterInformationById(printerId: string): Promise<PrinterInformation>--><!--Device-print-function getPrinterInformationById(printerId: string): Promise<PrinterInformation>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PrinterInformation](arkts-basicservices-print-printerinformation-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerId : string = 'testPrinterId';
print.getPrinterInformationById(printerId).then((printerInformation : print.PrinterInformation) => {
    console.info('getPrinterInformationById data : ' + JSON.stringify(printerInformation));
}).catch((error: BusinessError) => {
    console.error('getPrinterInformationById error : ' + JSON.stringify(error));
})
```
