# getTotalInodes

## Modules to Import

```TypeScript
```

## getTotalInodes

```TypeScript
function getTotalInodes(): Promise<number>
```

Get the total inodes.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-storageStatistics-function getTotalInodes(): Promise<long>--><!--Device-storageStatistics-function getTotalInodes(): Promise<long>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13600016 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getTotalInodes().then((totalInodes: number) => {
  console.info("getTotalInodes successfully: " + totalInodes);
}).catch((err: BusinessError) => {
  console.error(`getTotalInodes failed. Code: ${err.code}, Message: ${err.message}`);
});
```
