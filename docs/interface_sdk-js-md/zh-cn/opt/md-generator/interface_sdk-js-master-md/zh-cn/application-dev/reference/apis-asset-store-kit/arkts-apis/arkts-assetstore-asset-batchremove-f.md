# batchRemove

## batchRemove

```TypeScript
function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>
```

批量删除符合条件的关键资产。使用Promise异步回调。

批量删除的关键资产必须具有相同的[Tag.GROUP_ID](arkts-assetstore-asset-tagtype-e.md)和[Tag.REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tagtype-e.md)属性。

批量删除的关键资产数量最大值为100。

**起始版本：** 26.0.0

<!--Device-asset-function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>--><!--Device-asset-function batchRemove(assetsToBeRemoved: Array<AssetMap>): Promise<void>-End-->

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetsToBeRemoved | Array&lt;AssetMap&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [24000015](../errorcode-asset.md#24000015-获取系统时间失败) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000008](../errorcode-asset.md#24000008-数据库操作失败) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [24000007](../errorcode-asset.md#24000007-关键资产损坏) |
| [24000019](../errorcode-asset.md#24000019-属性值不一致) |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |

## 示例

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let assetsToBeRemoved: Array<asset.AssetMap> = [];
let query1: asset.AssetMap = new Map();
query1.set(asset.Tag.ALIAS, stringToArray('demo_alias1'));
assetsToBeRemoved.push(query1);

let query2: asset.AssetMap = new Map();
query2.set(asset.Tag.ALIAS, stringToArray('demo_alias2'));
assetsToBeRemoved.push(query2);

asset.batchRemove(assetsToBeRemoved).then(() => {
  console.info(`Succeeded in batch removing Asset.`);
});
```
