# postConversationData (System API)

## Modules to Import

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## postConversationData

```TypeScript
function postConversationData(
    deviceId: string,
    bundleName: string,
    abilityName: string,
    msg: ArrayBuffer
  ): Promise<void>
```

Sends session data to the target device. The target device must be a trusted device under the same account. The network ID or UDID of the target device is used for device addressing. Data is sent to the app with the registered listener on the target device based on the specified bundle name and ability name. Typical use scenarios include sending collaboration commands across devices.

**Since:** 26.1.0

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| bundleName | string | Yes |
| abilityName | string | Yes |
| msg | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2000001](../errorcode-conversation.md#2000001-internal-error) |
| [2004001](../errorcode-conversation.md#2004001-peer-device-system-version-outdated) |
| [2004002](../errorcode-conversation.md#2004002-failed-to-start-the-peer-ability) |
| [2004003](../errorcode-conversation.md#2004003-failure-to-send-data) |
| [2004004](../errorcode-conversation.md#2004004-peer-confirmation-timeout) |
