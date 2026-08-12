# batchUpdate

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## batchUpdate

```TypeScript
function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>
```

Updates assets in batches based on an attributes array.

Only assets with the same [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) can be updated in batches.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-asset-function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>--><!--Device-asset-function batchUpdate(sourceAttributes: Array<AssetMap>, destAttributes: Array<AssetMap>): Promise<BatchResult>-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sourceAttributes | Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; | Yes | an array of map objects containing asset attributes to query. &lt;br&gt;The [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) attributes of all assets must be the same. |
| destAttributes | Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt; | Yes | an array of map objects containing asset attributes to be updated. &lt;br&gt;The [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) attributes of all assets must be the same. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[BatchResult](arkts-assetstore-asset-batchresult-i.md)&gt; | the promise object returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24000015](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000015-failed-to-obtain-the-system-time) | Getting the system time failed. |
| [24000012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000012-account-system-service-abnormal) | Calling the OS Account service failed. |
| [24000013](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000013-access-token-service-abnormal) | Calling the Access Token service failed. |
| [24000010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000010-ipc-failed) | IPC failed. |
| [24000011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000011-bundle-manager-service-abnormal) | Calling the Bundle Manager service failed. |
| [24000008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000008-database-operation-failed) | The database operation failed. |
| [24000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000006-insufficient-memory) | Insufficient memory. |
| [24000007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000007-asset-corrupted) | The asset is corrupted. |
| [24000019](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000019-inconsistent-attribute-values) | Each value of [GROUP_ID](arkts-assetstore-asset-tag-e.md#GROUP_ID) and [REQUIRE_ATTR_ENCRYPTED](arkts-assetstore-asset-tag-e.md#REQUIRE_ATTR_ENCRYPTED) in the array is not consistent. |
| [24000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000001-asset-store-service-unavailable) | The ASSET service is unavailable. |

