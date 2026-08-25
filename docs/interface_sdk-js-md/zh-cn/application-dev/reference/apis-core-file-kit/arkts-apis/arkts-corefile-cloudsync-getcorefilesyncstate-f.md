# getCoreFileSyncState

## 导入模块

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## getCoreFileSyncState

```TypeScript
function getCoreFileSyncState(uri: string): FileState
```

同步方法获取云盘文件同步上行状态。

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| [FileState](arkts-corefile-cloudsync-filestate-e.md) |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13900002 |
| 13900004 |
| 13900010 |
| 13900012 |
| 13900020 |
| 13900031 |
| 14000002 |
| 22400005 |
