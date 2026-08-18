# getFreeInodes

## Modules to Import

```TypeScript
```

## getFreeInodes

```TypeScript
function getFreeInodes(): Promise<number>
```

Get the free inodes.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-storageStatistics-function getFreeInodes(): Promise<long>--><!--Device-storageStatistics-function getFreeInodes(): Promise<long>-End-->

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

storageStatistics.getFreeInodes().then((freeInodes: number) => {
  console.info("getFreeInodes successfully: " + freeInodes);
}).catch((err: BusinessError) => {
  console.error(`getFreeInodes failed. Code: ${err.code}, Message: ${err.message}`);
});
```
