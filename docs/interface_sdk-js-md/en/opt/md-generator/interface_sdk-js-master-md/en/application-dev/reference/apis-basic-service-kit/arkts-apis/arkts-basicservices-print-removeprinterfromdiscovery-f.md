# removePrinterFromDiscovery

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## removePrinterFromDiscovery

```TypeScript
function removePrinterFromDiscovery(printerId: string): Promise<void>
```

Removes a printer from the printer discovery list. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PRINT

<!--Device-print-function removePrinterFromDiscovery(printerId: string): Promise<void>--><!--Device-print-function removePrinterFromDiscovery(printerId: string): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| printerId | string | Yes |

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

let printerId : string = 'testPrinterId';
print.removePrinterFromDiscovery(printerId).then(() => {
    console.info('removePrinterFromDiscovery success');
}).catch((error: BusinessError) => {
    console.error('removePrinterFromDiscovery error : ' + JSON.stringify(error));
})
```
