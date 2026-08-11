# getAddedPrinters

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## getAddedPrinters

```TypeScript
function getAddedPrinters(): Promise<Array<string>>
```

Obtains the list of printers added to the system. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINT

<!--Device-print-function getAddedPrinters(): Promise<Array<string>>--><!--Device-print-function getAddedPrinters(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

print.getAddedPrinters().then((printers: string[]) => {
    console.info('getAddedPrinters success ' + JSON.stringify(printers));
    // ...
}).catch((error: BusinessError) => {
    console.error('failed to getAddedPrinters because ' + JSON.stringify(error));
})
```
