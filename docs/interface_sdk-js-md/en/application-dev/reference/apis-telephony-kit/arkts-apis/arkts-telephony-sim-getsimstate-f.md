# getSimState

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## getSimState

```TypeScript
function getSimState(slotId: int, callback: AsyncCallback<SimState>): void
```

Obtains the state of the SIM card in a specified slot.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-sim-function getSimState(slotId: int, callback: AsyncCallback<SimState>): void--><!--Device-sim-function getSimState(slotId: int, callback: AsyncCallback<SimState>): void-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from {@code 0} to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;SimState&gt; | Yes | Indicates the callback for getting one of the following SIM card states: &lt;ul&gt; &lt;li&gt;{@code SimState#SIM_STATE_UNKNOWN} &lt;li&gt;{@code SimState#SIM_STATE_NOT_PRESENT} &lt;li&gt;{@code SimState#SIM_STATE_LOCKED} &lt;li&gt;{@code SimState#SIM_STATE_NOT_READY} &lt;li&gt;{@code SimState#SIM_STATE_READY} &lt;li&gt;{@code SimState#SIM_STATE_LOADED} &lt;/ul&gt; |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0, (err: BusinessError, data: sim.SimState) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```


## getSimState

```TypeScript
function getSimState(slotId: int): Promise<SimState>
```

Obtains the state of the SIM card in a specified slot.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-sim-function getSimState(slotId: int): Promise<SimState>--><!--Device-sim-function getSimState(slotId: int): Promise<SimState>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the card slot index number, ranging from {@code 0} to the maximum card slot index number supported by the device. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SimState&gt; | Returns one of the following SIM card states: &lt;ul&gt; &lt;li&gt;{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0).then((data: sim.SimState) => {
    console.info(`getSimState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimState failed, promise: err->${JSON.stringify(err)}`);
});
```

