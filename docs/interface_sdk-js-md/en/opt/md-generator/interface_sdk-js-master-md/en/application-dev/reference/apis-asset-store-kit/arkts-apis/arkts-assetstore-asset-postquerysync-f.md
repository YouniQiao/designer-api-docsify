# postQuerySync

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## postQuerySync

```TypeScript
function postQuerySync(handle: AssetMap): void
```

Performs postprocessing for the asset query. This API is used when user authentication is required for the access to the asset. This API must be used with [asset.preQuerySync](arkts-assetstore-asset-prequerysync-f.md#preQuerySync) together. This API returns the result synchronously.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-asset-function postQuerySync(handle: AssetMap): void--><!--Device-asset-function postQuerySync(handle: AssetMap): void-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';

let handle: asset.AssetMap = new Map();
// The new Uint8Array(32) is only an example. Pass in the challenge value returned by asset.preQuerySync.
handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
asset.postQuerySync(handle)
```
