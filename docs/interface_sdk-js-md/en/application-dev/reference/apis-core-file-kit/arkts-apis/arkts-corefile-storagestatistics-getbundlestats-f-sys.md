# getBundleStats (System API)

## Modules to Import

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getBundleStats

```TypeScript
function getBundleStats(packageName: string, callback: AsyncCallback<BundleStats>, index?: int): void
```

异步获取应用存储数据的空间大小（单位为Byte），以callback方式返回。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getBundleStats(packageName: string, callback: AsyncCallback<BundleStats>, index?: int): void--><!--Device-storageStatistics-function getBundleStats(packageName: string, callback: AsyncCallback<BundleStats>, index?: int): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| packageName | string | Yes | 应用包名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;BundleStats&gt; | Yes | 获取指定卷上的应用存储数据的空间大小之后的回调。 |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 分身应用的索引号，默认值为0（表示未分身的主应用）。分身应用索引号在分身创建时默认 占用从1开始且当前未被占用的最小索引号，并赋值给该应用的 [BundleResourceInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundleresourceinfo-i-sys.md/arkts-ability-bundleresourceinfo-i-sys.md)的appIndex属性，后续可以通过调用 [getBundleResourceInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundleresourcemanager-getbundleresourceinfo-f-sys.md/arkts-ability-bundleresourcemanager-getbundleresourceinfo-f-sys.md#getbundleresourceinfo) 接口获得。<br>**Since:** 12 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid. |
| 13600008 | No such object. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

## Examples

```TypeScript
import { bundleResourceManager } from '@kit.AbilityKit';
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.example.myapplication";
let bundleFlags = bundleResourceManager.ResourceFlag.GET_RESOURCE_INFO_ALL;
try {
  let resourceInfo = bundleResourceManager.getBundleResourceInfo(bundleName, bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleResourceInfo successfully. Data label: %{public}s', JSON.stringify(resourceInfo.label));

  let packageName:string = bundleName;
  let index:number = resourceInfo.appIndex;
  storageStatistics.getBundleStats(packageName, (err: BusinessError, BundleStats: storageStatistics.BundleStats) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getBundleStats failed with error: %{public}s', JSON.stringify(err));
    } else {
      hilog.info(0x0000, 'testTag', 'getBundleStats successfully. BundleStats: %{public}s', JSON.stringify(BundleStats));
    }
  }, index);

} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleResourceInfo failed: %{public}s', message);
}
```


## getBundleStats

```TypeScript
function getBundleStats(packageName: string, index?: int): Promise<BundleStats>
```

异步获取应用存储数据的空间大小（单位为Byte），以Promise方式返回。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getBundleStats(packageName: string, index?: int): Promise<BundleStats>--><!--Device-storageStatistics-function getBundleStats(packageName: string, index?: int): Promise<BundleStats>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.SpatialStatistics

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| packageName | string | Yes | 应用包名。 |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 分身应用的索引号，默认值为0（表示未分身的主应用）。分身应用索引号在分身创建时默认占用 从1开始且当前未被占用的最小索引号，并赋值给该应用的 [BundleResourceInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundleresourceinfo-i-sys.md/arkts-ability-bundleresourceinfo-i-sys.md)的appIndex属性，后续可以通过调用 [getBundleResourceInfo] {@link @ohos.bundle.bundleResourceManager:bundleResourceManager.getBundleResourceInfo(bundleName: string, resourceFlags?: int, appIndex?: int)} 接口获得。<br>**Since:** 12 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;BundleStats&gt; | Promise对象，返回指定卷上的应用存储数据的空间大小（单位为Byte）。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid. |
| 13600008 | No such object. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

## Examples

```TypeScript
import { bundleResourceManager } from '@kit.AbilityKit';
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.example.myapplication";
let bundleFlags = bundleResourceManager.ResourceFlag.GET_RESOURCE_INFO_ALL;
try {
  let resourceInfo = bundleResourceManager.getBundleResourceInfo(bundleName, bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleResourceInfo successfully. Data label: %{public}s', JSON.stringify(resourceInfo.label));

  let packageName:string = bundleName;
  let index:number = resourceInfo.appIndex;
  storageStatistics.getBundleStats(packageName, index).then((BundleStats: storageStatistics.BundleStats) => {
    hilog.info(0x0000, 'testTag', 'getBundleStats successfully. BundleStats: %{public}s', JSON.stringify(BundleStats));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getBundleStats failed with error: %{public}s', JSON.stringify(err));
  });

} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleResourceInfo failed with error: %{public}s', message);
}
```

