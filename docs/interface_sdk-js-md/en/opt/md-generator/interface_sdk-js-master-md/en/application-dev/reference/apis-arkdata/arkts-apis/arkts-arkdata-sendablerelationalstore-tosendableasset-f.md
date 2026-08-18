# toSendableAsset

## Modules to Import

```TypeScript
```

## toSendableAsset

```TypeScript
function toSendableAsset(asset: NonSendableAsset): Asset
```

Converts the asset data that cannot be passed across threads into the data that can be passed across threads.

**Since:** 12

<!--Device-sendableRelationalStore-function toSendableAsset(asset: NonSendableAsset): Asset--><!--Device-sendableRelationalStore-function toSendableAsset(asset: NonSendableAsset): Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [asset](../../apis-asset-store-kit/arkts-apis/arkts-security-asset.md) | [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Asset](arkts-arkdata-commontype-asset-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |

**Examples**

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
```
