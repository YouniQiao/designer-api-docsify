# getUserStorageStats（系统接口）

## 导入模块

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getUserStorageStats

```TypeScript
function getUserStorageStats(): Promise<StorageStats>
```

异步获取当前用户各类别存储空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(): Promise<StorageStats>--><!--Device-storageStatistics-function getUserStorageStats(): Promise<StorageStats>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;StorageStats&gt; | Promise对象，返回当前用户各类别存储空间大小（单位为Byte）。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

## 示例

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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(callback: AsyncCallback<StorageStats>): void--><!--Device-storageStatistics-function getUserStorageStats(callback: AsyncCallback<StorageStats>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;StorageStats&gt; | 是 | 返回用户各类别存储空间大小之后的回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

## 示例

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
function getUserStorageStats(userId: long): Promise<StorageStats>
```

异步获取指定用户各类别存储空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(userId: long): Promise<StorageStats>--><!--Device-storageStatistics-function getUserStorageStats(userId: long): Promise<StorageStats>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | 是 | 用户id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;StorageStats&gt; | Promise对象，返回指定用户各类别存储空间大小（单位为Byte）。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600009 | User if out of range. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

## 示例

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
function getUserStorageStats(userId: long, callback: AsyncCallback<StorageStats>): void
```

异步获取指定用户各类别存储空间大小（单位为Byte），以callback方式返回。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getUserStorageStats(userId: long, callback: AsyncCallback<StorageStats>): void--><!--Device-storageStatistics-function getUserStorageStats(userId: long, callback: AsyncCallback<StorageStats>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：long | 是 | 用户id。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;StorageStats&gt; | 是 | 返回指定用户各类别存储空间大小之后的回调。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600009 | User if out of range. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

## 示例

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

