# FactoryResetInfo (System API)

Describes the information of restoring factory settings.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from '@kit.BasicServicesKit';
```

## duration

```TypeScript
duration: int
```

Duration required for restoring factory settings, in minutes. The value range is [0, +∞]. An exception is thrown if the value is out of range.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.
