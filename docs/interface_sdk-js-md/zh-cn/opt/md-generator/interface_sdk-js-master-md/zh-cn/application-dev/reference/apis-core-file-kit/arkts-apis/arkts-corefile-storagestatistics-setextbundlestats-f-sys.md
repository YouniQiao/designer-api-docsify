# setExtBundleStats（系统接口）

## setExtBundleStats

```TypeScript
function setExtBundleStats(userId: number, stats: ExtBundleStats): Promise<void>
```

系统应用或系统服务上报自身的空间占用信息。使用Promise异步回调。 > **说明：** > > 入参stats中的flag为false时，businessName必须为某个应用的包名。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.STORAGE_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-storageStatistics-function setExtBundleStats(userId: int, stats: ExtBundleStats): Promise<void>--><!--Device-storageStatistics-function setExtBundleStats(userId: int, stats: ExtBundleStats): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| stats | [ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600011 |
| 13600010 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

## 示例

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
let extBundleStats: storageStatistics.ExtBundleStats = {
  businessName: "com.example.storagedemo",
  size: 10000,
  flag: true
};
storageStatistics.setExtBundleStats(userId, extBundleStats).then(() => {
  console.info("setExtBundleStats successfully");
}).catch((err: BusinessError) => {
  console.error(`setExtBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```
