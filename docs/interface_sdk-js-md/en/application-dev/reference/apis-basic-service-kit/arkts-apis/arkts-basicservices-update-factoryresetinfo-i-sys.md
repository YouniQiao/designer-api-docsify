# FactoryResetInfo (System API)

Describes the information of restoring factory settings.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-update-export interface FactoryResetInfo--><!--Device-update-export interface FactoryResetInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'update';
```

## duration

```TypeScript
duration: int
```

Duration required for restoring factory settings, in minutes. The value range is [0, +∞]. An exception is thrown if the value is out of range.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FactoryResetInfo-duration: int--><!--Device-FactoryResetInfo-duration: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

