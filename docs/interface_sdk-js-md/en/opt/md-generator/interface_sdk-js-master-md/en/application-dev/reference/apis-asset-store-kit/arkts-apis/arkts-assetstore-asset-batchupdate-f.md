# batchUpdate

## Modules to Import

```TypeScript
import { asset } from 'kits/@kit.AssetStoreKit';
```

## batchUpdate

```TypeScript
function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>
```

Updates assets in batches based on an attributes array.

Only assets with the same {@link Tag.GROUP_ID} and {@link Tag.REQUIRE_ATTR_ENCRYPTED} can be updated in batches.

**Since:** 26.0.0

<!--Device-asset-function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>--><!--Device-asset-function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceAttributes | Array&lt;AssetMap&gt; | Yes |
| destAttributes | Array&lt;AssetMap&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;BatchResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000015](../errorcode-asset.md#24000015-failed-to-obtain-the-system-time) |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [24000019](../errorcode-asset.md#24000019-inconsistent-attribute-values) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
