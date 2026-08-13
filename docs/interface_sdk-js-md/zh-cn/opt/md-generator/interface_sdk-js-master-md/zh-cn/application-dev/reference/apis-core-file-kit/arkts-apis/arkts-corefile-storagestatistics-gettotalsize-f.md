# getTotalSize

## getTotalSize

```TypeScript
function getTotalSize(): Promise<number>
```

获取内置存储的总空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 23

**废弃版本：** -1

<!--Device-storageStatistics-function getTotalSize(): Promise<long>--><!--Device-storageStatistics-function getTotalSize(): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

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
