# getCallState

## Modules to Import

```TypeScript
import { call } from 'call';
```

## getCallState

```TypeScript
function getCallState(callback: AsyncCallback<CallState>): void
```

Obtains the call status. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-call-function getCallState(callback: AsyncCallback<CallState>): void--><!--Device-call-function getCallState(callback: AsyncCallback<CallState>): void-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;CallState&gt; | Yes | Callback used to return the result. |

## Examples

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

Obtains the call status. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-call-function getCallState(): Promise<CallState>--><!--Device-call-function getCallState(): Promise<CallState>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CallState&gt; | Promise used to return the result. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallState().then((data: call.CallState) => {
    console.info(`getCallState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCallState fail, promise: err->${JSON.stringify(err)}`);
});
```

