# init

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## init

```TypeScript
function init(): Promise<void>
```

Initializes the scan service. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function init(): Promise<void>--><!--Device-scan-function init(): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

scan.init().then(() => {
    console.info('scan init success');
}).catch((error: BusinessError) => {
    console.error('scan init failed: ' + JSON.stringify(error));
})
```
