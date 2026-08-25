# querySync

## 导入模块

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## querySync

```TypeScript
function querySync(query: AssetMap): Array<AssetMap>
```

查询一条或多条符合条件的关键资产。若查询需要用户认证的关键资产，则需要在本函数前调用[asset.preQuerySync](arkts-assetstore-asset-prequerysync-f.md)，在本函数后调用 [asset.postQuerySync](arkts-assetstore-asset-postquerysync-f.md)，开发步骤请参考 [开发指导](../../../security/AssetStoreKit/asset-js-query-auth.md)。使用同步方式返回结果。如果未查询到符合条件的关键资产，将抛出“未找到关键资产”的异常，而非返回空的查询结果列表。

**起始版本：** 12

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |
| [24000002](../errorcode-asset.md#24000002-未找到关键资产) |
| [24000004](../errorcode-asset.md#24000004-访问被拒绝) |
| [24000005](../errorcode-asset.md#24000005-锁屏状态不匹配) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [24000007](../errorcode-asset.md#24000007-关键资产损坏) |
| [24000008](../errorcode-asset.md#24000008-数据库操作失败) |
| [24000009](../errorcode-asset.md#24000009-算法库操作失败) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000017](../errorcode-asset.md#24000017-该子功能不支持) |
