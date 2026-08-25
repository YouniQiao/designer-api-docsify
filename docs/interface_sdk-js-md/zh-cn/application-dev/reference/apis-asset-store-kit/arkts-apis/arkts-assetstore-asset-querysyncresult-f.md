# querySyncResult

## 导入模块

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## querySyncResult

```TypeScript
function querySyncResult(query: AssetMap): Promise<SyncResult>
```

执行同步操作后，查询同步执行结果。使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SyncResult & gt; |

**错误码：**

| 错误码ID |
| --- |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000014](../errorcode-asset.md#24000014-文件操作失败) |
| [24000018](../errorcode-asset.md#24000018-参数校验失败) |
