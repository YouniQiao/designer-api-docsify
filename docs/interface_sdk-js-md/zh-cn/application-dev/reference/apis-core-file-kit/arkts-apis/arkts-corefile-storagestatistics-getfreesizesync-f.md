# getFreeSizeSync

## 导入模块

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getFreeSizeSync

```TypeScript
function getFreeSizeSync(): number
```

同步获取内置存储的可用空间大小（单位为Byte）。

**起始版本：** 15

**需要权限：** 
- API版本10 - 14：ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

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
