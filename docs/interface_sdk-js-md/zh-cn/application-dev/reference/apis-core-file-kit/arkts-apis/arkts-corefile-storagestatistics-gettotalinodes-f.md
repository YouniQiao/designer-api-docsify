# getTotalInodes

## 导入模块

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getTotalInodes

```TypeScript
function getTotalInodes(): Promise<number>
```

获取文件系统的inode资源总量，仅支持查询系统数据分区。使用Promise异步回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

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
