# UpgradePeriod (System API)

升级时间段。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface UpgradePeriod--><!--Device-update-export interface UpgradePeriod-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## end

```TypeScript
end: int
```

结束时间，取值范围[0, 1440]，单位为min。表示一天中的分钟数，0表示00:00，1440表示24:00。

必须大于或等于start，超出范围时抛出异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradePeriod-end: int--><!--Device-UpgradePeriod-end: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## start

```TypeScript
start: int
```

开始时间，取值范围[0, 1440]，单位为min。表示一天中的分钟数，0表示00:00，1440表示24:00。

必须小于或等于end，超出范围时抛出异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradePeriod-start: int--><!--Device-UpgradePeriod-start: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

