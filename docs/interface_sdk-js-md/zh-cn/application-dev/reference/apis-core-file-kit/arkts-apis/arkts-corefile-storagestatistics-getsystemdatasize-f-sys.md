# getSystemDataSize（系统接口）

## 导入模块

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getSystemDataSize

```TypeScript
function getSystemDataSize(): Promise<number>
```

获取系统数据的总空间大小，使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.STORAGE_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13600018 |
