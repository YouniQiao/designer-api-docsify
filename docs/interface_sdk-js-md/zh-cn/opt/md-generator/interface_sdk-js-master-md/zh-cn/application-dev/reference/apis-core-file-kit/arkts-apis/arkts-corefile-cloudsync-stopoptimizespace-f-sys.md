# stopOptimizeSpace（系统接口）

## stopOptimizeSpace

```TypeScript
function stopOptimizeSpace(): void
```

同步方法停止图库云图资源空间优化，和startOptimizeSpace配对使用。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-cloudSync-function stopOptimizeSpace(): void--><!--Device-cloudSync-function stopOptimizeSpace(): void-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| 22400005 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let para:cloudSync.OptimizeSpaceParam = {totalSize: 1073741824, agingDays: 30};
let callback = (data:cloudSync.OptimizeSpaceProgress) => {
  if (data.state == cloudSync.OptimizeState.FAILED) {
    console.info("optimize space failed");
  } else if (data.state == cloudSync.OptimizeState.RUNNING) {
    console.info("optimize space progress: " + data.progress);
  }
}
cloudSync.startOptimizeSpace(para, callback);
cloudSync.stopOptimizeSpace();   // 停止空间优化
```
