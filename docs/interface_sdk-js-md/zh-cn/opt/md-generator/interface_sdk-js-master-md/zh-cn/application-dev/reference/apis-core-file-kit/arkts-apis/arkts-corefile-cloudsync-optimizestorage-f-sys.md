# optimizeStorage（系统接口）

## optimizeStorage

```TypeScript
function optimizeStorage():Promise<void>
```

优化图库已同步云空间的本地资源，按照本地剩余空间执行自动老化策略。使用Promise异步回调。

**起始版本：** 17

**需要权限：** ohos.permission.CLOUDFILE_SYNC

<!--Device-cloudSync-function optimizeStorage():Promise<void>--><!--Device-cloudSync-function optimizeStorage():Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudSync.optimizeStorage().then(() => {
  console.info("optimize storage successfully");   // 前台UX按需阻塞等待
}).catch((err: BusinessError) => {
  console.error(`optimize storage failed with error message: ${err.message}, error code: ${err.code}`);
});
```
