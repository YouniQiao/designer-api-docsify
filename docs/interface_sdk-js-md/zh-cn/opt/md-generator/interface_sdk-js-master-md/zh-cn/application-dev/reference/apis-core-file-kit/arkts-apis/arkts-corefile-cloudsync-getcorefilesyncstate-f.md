# getCoreFileSyncState

## getCoreFileSyncState

```TypeScript
function getCoreFileSyncState(uri: string): FileState
```

同步方法获取云盘文件同步上行状态。

**起始版本：** 20

<!--Device-cloudSync-function getCoreFileSyncState(uri: string): FileState--><!--Device-cloudSync-function getCoreFileSyncState(uri: string): FileState-End-->

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
| 13900004 |
| 13900020 |
| 22400005 |
| 13900002 |
| 14000002 |
| 13900012 |
| 13900031 |
| 13600001 |
| 13900010 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';

let path = "/data/storage/el2/cloud/1.txt";
let uri = fileUri.getUriFromPath(path);
try {
  let state = cloudSync.getCoreFileSyncState(uri);
} catch (err) {
  let error:BusinessError = err as BusinessError;
  console.error(`getCoreFileSyncState failed with error ${error.code}, message is ${error.message}`);
}
```
