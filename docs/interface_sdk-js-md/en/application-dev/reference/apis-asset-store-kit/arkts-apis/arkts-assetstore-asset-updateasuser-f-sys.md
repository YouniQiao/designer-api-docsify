# updateAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## updateAsUser

```TypeScript
function updateAsUser(userId: number, query: AssetMap, attributesToUpdate: AssetMap): Promise<void>
```

Updates an asset in the specified user space. This API uses a promise to return the result.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function updateAsUser(userId: number, query: AssetMap, attributesToUpdate: AssetMap): Promise<void>--><!--Device-asset-function updateAsUser(userId: number, query: AssetMap, attributesToUpdate: AssetMap): Promise<void>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | the user identifier to update an Asset. The value must be greater than or equal to 100. |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | Attributes of the asset to update, such as the asset alias, access control attributes, and custom data. |
| attributesToUpdate | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes | New attributes of the asset, such as the asset plaintext and custom data. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24000015](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000015-failed-to-obtain-the-system-time) | Getting the system time failed. |
| [24000012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000012-account-system-service-abnormal) | Calling the OS Account service failed. |
| [24000013](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000013-access-token-service-abnormal) | Calling the Access Token service failed. |
| [24000010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000010-ipc-failed) | IPC failed. |
| [24000011](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000011-bundle-manager-service-abnormal) | Calling the Bundle Manager service failed. |
| [24000008](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000008-database-operation-failed) | The database operation failed. |
| [24000009](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000009-cryptographic-operation-failed) | The cryptography operation failed. |
| [24000006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000006-insufficient-memory) | Insufficient memory. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | The caller doesn't have the permission. |
| [24000007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000007-asset-corrupted) | The asset is corrupted. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [24000005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000005-incorrect-screen-lock-status) | The screen lock status does not match. |
| [24000002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000002-asset-not-found) | The asset is not found. |
| [24000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-asset-store-kit/errorcode-asset.md#24000001-asset-store-service-unavailable) | The ASSET service is unavailable. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |

## Examples

```TypeScript
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let userId: number = 100;
let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
asset.updateAsUser(userId, query, attrsToUpdate).then(() => {
  console.info(`Succeeded in updating Asset in user space.`);
});
```

