# hasSmsCapability

## Modules to Import

```TypeScript
import { sms } from '@kit.TelephonyKit';
```

## hasSmsCapability

```TypeScript
function hasSmsCapability(): boolean
```

Checks whether the current device can send and receive SMS messages. This API works in synchronous mode.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-sms-function hasSmsCapability(): boolean--><!--Device-sms-function hasSmsCapability(): boolean-End-->

**System capability:** SystemCapability.Telephony.SmsMms

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true**: The device can send and receive SMS messages. &lt;br&gt;- **false**: The device cannot send or receive SMS messages. |

