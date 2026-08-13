# getBundleStats（系统接口）

## getBundleStats

```TypeScript
function getBundleStats(packageName: string, callback: AsyncCallback<BundleStats>, index?: number): void
```

异步获取应用存储数据的空间大小（单位为Byte），以callback方式返回。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getBundleStats(packageName: string, callback: AsyncCallback<BundleStats>, index?: int): void--><!--Device-storageStatistics-function getBundleStats(packageName: string, callback: AsyncCallback<BundleStats>, index?: int): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [packageName](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-inputmethodproperty-i.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleStats](arkts-corefile-storagestatistics-bundlestats-i.md)&gt; | 是 |
| index | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600008 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

## 示例

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
  storageStatistics.getBundleStats(packageName, (err: BusinessError, bundleStats: storageStatistics.BundleStats) => {
    if (err) {
      console.error(`getBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
    } else {
      hilog.info(0x0000, 'testTag', 'getBundleStats successfully. BundleStats: %{public}s', JSON.stringify(bundleStats));
    }
  }, index);

} catch (err) {
  let message = (err as BusinessError).message;
  console.error(`getBundleResourceInfo failed with err, message is: ${message}`);
}
```


## getBundleStats

```TypeScript
function getBundleStats(packageName: string, index?: number): Promise<BundleStats>
```

异步获取应用存储数据的空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getBundleStats(packageName: string, index?: int): Promise<BundleStats>--><!--Device-storageStatistics-function getBundleStats(packageName: string, index?: int): Promise<BundleStats>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [packageName](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-inputmethodproperty-i.md) | string | 是 |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[BundleStats](arkts-corefile-storagestatistics-bundlestats-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600008 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

## 示例

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
  storageStatistics.getBundleStats(packageName, index).then((bundleStats: storageStatistics.BundleStats) => {
    hilog.info(0x0000, 'testTag', 'getBundleStats successfully. BundleStats: %{public}s', JSON.stringify(bundleStats));
  }).catch((err: BusinessError) => {
    console.error(`getBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
  });

} catch (err) {
  let message = (err as BusinessError).message;
  console.error(`getBundleResourceInfo failed with err, message is: ${message}`);
}
```
