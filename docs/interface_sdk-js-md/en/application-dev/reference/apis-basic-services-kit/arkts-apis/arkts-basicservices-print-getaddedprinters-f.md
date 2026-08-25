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

**System capability:** SystemCapability.Print.PrintFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
