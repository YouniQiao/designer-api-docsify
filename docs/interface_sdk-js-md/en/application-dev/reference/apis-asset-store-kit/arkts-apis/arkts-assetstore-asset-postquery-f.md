# postQuery

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## postQuery

```TypeScript
function postQuery(handle: AssetMap): Promise<void>
```

Performs postprocessing for the asset query. This API is used when user authentication is required for the access to an asset. This API must be used with [asset.preQuery](arkts-assetstore-asset-prequery-f.md) together. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handle | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
