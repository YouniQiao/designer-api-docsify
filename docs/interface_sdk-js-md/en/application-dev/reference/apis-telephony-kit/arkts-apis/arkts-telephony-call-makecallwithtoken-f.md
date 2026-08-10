# makeCallWithToken

## Modules to Import

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## makeCallWithToken

```TypeScript
function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>
```

Go to the dial screen and the called number is displayed.The authentication challenge value is returned.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-call-function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>--><!--Device-call-function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| phoneNumber | string | Yes | Indicates the called number. |
| options | [MakeCallOptions](arkts-telephony-call-makecalloptions-i.md) | No | Indicates additional information carried in the call. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return access token by the makeCall. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 8300999 | Unknown error code. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

