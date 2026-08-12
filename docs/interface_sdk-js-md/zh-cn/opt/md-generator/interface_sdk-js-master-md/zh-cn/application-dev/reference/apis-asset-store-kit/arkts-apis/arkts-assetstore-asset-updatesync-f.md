# updateSync

## updateSync

```TypeScript
function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void
```

更新符合条件的一条关键资产，使用同步方式返回结果。

**起始版本：** 12

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-asset-function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void--><!--Device-asset-function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void-End-->

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 |
| attributesToUpdate | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [24000015](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000015-获取系统时间失败) |
| [24000012](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000012-账号系统服务异常) |
| [24000013](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000013-访问控制服务异常) |
| [24000010](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000010-进程通信错误) |
| [24000011](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000011-包管理服务异常) |
| [24000008](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000008-数据库操作失败) |
| [24000009](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000009-算法库操作失败) |
| [24000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000006-系统内存不足) |
| [24000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000007-关键资产损坏) |
| [24000005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000005-锁屏状态不匹配) |
| [24000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000002-未找到关键资产) |
| [24000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000001-关键资产服务不可用) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## 示例

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
asset.updateSync(query, attrsToUpdate);
```
