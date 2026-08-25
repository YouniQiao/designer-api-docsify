# batchRemove

## 导入模块

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## batchRemove

```TypeScript
function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>
```

批量删除符合条件的关键资产。使用Promise异步回调。批量删除的关键资产必须具有相同的[Tag.GROUP_ID](arkts-assetstore-asset-tagtype-e.md)和[Tag.REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tagtype-e.md)属性。批量删除的关键资产数量最大值为100。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetsToBeRemoved | Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [24000007](../errorcode-asset.md#24000007-关键资产损坏) |
| [24000008](../errorcode-asset.md#24000008-数据库操作失败) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000015](../errorcode-asset.md#24000015-获取系统时间失败) |
| [24000019](../errorcode-asset.md#24000019-属性值不一致) |
