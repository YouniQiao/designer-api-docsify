# getCallStateSync

## Modules to Import

```TypeScript
```

## getCallStateSync

```TypeScript
function getCallStateSync(): CallState
```

Obtains the call status.

**Since:** 23

<!--Device-call-function getCallStateSync(): CallState--><!--Device-call-function getCallStateSync(): CallState-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CallState](arkts-telephony-call-callstate-e.md) |

**Examples**

```TypeScript
let callState: call.CallState = call.getCallStateSync();
console.info(`the call state is:` + callState);
```
