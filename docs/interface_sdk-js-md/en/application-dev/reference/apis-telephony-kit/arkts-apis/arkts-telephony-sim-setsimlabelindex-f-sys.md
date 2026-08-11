# setSimLabelIndex (System API)

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## setSimLabelIndex

```TypeScript
function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>
```

Set the SIM card labelIndex.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>--><!--Device-sim-function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CoreService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| simId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the sim Id for card from sim account information. &lt;br&gt;Value range:[1,500] |
| simLabelIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the simlabel index for card. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the setSimLabelIndex. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error code. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Nonsystem applications use system APIs. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

