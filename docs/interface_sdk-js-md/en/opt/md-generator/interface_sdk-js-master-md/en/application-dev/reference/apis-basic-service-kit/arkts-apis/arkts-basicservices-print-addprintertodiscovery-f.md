# addPrinterToDiscovery

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## addPrinterToDiscovery

```TypeScript
function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>
```

Adds a printer to the printer discovery list. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>--><!--Device-print-function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerInformation | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId',
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOps'
};
print.addPrinterToDiscovery(printerInformation).then(() => {
    console.info('addPrinterToDiscovery success');
}).catch((error: BusinessError) => {
    console.error('addPrinterToDiscovery error : ' + JSON.stringify(error));
})
```
