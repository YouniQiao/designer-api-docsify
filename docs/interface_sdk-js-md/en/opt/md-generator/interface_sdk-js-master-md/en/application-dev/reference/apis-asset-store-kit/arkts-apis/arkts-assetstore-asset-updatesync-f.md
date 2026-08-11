# updateSync

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## updateSync

```TypeScript
function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void
```

Updates an asset. This API returns the result synchronously.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void--><!--Device-asset-function updateSync(query: AssetMap, attributesToUpdate: AssetMap): void-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |
| attributesToUpdate | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [24000015](../errorcode-asset.md#24000015-failed-to-obtain-the-system-time) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [24000005](../errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000002](../errorcode-asset.md#24000002-asset-not-found) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

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
