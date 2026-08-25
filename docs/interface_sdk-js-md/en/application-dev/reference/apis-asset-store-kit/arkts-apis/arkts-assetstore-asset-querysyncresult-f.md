# querySyncResult

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## querySyncResult

```TypeScript
function querySyncResult(query: AssetMap): Promise<SyncResult>
```

Queries the result of the sync operation. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SyncResult & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000014](../errorcode-asset.md#24000014-file-operation-failed) |
| [24000018](../errorcode-asset.md#24000018-parameter-check-failed) |
