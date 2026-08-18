# ApplicationStateChangeCallback

The module is used to listen for state changes of the current application process. For ease of description, the term "application process" will be referred to as "process" in the following sections. You can call [ApplicationContext.on('applicationStateChange')](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#on_abilitylifecycleabilitylifecycle) and pass in a custom ApplicationStateChangeCallback to listen for foreground/background state changes of the current process. This allows you to perform certain actions based on the process state changes, for example, tracking the duration of the process in the foreground and background, or clearing memory caches when the process moves to the background.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-declare interface ApplicationStateChangeCallback--><!--Device-unnamed-declare interface ApplicationStateChangeCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
```

## onApplicationBackground

```TypeScript
onApplicationBackground(): void
```

Called when the current process switches from the foreground to the background. When this callback is triggered, the process is fully in the background state, and you can perform operations suitable for the background state (for example, clearing memory caches).

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationStateChangeCallback-onApplicationBackground(): void--><!--Device-ApplicationStateChangeCallback-onApplicationBackground(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onApplicationForeground

```TypeScript
onApplicationForeground(): void
```

Called when the current process switches from the background to the foreground. When this callback is triggered, it does not mean that the process is already fully in the foreground state, but rather that it is about to enter the foreground state. At this point, operations that depend on the foreground state (such as launching another UIAbility) cannot be performed.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ApplicationStateChangeCallback-onApplicationForeground(): void--><!--Device-ApplicationStateChangeCallback-onApplicationForeground(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

