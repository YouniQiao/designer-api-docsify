# stopRtt (System API)

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## stopRtt

```TypeScript
function stopRtt(callId: number, type: ImsRttMode): Promise<void>
```

Stop rtt.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.PLACE_CALL

<!--Device-call-function stopRtt(callId: int, type: ImsRttMode): Promise<void>--><!--Device-call-function stopRtt(callId: int, type: ImsRttMode): Promise<void>-End-->

**System capability:** SystemCapability.Telephony.CallManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callId | number | Yes |
| type | [ImsRttMode](arkts-telephony-call-imsrttmode-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
