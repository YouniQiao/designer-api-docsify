# removeSync

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## removeSync

```TypeScript
function removeSync(query: AssetMap): void
```

Removes one or more assets. This API returns the result synchronously.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function removeSync(query: AssetMap): void--><!--Device-asset-function removeSync(query: AssetMap): void-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24000015](../errorcode-asset.md#24000015-failed-to-obtain-the-system-time) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [24000002](../errorcode-asset.md#24000002-asset-not-found) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |

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
asset.removeSync(query);
```
