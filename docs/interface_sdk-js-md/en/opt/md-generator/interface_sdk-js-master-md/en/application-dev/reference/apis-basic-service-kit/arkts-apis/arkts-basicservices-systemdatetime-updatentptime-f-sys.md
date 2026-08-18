# updateNtpTime (System API)

## Modules to Import

```TypeScript
```

## updateNtpTime

```TypeScript
function updateNtpTime(): Promise<void>
```

Updates the NTP time from the NTP server This API returns the result asynchronously. In this way, the NTP time is updated from the NTP server only once within one hour.

**Since:** 23

<!--Device-systemDateTime-function updateNtpTime(): Promise<void>--><!--Device-systemDateTime-function updateNtpTime(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [13000001](../../apis-basic-services-kit/errorcode-time.md#13000001-network-or-os-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.updateNtpTime().then(() => {
    console.info(`Succeeded in updating ntp time.`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to update ntp time. message: ${error.message}, code: ${error.code}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to update ntp time. message: ${error.message}, code: ${error.code}`);
}
```
