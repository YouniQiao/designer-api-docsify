# getSupportedPkids (System API)

## Modules to Import

```TypeScript
```

## getSupportedPkids

```TypeScript
function getSupportedPkids(slotId: number) : Promise<string>
```

Get supported pkids

**Since:** 23

**Required permissions:** ohos.permission.GET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function getSupportedPkids(slotId: int) : Promise<string>--><!--Device-eSIM-function getSupportedPkids(slotId: int) : Promise<string>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |

**Examples**

```TypeScript
import { eSIM } from '@kit.TelephonyKit';

try {
    let supportedPkids: string = await eSIM.getSupportedPkids(1);
    console.info(`supported pkids is:` + supportedPkids);
} catch (err) {
    console.error(`getSupportedPkids, promise: err->${JSON.stringify(err)}`)
}
```
