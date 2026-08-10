# getNtpTime (System API)

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getNtpTime

```TypeScript
function getNtpTime(): long
```

使用同步方式获取基于上次更新的NTP时间所计算出的真实时间。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-systemDateTime-function getNtpTime(): long--><!--Device-systemDateTime-function getNtpTime(): long-End-->

**System capability:** SystemCapability.MiscServices.Time

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | 基于上次更新的NTP时间所计算出的Unix纪元时间(ms)。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13000002 | updateNtpTime() is not called successfully. |
| 202 | Permission verification failed. A non-system application calls a system API. |

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

