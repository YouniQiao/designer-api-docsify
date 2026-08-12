# UpgradePeriod (System API)

Represents an automatic upgrade period.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface UpgradePeriod--><!--Device-update-export interface UpgradePeriod-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from '@kit.BasicServicesKit';
```

## end

```TypeScript
end: int
```

End time. The value ranges from 0 to 1440, in minutes. This parameter indicates the number of minutes in a day. The value **0** indicates the time of 00:00, and the value **1440** indicates 24:00.

The value must be greater than or equal to that of **start**. An exception is thrown if the value is out of range.

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

Start time. The value ranges from 0 to 1440, in minutes. This parameter indicates the number of minutes in a day.The value **0** indicates the time of 00:00, and the value **1440** indicates 24:00.

The value must be less than or equal to that of **end**. An exception is thrown if the value is out of range.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-UpgradePeriod-start: int--><!--Device-UpgradePeriod-start: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

