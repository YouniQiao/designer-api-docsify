# ScanOptions

Describes the parameters for scan.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-scan-interface ScanOptions--><!--Device-scan-interface ScanOptions-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.ConnectivityKit';
```

## duration

```TypeScript
duration?: int
```

Indicates the scan duration.If the "duration" is not set, the scanning is performed all the time.Unit: Seconds, The value must be an integer within [10,60].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanOptions-duration?: int--><!--Device-ScanOptions-duration?: int-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

## scanMode

```TypeScript
scanMode?: ScanMode
```

Indicates the scan mode.If the "scanMode" is not set, the default value is "SCAN_MODE_LOW_POWER".Default value: SCAN_MODE_LOW_POWER.

**Type:** [ScanMode](arkts-connectivity-bluetooth-scanmode-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanOptions-scanMode?: ScanMode--><!--Device-ScanOptions-scanMode?: ScanMode-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

