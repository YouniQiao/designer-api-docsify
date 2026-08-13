# postConversationData (System API)

## Modules to Import

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
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

**Deprecated since:** -1

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

<!--Device-conversation-function postConversationData(    deviceId: string,    bundleName: string,    abilityName: string,    msg: ArrayBuffer  ): Promise<void>--><!--Device-conversation-function postConversationData(    deviceId: string,    bundleName: string,    abilityName: string,    msg: ArrayBuffer  ): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2004004](../../apis-distributedservice-kit/errorcode-conversation.md#2004004-peer-confirmation-timeout) |
| [2004002](../../apis-distributedservice-kit/errorcode-conversation.md#2004002-failed-to-start-the-peer-ability) |
| [2004003](../../apis-distributedservice-kit/errorcode-conversation.md#2004003-failure-to-send-data) |
| [2000001](../../apis-distributedservice-kit/errorcode-conversation.md#2000001-internal-error) |
| [2004001](../../apis-distributedservice-kit/errorcode-conversation.md#2004001-peer-device-system-version-outdated) |

## Examples

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let deviceId: string = 'device_network_id_or_udid'; // deviceId is the network ID or UDID of the target device obtained by calling conversation.getTrustedDevices().
  let bundleName: string = 'com.example.demo';
  let abilityName: string = 'EntryAbility';
  let msg: ArrayBuffer = new ArrayBuffer(10);
  let view = new Uint8Array(msg);
  view[0] = 1;

  conversation.postConversationData(deviceId, bundleName, abilityName, msg).then(() => {
    console.info(`postConversationData success`);
  }).catch((err: BusinessError) => {
    console.error(`postConversationData errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  const e: BusinessError = err as BusinessError;
  console.error(`postConversationData errCode: ${e.code}, errMessage: ${e.message}`);
}
```
