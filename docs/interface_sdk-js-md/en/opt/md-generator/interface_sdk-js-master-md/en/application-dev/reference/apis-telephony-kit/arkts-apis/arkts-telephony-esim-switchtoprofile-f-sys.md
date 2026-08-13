# switchToProfile (System API)

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## switchToProfile

```TypeScript
function switchToProfile(slotId: number, portIndex: number, iccid: string,
                           forceDisableProfile: boolean): Promise<ResultCode>
```

Switch to (enable) the given profile on the eUICC.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function switchToProfile(slotId: int, portIndex: int, iccid: string,                           forceDisableProfile: boolean): Promise<ResultCode>--><!--Device-eSIM-function switchToProfile(slotId: int, portIndex: int, iccid: string,                           forceDisableProfile: boolean): Promise<ResultCode>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |
| portIndex | number | Yes |
| iccid | string | Yes |
| [forceDisableProfile](arkts-telephony-esim-downloadconfiguration-i-sys.md) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;ResultCode & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3120002](../errorcode-telephony.md#3120002-system-internal-error) |
| [3120001](../errorcode-telephony.md#3120001-service-connection-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.switchToProfile(1, 0, 'testId', true).then(() => {
    console.info(`switchToProfile invoking succeeded.`);
}).catch((err: BusinessError<void>) => {
    console.error(`switchToProfile, ErrorState: err->${JSON.stringify(err)}`);
});
```
