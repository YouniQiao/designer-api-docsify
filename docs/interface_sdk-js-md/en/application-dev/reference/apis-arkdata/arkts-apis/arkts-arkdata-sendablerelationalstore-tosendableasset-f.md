# toSendableAsset

## Modules to Import

```TypeScript
import { sendableRelationalStore } from 'kits/@kit.ArkData';
```

## toSendableAsset

```TypeScript
function toSendableAsset(asset: NonSendableAsset): Asset
```

Converts the asset data that cannot be passed across threads into the data that can be passed across threads.

**Since:** 12

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [asset](../../apis-asset-store-kit/arkts-apis/arkts-security-asset.md) | [NonSendableAsset](arkts-arkdata-sendablerelationalstore-nonsendableasset-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Asset](arkts-arkdata-sendablerelationalstore-asset-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [14800000](../errorcode-data-rdb.md#14800000-internal-error) |
