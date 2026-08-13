# setPreferredApn

## Modules to Import

```TypeScript
import { data } from '@kit.TelephonyKit';
```

## setPreferredApn

```TypeScript
function setPreferredApn(apnId: number): Promise<boolean>
```

Set preferred APN.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_APN_SETTING

<!--Device-data-function setPreferredApn(apnId: int): Promise<boolean>--><!--Device-data-function setPreferredApn(apnId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| apnId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let apnId: number = 0; // apnId is a valid value returned by queryApnIds. If an invalid APN ID is passed to setPreferredApn, the default preferred APN configured by the carrier is used.
data.setPreferredApn(apnId).then((result: boolean) => {
    console.info(`setPreferredApn result: ${result}`);
}).catch((err: BusinessError) => {
    console.error(`setPreferredApn failed. code: ${err.code}, message: ${err.message}`);
});
```
