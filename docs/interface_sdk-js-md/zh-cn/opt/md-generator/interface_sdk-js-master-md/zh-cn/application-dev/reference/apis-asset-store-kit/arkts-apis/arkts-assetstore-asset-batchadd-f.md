# batchAdd

## batchAdd

```TypeScript
function batchAdd(attributesArray: Array<AssetMap>): Promise<BatchResult>
```

批量新增关键资产。使用Promise异步回调。 设置[Tag.IS_PERSISTENT](arkts-assetstore-asset-tagtype-e.md#TagType)属性时，需要申请ohos.permission.STORE_PERSISTENT_DATA权限，申请方式请参考 [声明权限](../../../security/AccessToken/declare-permissions.md)。 批量新增的关键资产必须具有相同的[Tag.GROUP_ID](arkts-assetstore-asset-tagtype-e.md#TagType)和[Tag.REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tagtype-e.md#TagType)属性。 批量新增的关键资产数量最大值为100。

**起始版本：** 26.0.0

**废弃版本：** -1

<!--Device-asset-function batchAdd(attributesArray: Array<AssetMap>): Promise<BatchResult>--><!--Device-asset-function batchAdd(attributesArray: Array<AssetMap>): Promise<BatchResult>-End-->

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attributesArray | Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[BatchResult](arkts-assetstore-asset-batchresult-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [24000014](../errorcode-asset.md#24000014-文件操作失败) |
| [24000015](../errorcode-asset.md#24000015-获取系统时间失败) |
| [24000012](../errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../errorcode-asset.md#24000013-访问控制服务异常) |
| [24000010](../errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../errorcode-asset.md#24000011-包管理服务异常) |
| [24000008](../errorcode-asset.md#24000008-数据库操作失败) |
| [24000009](../errorcode-asset.md#24000009-算法库操作失败) |
| [24000006](../errorcode-asset.md#24000006-系统内存不足) |
| [24000007](../errorcode-asset.md#24000007-关键资产损坏) |
| [24000005](../errorcode-asset.md#24000005-锁屏状态不匹配) |
| [24000001](../errorcode-asset.md#24000001-关键资产服务不可用) |
| [24000019](../errorcode-asset.md#24000019-属性值不一致) |

## 示例

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let attributesArray: Array<asset.AssetMap> = [];
let attr1: asset.AssetMap = new Map();
attr1.set(asset.Tag.SECRET, stringToArray('demo_pwd1'));
attr1.set(asset.Tag.ALIAS, stringToArray('demo_alias1'));
attr1.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attributesArray.push(attr1);

let attr2: asset.AssetMap = new Map();
attr2.set(asset.Tag.SECRET, stringToArray('demo_pwd2'));
attr2.set(asset.Tag.ALIAS, stringToArray('demo_alias2'));
attr2.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attributesArray.push(attr2);

asset.batchAdd(attributesArray).then((res: asset.BatchResult) => {
  console.info(`Succeeded in batch adding Asset, failedCount: ${res.failedCount}`);
});
```
