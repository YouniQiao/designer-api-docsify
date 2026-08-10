# MultiAppMode (System API)

定义应用是否支持多开模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export enum MultiAppMode--><!--Device-unnamed-export enum MultiAppMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## NOT_SUPPORTED

```TypeScript
NOT_SUPPORTED = 0
```

应用不支持多开模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiAppMode-NOT_SUPPORTED = 0--><!--Device-MultiAppMode-NOT_SUPPORTED = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## MULTI_INSTANCE

```TypeScript
MULTI_INSTANCE = 1
```

应用支持多实例模式。

**说明：** 只支持2in1设备。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiAppMode-MULTI_INSTANCE = 1--><!--Device-MultiAppMode-MULTI_INSTANCE = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## APP_CLONE

```TypeScript
APP_CLONE = 2
```

应用支持分身模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MultiAppMode-APP_CLONE = 2--><!--Device-MultiAppMode-APP_CLONE = 2-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

