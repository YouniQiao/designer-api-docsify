# getAllExtBundleStats（系统接口）

## getAllExtBundleStats

```TypeScript
function getAllExtBundleStats(userId: number): Promise<Array<ExtBundleStats>>
```

获取指定用户下所有系统应用或系统服务的空间占用详情。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-storageStatistics-function getAllExtBundleStats(userId: int): Promise<Array<ExtBundleStats>>--><!--Device-storageStatistics-function getAllExtBundleStats(userId: int): Promise<Array<ExtBundleStats>>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;ExtBundleStats&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600013 |
| 13600010 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

## 示例

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
storageStatistics.getAllExtBundleStats(userId).then((bundleStatsList: storageStatistics.ExtBundleStats[]) => {
  console.info("getAllExtBundleStats successfully");
}).catch((err: BusinessError) => {
  console.error(`getAllExtBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```
