# FactoryResetInfo (System API)

恢复出厂设置信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-update-export interface FactoryResetInfo--><!--Device-update-export interface FactoryResetInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## duration

```TypeScript
duration: int
```

恢复出厂设置所需持续时间。单位为min。取值范围[0, 86400]。超出范围时抛出异常。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FactoryResetInfo-duration: int--><!--Device-FactoryResetInfo-duration: int-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

