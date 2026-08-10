# getAllExtBundleStats (System API)

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getAllExtBundleStats

```TypeScript
function getAllExtBundleStats(userId: int): Promise<Array<ExtBundleStats>>
```

获取指定用户下所有系统应用或系统服务的空间占用详情。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.STORAGE_MANAGER

**Model restriction:** This API can be used only in the stage model.

<!--Device-storageStatistics-function getAllExtBundleStats(userId: int): Promise<Array<ExtBundleStats>>--><!--Device-storageStatistics-function getAllExtBundleStats(userId: int): Promise<Array<ExtBundleStats>>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 用户id。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;ExtBundleStats&gt;&gt; | Promise对象，返回指定用户下所有系统应用或系统服务的空间占用详情。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13600013 | Failed to query all business space usage. |
| 13600010 | The input parameter is invalid. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. |

## Examples

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
storageStatistics.getAllExtBundleStats(userId).then((bundleStatsList: storageStatistics.ExtBundleStats[]) => {
  console.info("getAllExtBundleStats successfully");
}).catch((err: BusinessError) => {
  console.error(`getAllExtBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```

