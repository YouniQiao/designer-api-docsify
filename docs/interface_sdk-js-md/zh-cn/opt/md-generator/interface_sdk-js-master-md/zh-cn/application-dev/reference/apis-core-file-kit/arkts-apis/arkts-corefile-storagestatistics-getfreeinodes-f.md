# getFreeInodes

## getFreeInodes

```TypeScript
function getFreeInodes(): Promise<number>
```

获取文件系统的inode资源剩余量，仅支持查询系统数据分区。使用Promise异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-storageStatistics-function getFreeInodes(): Promise<long>--><!--Device-storageStatistics-function getFreeInodes(): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13600016 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getFreeInodes().then((freeInodes: number) => {
  console.info('getFreeInodes successfully:' + freeInodes);
}).catch((err: BusinessError) => {
  console.error(`getFreeInodes failed. Code: ${err.code}, message: ${err.message}`);
});
```
