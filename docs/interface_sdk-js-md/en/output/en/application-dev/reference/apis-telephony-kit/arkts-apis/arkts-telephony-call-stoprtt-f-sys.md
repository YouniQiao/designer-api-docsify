# stopRtt (System API)

## stopRtt

```TypeScript
function stopRtt(callId: int, type: ImsRttMode): Promise<void>
```

Stop rtt.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function stopRtt(callId: int, type: ImsRttMode): Promise<void>--><!--Device-call-function stopRtt(callId: int, type: ImsRttMode): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Indicates the identifier of the call. |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the type of operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the stopRtt. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |

