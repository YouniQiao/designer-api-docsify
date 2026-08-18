# getDefaultVoiceSimId

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## getDefaultVoiceSimId

```TypeScript
function getDefaultVoiceSimId(callback: AsyncCallback<int>): void
```

Obtains the default SIM ID for the voice service.

**Since:** 23

<!--Device-sim-function getDefaultVoiceSimId(callback: AsyncCallback<int>): void--><!--Device-sim-function getDefaultVoiceSimId(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Returns the SIM ID of the default voice sim and SIM ID will increase from 1. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8301001](../errorcode-telephony.md#8301001-sim-card-not-activated) | SIM card is not activated. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSimId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getDefaultVoiceSimId

```TypeScript
function getDefaultVoiceSimId(): Promise<int>
```

Obtains the default SIM ID for the voice service.

**Since:** 23

<!--Device-sim-function getDefaultVoiceSimId(): Promise<int>--><!--Device-sim-function getDefaultVoiceSimId(): Promise<int>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Returns the SIM ID of the default voice sim and SIM ID will increase from 1. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [8301001](../errorcode-telephony.md#8301001-sim-card-not-activated) | SIM card is not activated. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300004](../errorcode-telephony.md#8300004-sim-card-not-detected) | No SIM card found. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let promise = sim.getDefaultVoiceSimId();
promise.then((data: number) => {
    console.info(`getDefaultVoiceSimId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultVoiceSimId failed, promise: err->${JSON.stringify(err)}`);
});
```

