# getUserStorageStats（系统接口）

## 导入模块

```TypeScript
```

## getUserStorageStats

```TypeScript
function getUserStorageStats(): Promise<StorageStats>
```

异步获取当前用户各类别存储空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(): Promise<StorageStats>--><!--Device-storageStatistics-function getUserStorageStats(): Promise<StorageStats>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[StorageStats](arkts-corefile-storagestatistics-storagestats-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getUserStorageStats().then((storageStats: storageStatistics.StorageStats) => {
  console.info("getUserStorageStats successfully:" + JSON.stringify(storageStats));
}).catch((err: BusinessError) => {
  console.error(`getUserStorageStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```


## getUserStorageStats

```TypeScript
function getUserStorageStats(callback: AsyncCallback<StorageStats>): void
```

异步获取当前用户各类别存储空间大小（单位为Byte），以callback方式返回。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(callback: AsyncCallback<StorageStats>): void--><!--Device-storageStatistics-function getUserStorageStats(callback: AsyncCallback<StorageStats>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[StorageStats](arkts-corefile-storagestatistics-storagestats-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getUserStorageStats((error: BusinessError, storageStats: storageStatistics.StorageStats) => {
  if (error) {
    console.error(`getUserStorageStats failed with err, code is: ${error.code}, message is: ${error.message}`);
  } else {
    // do something
    console.info("getUserStorageStats successfully:" + JSON.stringify(storageStats));
  }
});
```


## getUserStorageStats

```TypeScript
function getUserStorageStats(userId: number): Promise<StorageStats>
```

异步获取指定用户各类别存储空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(userId: long): Promise<StorageStats>--><!--Device-storageStatistics-function getUserStorageStats(userId: long): Promise<StorageStats>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[StorageStats](arkts-corefile-storagestatistics-storagestats-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600009 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let userId: number = 100;
storageStatistics.getUserStorageStats(userId).then((storageStats: storageStatistics.StorageStats) => {
  console.info("getUserStorageStats successfully:" + JSON.stringify(storageStats));
}).catch((err: BusinessError) => {
  console.error(`getUserStorageStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```


## getUserStorageStats

```TypeScript
function getUserStorageStats(userId: number, callback: AsyncCallback<StorageStats>): void
```

异步获取指定用户各类别存储空间大小（单位为Byte），以callback方式返回。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(userId: long, callback: AsyncCallback<StorageStats>): void--><!--Device-storageStatistics-function getUserStorageStats(userId: long, callback: AsyncCallback<StorageStats>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[StorageStats](arkts-corefile-storagestatistics-storagestats-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600009 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let userId: number = 100;
storageStatistics.getUserStorageStats(userId, (error: BusinessError, storageStats: storageStatistics.StorageStats) => {
  if (error) {
    console.error(`getUserStorageStats failed with err, code is: ${error.code}, message is: ${error.message}`);
  } else {
    // do something
    console.info("getUserStorageStats successfully:" + JSON.stringify(storageStats));
  }
});
```
