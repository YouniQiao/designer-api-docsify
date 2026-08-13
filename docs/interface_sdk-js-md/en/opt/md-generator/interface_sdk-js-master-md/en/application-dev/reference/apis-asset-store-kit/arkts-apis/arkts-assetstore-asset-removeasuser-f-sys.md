# removeAsUser (System API)

## Modules to Import

```TypeScript
import { asset } from '@kit.AssetStoreKit';
```

## removeAsUser

```TypeScript
function removeAsUser(userId: number, query: AssetMap): Promise<void>
```

Removes one or more assets in the specified user space. This API uses a promise to return the result.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS

<!--Device-asset-function removeAsUser(userId: number, query: AssetMap): Promise<void>--><!--Device-asset-function removeAsUser(userId: number, query: AssetMap): Promise<void>-End-->

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
| Promise & lt;void & gt; |

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [24000007](../errorcode-asset.md#24000007-asset-corrupted) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [24000002](../errorcode-asset.md#24000002-asset-not-found) |
| [24000001](../errorcode-asset.md#24000001-asset-store-service-unavailable) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

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
asset.removeAsUser(userId, query).then(() => {
  console.info(`Succeeded in removing Asset from user space.`);
});
```
