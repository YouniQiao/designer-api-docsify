# getCallState

## getCallState

```TypeScript
function getCallState(callback: AsyncCallback<CallState>): void
```

Obtains the call state. If an incoming call is ringing or waiting, the system returns {@code CallState#CALL\_STATE\_RINGING}. If at least one call is in the active, hold, or dialing state, the system returns {@code CallState#CALL\_STATE\_OFFHOOK}. In other cases, the system returns {@code CallState#CALL\_STATE\_IDLE}.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-call-function getCallState(callback: AsyncCallback<CallState>): void--><!--Device-call-function getCallState(callback: AsyncCallback<CallState>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;CallState&gt; | Yes | Indicates the callback for getting the call state. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallState((err: BusinessError, data: call.CallState) => {
    if (err) {
        console.error(`getCallState fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`getCallState success, data->${JSON.stringify(data)}`);
    }
});
```


## getCallState

```TypeScript
function getCallState(): Promise<CallState>
```

Obtains the call state. If an incoming call is ringing or waiting, the system returns {@code CallState#CALL\_STATE\_RINGING}. If at least one call is in the active, hold, or dialing state, the system returns {@code CallState#CALL\_STATE\_OFFHOOK}. In other cases, the system returns {@code CallState#CALL\_STATE\_IDLE}.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-call-function getCallState(): Promise<CallState>--><!--Device-call-function getCallState(): Promise<CallState>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CallState&gt; | Returns the call state. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallState().then((data: call.CallState) => {
    console.info(`getCallState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCallState fail, promise: err->${JSON.stringify(err)}`);
});
```

