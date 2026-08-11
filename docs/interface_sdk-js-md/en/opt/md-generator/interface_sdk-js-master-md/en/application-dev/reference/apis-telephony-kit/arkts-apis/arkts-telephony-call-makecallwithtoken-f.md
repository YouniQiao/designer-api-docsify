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

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-call-function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>--><!--Device-call-function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| phoneNumber | string | Yes |
| options | [MakeCallOptions](arkts-telephony-call-makecalloptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
