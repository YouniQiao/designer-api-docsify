# StartupVisibility

Enumerates the visibility statuses of the UIAbility after it is started. If the target UIAbility is set to invisible, the window of the target UIAbility is not displayed in the foreground, there is no icon in the dock, and the **onForeground** lifecycle of the target UIAbility is not triggered. As a property of [StartOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, **StartupVisibility** takes effect only in [UIAbilityContext.startAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and specifies the visibility of the target UIAbility after it is started. This value takes effect only on 2-in-1 devices and tablets. If it is used on other devices, error code 801 is returned.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-contextConstant-export enum StartupVisibility--><!--Device-contextConstant-export enum StartupVisibility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## STARTUP_HIDE

```TypeScript
STARTUP_HIDE = 0
```

The target UIAbility is hidden after it is started in the new process. The **onForeground** lifecycle of the UIAbility is not invoked.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupVisibility-STARTUP_HIDE = 0--><!--Device-StartupVisibility-STARTUP_HIDE = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## STARTUP_SHOW

```TypeScript
STARTUP_SHOW = 1
```

The target UIAbility is displayed normally after it is started in the new process.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StartupVisibility-STARTUP_SHOW = 1--><!--Device-StartupVisibility-STARTUP_SHOW = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

