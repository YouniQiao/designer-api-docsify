# getCallStateSync

## getCallStateSync

```TypeScript
function getCallStateSync(): CallState
```

Obtains the call state. If an incoming call is ringing or waiting, the system returns {@code CallState#CALL\_STATE\_RINGING}. If at least one call is in the active, hold, or dialing state, the system returns {@code CallState#CALL\_STATE\_OFFHOOK}. In other cases, the system returns {@code CallState#CALL\_STATE\_IDLE}.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-call-function getCallStateSync(): CallState--><!--Device-call-function getCallStateSync(): CallState-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Returns the call state. |

**Example**

```TypeScript
let callState: call.CallState = call.getCallStateSync();
console.info(`the call state is:` + callState);
```

