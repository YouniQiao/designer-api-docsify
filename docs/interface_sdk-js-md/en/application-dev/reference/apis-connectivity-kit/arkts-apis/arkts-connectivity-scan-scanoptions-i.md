# ScanOptions

扫描参数。

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

扫描时长。“持续时间”，单位为秒，有效范围为10s~60s。如果不设置“持续时间”，则会一直扫描。单位为： 秒，取值应为[10,60]内的整数。

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

扫描模式。如果未设置“scanMode”，则默认值为“SCAN_MODE_LOW_POWER”。默认值： SCAN_MODE_LOW_POWER。

**Type:** [ScanMode](arkts-connectivity-bluetooth-scanmode-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScanOptions-scanMode?: ScanMode--><!--Device-ScanOptions-scanMode?: ScanMode-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

