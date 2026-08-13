# getFreeSizeSync（系统接口）

## getFreeSizeSync

```TypeScript
function getFreeSizeSync(): number
```

同步获取内置存储的可用空间大小（单位为Byte）。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** 
- API版本10 - 14：ohos.permission.STORAGE_MANAGER

<!--Device-storageStatistics-function getFreeSizeSync(): long--><!--Device-storageStatistics-function getFreeSizeSync(): long-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let freeSize = storageStatistics.getFreeSizeSync();
  console.info('getFreeSizeSync successfully:' + freeSize);
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`getFreeSizeSync failed. Code: ${error.code}, message: ${error.message}`);
}
```
