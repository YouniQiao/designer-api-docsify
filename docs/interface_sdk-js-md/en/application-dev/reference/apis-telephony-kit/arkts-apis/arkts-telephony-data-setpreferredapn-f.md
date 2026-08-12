# setPreferredApn

## Modules to Import

```TypeScript
import { data } from '@kit.TelephonyKit';
```

## setPreferredApn

```TypeScript
function setPreferredApn(apnId: int): Promise<boolean>
```

Set preferred APN.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_APN_SETTING

<!--Device-data-function setPreferredApn(apnId: int): Promise<boolean>--><!--Device-data-function setPreferredApn(apnId: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Telephony.CellularData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| apnId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The APN ID which is used to be set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |

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

