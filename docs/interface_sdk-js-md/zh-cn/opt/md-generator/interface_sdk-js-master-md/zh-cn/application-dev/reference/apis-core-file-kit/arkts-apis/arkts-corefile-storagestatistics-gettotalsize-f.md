# getTotalSize

## getTotalSize

```TypeScript
function getTotalSize(callback: AsyncCallback<number>): void
```

获取内置存储的总空间大小（单位为Byte），以callback方式返回。

**起始版本：** 15

**需要权限：** 
- API版本9 - 14：ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getTotalSize(callback: AsyncCallback<long>): void--><!--Device-storageStatistics-function getTotalSize(callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize((error: BusinessError, totalSize: number) => {
  if (error) {
    console.error(`getTotalSize failed. Code: ${error.code}, message: ${error.message}`);
  } else {
    // do something
    console.info('getTotalSize successfully:' + totalSize);
  }
});
```


## getTotalSize

```TypeScript
function getTotalSize(): Promise<number>
```

获取内置存储的总空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 15

<!--Device-storageStatistics-function getTotalSize(): Promise<long>--><!--Device-storageStatistics-function getTotalSize(): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
storageStatistics.getTotalSize().then((totalSize: number) => {
  console.info('getTotalSize successfully:' + totalSize);
}).catch((err: BusinessError) => {
  console.error(`getTotalSize failed. Code: ${err.code}, message: ${err.message}`);
});
```
