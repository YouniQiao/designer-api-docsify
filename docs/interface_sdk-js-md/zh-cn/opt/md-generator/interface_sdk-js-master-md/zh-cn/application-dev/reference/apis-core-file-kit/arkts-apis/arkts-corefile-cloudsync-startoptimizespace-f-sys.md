# startOptimizeSpace（系统接口）

## startOptimizeSpace

```TypeScript
function startOptimizeSpace(optimizePara: OptimizeSpaceParam, callback?: Callback<OptimizeSpaceProgress>): Promise<void>
```

优化图库已同步云空间的本地资源，执行立即优化空间策略，对老化天数前未访问的本地图片/视频进行优化。使用Promise异步回调。callback返回优化进度。

startOptimizeSpace的使用和stopOptimizeSpace方法调用一一对应，重复开启将返回其他任务正在执行的错误信息（22400006）。

**起始版本：** 17

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-cloudSync-function startOptimizeSpace(optimizePara: OptimizeSpaceParam, callback?: Callback<OptimizeSpaceProgress>): Promise<void>--><!--Device-cloudSync-function startOptimizeSpace(optimizePara: OptimizeSpaceParam, callback?: Callback<OptimizeSpaceProgress>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| optimizePara | [OptimizeSpaceParam](arkts-corefile-cloudsync-optimizespaceparam-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OptimizeSpaceProgress&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| 22400005 |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| 22400006 |
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
  } else if (data.state == cloudSync.OptimizeState.COMPLETED && data.progress == 100) {
    console.info("optimize space successfully");
  } else if (data.state == cloudSync.OptimizeState.RUNNING) {
    console.info("optimize space progress: " + data.progress);
  }
}
cloudSync.startOptimizeSpace(para, callback).then(() => {
  console.info("start optimize space");
}).catch((err: BusinessError) => {
  console.error(`start optimize space failed with error message: ${err.message}, error code: ${err.code}`);
});
```
