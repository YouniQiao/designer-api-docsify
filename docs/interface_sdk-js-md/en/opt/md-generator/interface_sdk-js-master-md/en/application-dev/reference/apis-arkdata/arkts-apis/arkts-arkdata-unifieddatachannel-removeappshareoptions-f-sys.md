# removeAppShareOptions (System API)

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## removeAppShareOptions

```TypeScript
function removeAppShareOptions(intention: Intention): void
```

Removes the data control information set by [setAppShareOptions](arkts-arkdata-unifieddatachannel-setappshareoptions-f-sys.md#setAppShareOptions-(System-API)).

**Since:** 23

**Deprecated since:** -1

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-unifiedDataChannel-function removeAppShareOptions(intention: Intention): void--><!--Device-unifiedDataChannel-function removeAppShareOptions(intention: Intention): void-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [intention](arkts-arkdata-unifieddatachannel-options-i.md) | [Intention](arkts-arkdata-unifieddatachannel-intention-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  unifiedDataChannel.removeAppShareOptions(unifiedDataChannel.Intention.DRAG);
  console.info(`[UDMF]removeAppShareOptions success.`);
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`[UDMF]removeAppShareOptions throws an exception. code is ${error.code}, message is ${error.message}`);
}
```
