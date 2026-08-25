# setAppShareOptions

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## setAppShareOptions

```TypeScript
function setAppShareOptions(intention: Intention, shareOptions: ShareOptions): void
```

Sets the [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md) for the application data. Currently, only the drag- and-drop data channel is supported.

**Since:** 14

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [intention](arkts-arkdata-unifieddatachannel-options-i.md) | [Intention](arkts-arkdata-unifieddatachannel-intention-e.md) | Yes |
| [shareOptions](arkts-arkdata-unifieddatachannel-unifieddataproperties-c.md) | [ShareOptions](arkts-arkdata-unifieddatachannel-shareoptions-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [20400001](../errorcode-udmf.md#20400001-settings-already-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
