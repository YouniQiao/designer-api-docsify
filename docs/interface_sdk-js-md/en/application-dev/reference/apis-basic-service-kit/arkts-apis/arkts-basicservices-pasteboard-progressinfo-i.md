# ProgressInfo

Defines the progress information. This information is reported only when  
[ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) is set to **NONE**.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-pasteboard-interface ProgressInfo--><!--Device-pasteboard-interface ProgressInfo-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## progress

```TypeScript
progress: int
```

If the progress indicator provided by the system is not used, the system reports the progress percentage of the paste task.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ProgressInfo-progress: int--><!--Device-ProgressInfo-progress: int-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

