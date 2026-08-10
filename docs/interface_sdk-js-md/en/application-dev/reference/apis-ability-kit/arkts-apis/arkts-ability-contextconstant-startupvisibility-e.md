# StartupVisibility

UIAbility启动后是否可见。当用户设置目标UIAbility为不可见时，目标UIAbility的窗口不会显示在前台，dock栏也不会有图标，同时目标UIAbility的onForeground生命周期不会被调用。StartupVisibility作为[StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md)的一个属性，仅在  
[UIAbilityContext.startAbility](arkts-ability-uiabilitycontext-c.md#startability)中生效，用来指定目标UIAbility启动后的可见性。该功能仅在2in1和Tablet设备上生效，在其他设备中返回801错误码。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-contextConstant-export enum StartupVisibility--><!--Device-contextConstant-export enum StartupVisibility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## STARTUP_HIDE

```TypeScript
STARTUP_HIDE = 0
```

目标UIAbility启动后，进入隐藏状态。不会调用UIAbility的onForeground生命周期。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupVisibility-STARTUP_HIDE = 0--><!--Device-StartupVisibility-STARTUP_HIDE = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## STARTUP_SHOW

```TypeScript
STARTUP_SHOW = 1
```

目标UIAbility启动后，正常显示。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupVisibility-STARTUP_SHOW = 1--><!--Device-StartupVisibility-STARTUP_SHOW = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

