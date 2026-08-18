# reserveProfilesForFactoryRestore (System API)

## Modules to Import

```TypeScript
```

## reserveProfilesForFactoryRestore

```TypeScript
function reserveProfilesForFactoryRestore(slotId: number): Promise<ResultCode>
```

Ensure that profiles will be retained on the next factory reset.

**Since:** 23

**Required permissions:** ohos.permission.SET_TELEPHONY_ESIM_STATE

<!--Device-eSIM-function reserveProfilesForFactoryRestore(slotId: int): Promise<ResultCode>--><!--Device-eSIM-function reserveProfilesForFactoryRestore(slotId: int): Promise<ResultCode>-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slotId | number | Yes |

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

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

eSIM.reserveProfilesForFactoryRestore(1).then(() => {
    console.info(`reserveProfilesForFactoryRestore invoking succeeded.`);
}).catch((err: BusinessError<void>) => {
    console.error(`reserveProfilesForFactoryRestore, ErrorState: err->${JSON.stringify(err)}`);
});
```
