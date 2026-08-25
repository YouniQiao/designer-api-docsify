# getNtpTime (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getNtpTime

```TypeScript
function getNtpTime(): number
```

Obtains the actual time calculated based on the last updated NTP time. This API returns the result synchronously.

**Since:** 14

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13000002](../errorcode-time.md#13000002-ntp-time-not-updated) |
