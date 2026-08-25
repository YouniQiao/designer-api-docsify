# getAllExtBundleStats（系统接口）

## 导入模块

```TypeScript
import { storageStatistics } from 'kits/@kit.CoreFileKit';
```

## getAllExtBundleStats

```TypeScript
function getAllExtBundleStats(userId: number): Promise<Array<ExtBundleStats>>
```

获取指定用户下所有系统应用或系统服务的空间占用详情。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.STORAGE_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ExtBundleStats](arkts-corefile-storagestatistics-extbundlestats-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13600010 |
| 13600013 |
