# getNtpTime (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from '@kit.BasicServicesKit';
```

## getNtpTime

```TypeScript
function getNtpTime(): number
```

Obtains the actual time calculated based on the last updated NTP time. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-systemDateTime-function getNtpTime(): long--><!--Device-systemDateTime-function getNtpTime(): long-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [13000002](../../apis-basic-services-kit/errorcode-time.md#13000002-ntp-time-not-updated) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getNtpTime();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get ntp time. message: ${error.message}, code: ${error.code}`);
}
```
