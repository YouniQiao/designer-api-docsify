# StartOptions

StartOptions可以作为启动UIAbility接口（例如  
[startAbility()](arkts-ability-uiabilitycontext-c.md#startability)）的入参，用于指定目标UIAbility启动时的选项，包括但不局限于窗口模式、目标UIAbility启动时所在的屏幕等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class StartOptions--><!--Device-unnamed-declare class StartOptions-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { StartOptions } from 'kits/@kit.AbilityKit';
```

## windowFocused

```TypeScript
windowFocused?: boolean
```

窗口是否获焦。默认是true，表示窗口获焦。

**约束：**

1.该功能仅在2in1和Tablet设备上生效。

2.仅在[UIAbilityContext.startAbility](arkts-ability-uiabilitycontext-c.md#startability)中生效。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartOptions-windowFocused?: boolean--><!--Device-StartOptions-windowFocused?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

