# queryAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## queryAsUser

```TypeScript
function queryAsUser(userId: number, query: AssetMap): Promise<Array<AssetMap>>
```

Queries one or more assets in the specified user space. If user authentication is required for the access to the asset, call [asset.preQueryAsUser](arkts-assetstore-asset-prequeryasuser-f-sys.md#preQueryAsUser-(System-API)) before this API and call [asset.postQueryAsUser](arkts-assetstore-asset-postqueryasuser-f-sys.md#postQueryAsUser-(System-API)) after this API. For details about the development procedure, see [Development Guidance](../../../security/AssetStoreKit/asset-js-query-auth.md). This API uses a promise to return the result.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function queryAsUser(userId: number, query: AssetMap): Promise<Array<AssetMap>>--><!--Device-asset-function queryAsUser(userId: number, query: AssetMap): Promise<Array<AssetMap>>-End-->

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| userId | number | Yes |
| query | [AssetMap](arkts-assetstore-asset-assetmap-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AssetMap](arkts-assetstore-asset-assetmap-t.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [24000012](../errorcode-asset.md#24000012-account-system-service-abnormal) |
| [24000013](../errorcode-asset.md#24000013-access-token-service-abnormal) |
| [24000010](../errorcode-asset.md#24000010-ipc-failed) |
| [24000011](../errorcode-asset.md#24000011-bundle-manager-service-abnormal) |
| [24000008](../errorcode-asset.md#24000008-database-operation-failed) |
| [24000009](../errorcode-asset.md#24000009-cryptographic-operation-failed) |
| [24000006](../errorcode-asset.md#24000006-insufficient-memory) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [24000004](../errorcode-asset.md#24000004-access-denied) |
| [24000005](../errorcode-asset.md#24000005-incorrect-screen-lock-status) |
| [24000002](../errorcode-asset.md#24000002-asset-not-found) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [24000017](../errorcode-asset.md#24000017-function-not-supported) |

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
asset.queryAsUser(userId, query).then((res: Array<asset.AssetMap>) => {
  for (let i = 0; i < res.length; i++) {
    // Parse the attributes.
    let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
    console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
  }
  console.info(`Succeeded in querying Asset from user space.`);
});
```
