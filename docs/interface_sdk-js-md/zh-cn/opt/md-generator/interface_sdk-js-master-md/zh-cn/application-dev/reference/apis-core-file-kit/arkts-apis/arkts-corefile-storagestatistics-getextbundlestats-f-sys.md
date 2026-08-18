# getExtBundleStats（系统接口）

## 导入模块

```TypeScript
```

## getExtBundleStats

```TypeScript
function getExtBundleStats(userId: number, businessName: string): Promise<ExtBundleStats>
```

获取指定用户、指定系统应用包名或系统服务名称的空间占用详情。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-storageStatistics-function getExtBundleStats(userId: int, businessName: string): Promise<ExtBundleStats>--><!--Device-storageStatistics-function getExtBundleStats(userId: int, businessName: string): Promise<ExtBundleStats>-End-->

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| [businessName](arkts-corefile-storagestatistics-extbundlestats-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600012 |
| 13600010 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |

**示例**

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let userId: number = 100;
let businessName: string = "com.example.storagedemo";
storageStatistics.getExtBundleStats(userId, businessName).then((bundleStats: storageStatistics.ExtBundleStats) => {
  console.info("getExtBundleStats successfully.");
}).catch((err: BusinessError) => {
  console.error(`getExtBundleStats failed with err, code is: ${err.code}, message is: ${err.message}`);
});
```
