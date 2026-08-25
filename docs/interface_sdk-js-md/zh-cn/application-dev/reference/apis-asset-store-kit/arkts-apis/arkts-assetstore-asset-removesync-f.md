# removeSync

## 导入模块

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## removeSync

```TypeScript
function removeSync(query: AssetMap): void
```

删除符合条件的一条或多条关键资产，使用同步方式。

**起始版本：** 12

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |
| [24000002](../errorcode-asset.md#24000002-未找到关键资产) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [24000007](../errorcode-asset.md#24000007-关键资产损坏) |
| [24000008](../errorcode-asset.md#24000008-数据库操作失败) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000015](../errorcode-asset.md#24000015-获取系统时间失败) |
