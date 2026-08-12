# registerConversationListener (System API)

## Modules to Import

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
```

## registerConversationListener

```TypeScript
function registerConversationListener(
    bundleName: string,
    abilityName: string,
    dataCallback: DataCallback
  ): void
```

Registers a listener to receive data from trusted devices under the same account. When the remote device sends data to the local device by calling [postConversationData](arkts-distributedservice-conversation-postconversationdata-f-sys.md#postConversationData), the data is distributed to the registered callback based on the specified bundle name and ability name. Only one listener can be registered for the same bundle name and ability name. Duplicate registration will overwrite the previously registered listener.

**API called in pairs:** This API must be used in pairs with  
[unregisterConversationListener](arkts-distributedservice-conversation-unregisterconversationlistener-f-sys.md#unregisterConversationListener), which is called to unregister the listener to release resources.

**Since:** 26.1.0

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

<!--Device-conversation-function registerConversationListener(    bundleName: string,    abilityName: string,    dataCallback: DataCallback  ): void--><!--Device-conversation-function registerConversationListener(    bundleName: string,    abilityName: string,    dataCallback: DataCallback  ): void-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| abilityName | string | Yes |
| dataCallback | [DataCallback](arkts-distributedservice-conversation-datacallback-t-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [2000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-distributedservice-kit/errorcode-conversation.md#2000001-internal-error) |

## Examples

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName: string = 'com.example.demo';
  let abilityName: string = 'EntryAbility';

  conversation.registerConversationListener(bundleName, abilityName, (deviceId: string, msg: ArrayBuffer) => {
    console.info(`received message, deviceId: ${deviceId}, msg length: ${msg.byteLength}`);
  });
  console.info(`registerConversationListener success`);
} catch (err) {
  const e: BusinessError = err as BusinessError;
  console.error(`registerConversationListener errCode: ${e.code}, errMessage: ${e.message}`);
}
```
