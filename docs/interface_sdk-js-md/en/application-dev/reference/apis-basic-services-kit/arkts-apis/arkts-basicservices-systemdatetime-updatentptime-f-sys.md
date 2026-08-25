# updateNtpTime (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## updateNtpTime

```TypeScript
function updateNtpTime(): Promise<void>
```

Updates the NTP time from the NTP server This API returns the result asynchronously. In this way, the NTP time is updated from the NTP server only once within one hour.

**Since:** 14

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [13000001](../errorcode-time.md#13000001-network-or-os-error) |
