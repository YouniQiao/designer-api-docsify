# offCommunicationStateChange

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## offCommunicationStateChange

```TypeScript
function offCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void
```

Unsubscribes from the callback for listening to the 5A state.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-observer-function offCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void--><!--Device-observer-function offCommunicationStateChange(callback: Callback<boolean>, options?: ObserverOptions): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
