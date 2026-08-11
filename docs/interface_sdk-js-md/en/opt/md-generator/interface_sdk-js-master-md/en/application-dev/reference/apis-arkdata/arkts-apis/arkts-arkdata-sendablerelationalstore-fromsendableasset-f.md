# fromSendableAsset

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## fromSendableAsset

```TypeScript
function fromSendableAsset(asset: Asset): NonSendableAsset
```

Converts the asset data that can be passed across threads into the data that cannot be passed across threads.

**Since:** 12

<!--Device-sendableRelationalStore-function fromSendableAsset(asset: Asset): NonSendableAsset--><!--Device-sendableRelationalStore-function fromSendableAsset(asset: Asset): NonSendableAsset-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| asset | [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [14800000](../../apis-basic-services-kit/errorcode-settings.md#14800000-parameter-check-failed) |

## Examples

```TypeScript
const asset1: sendableRelationalStore.NonSendableAsset = {
  name: 'hangman',
  uri: '//path/example',
  path: '//path/example',
  createTime: 'createTime1',
  modifyTime: 'modifyTime1',
  size: 'size1'
};
const sendableAsset = sendableRelationalStore.toSendableAsset(asset1);
const normalAsset = sendableRelationalStore.fromSendableAsset(sendableAsset);
```
