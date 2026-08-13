# getCallStateSync

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## getCallStateSync

```TypeScript
function getCallStateSync(): CallState
```

Obtains the call status.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-call-function getCallStateSync(): CallState--><!--Device-call-function getCallStateSync(): CallState-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| Type | Description |
| --- | --- |
| CallState | Promise used to return the result. |

## Examples

```TypeScript
let callState: call.CallState = call.getCallStateSync();
console.info(`the call state is:` + callState);
```

