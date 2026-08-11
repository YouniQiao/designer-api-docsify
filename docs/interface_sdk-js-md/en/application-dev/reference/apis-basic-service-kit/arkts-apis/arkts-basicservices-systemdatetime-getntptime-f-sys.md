# getNtpTime (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getNtpTime

```TypeScript
function getNtpTime(): long
```

Obtains the actual time calculated based on the last updated NTP time. This API returns the result synchronously.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-systemDateTime-function getNtpTime(): long--><!--Device-systemDateTime-function getNtpTime(): long-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | Unix epoch time (ms) calculated based on the last updated NTP time. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13000002](../../apis-basic-services-kit/errorcode-time.md#13000002-ntp-time-not-updated) | updateNtpTime() is not called successfully. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

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

