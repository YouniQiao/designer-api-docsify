# onCallStateChangeEx

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## onCallStateChangeEx

```TypeScript
function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void
```

Callback when the telCall state corresponding to the monitored {@code slotId} is updated.

**Since:** 23

**Deprecated since:** -1

<!--Device-observer-function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void--><!--Device-observer-function onCallStateChangeEx(callback: Callback<TelCallState>, options?: ObserverOptions): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [8800999](../errorcode-telephony.md#8800999-internal-error) |
| [8800002](../errorcode-telephony.md#8800002-service-connection-error) |
| [8800003](../errorcode-telephony.md#8800003-system-internal-error) |
| [8800001](../errorcode-telephony.md#8800001-input-parameter-value-out-of-range) |
