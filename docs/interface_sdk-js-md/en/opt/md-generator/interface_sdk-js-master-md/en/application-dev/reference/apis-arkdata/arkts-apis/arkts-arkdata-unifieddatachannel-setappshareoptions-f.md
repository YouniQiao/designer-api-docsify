# setAppShareOptions

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## setAppShareOptions

```TypeScript
function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void
```

Sets the [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md) for the application data. Currently, only the drag-and-drop data channel is supported.

**Since:** 14

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-unifiedDataChannel-function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void--><!--Device-unifiedDataChannel-function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| intention | [Intention](arkts-arkdata-unifieddatachannel-intention-e.md) | Yes |
| shareOptions | [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [20400001](../errorcode-udmf.md#20400001-settings-already-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  unifiedDataChannel.setAppShareOptions(unifiedDataChannel.Intention.DRAG, unifiedDataChannel.ShareOptions.IN_APP);
  console.info(`[UDMF]setAppShareOptions success.`);
} catch (e) {
  let error: BusinessError = e as BusinessError;
  console.error(`[UDMF]setAppShareOptions throws an exception. code is ${error.code}, message is ${error.message}`);
}
```
