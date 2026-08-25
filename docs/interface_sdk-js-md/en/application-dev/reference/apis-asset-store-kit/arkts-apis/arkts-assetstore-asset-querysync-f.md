# querySync

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## querySync

```TypeScript
function querySync(query: AssetMap): Array<AssetMap>
```

Queries one or more assets. If user authentication is required for the access to the asset, call [asset.preQuerySync](arkts-assetstore-asset-prequerysync-f.md) before this API and call [asset.postQuerySync](arkts-assetstore-asset-postquerysync-f.md) after this API. For details about the development procedure, see [Development Guidance](../../../security/AssetStoreKit/asset-js-query-auth.md). This API returns the result synchronously.If no asset is found, an exception indicating that no asset is found is thrown instead of returning an empty query result list.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [24000002](../errorcode-asset.md#24000002-asset-not-found) |
| [24000004](../errorcode-asset.md#24000004-access-denied) |
| [24000005](../errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000017](../errorcode-asset.md#24000017-function-not-supported) |
