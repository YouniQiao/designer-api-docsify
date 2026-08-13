# EnvironmentCallback

The EnvironmentCallback module provides capabilities to listen for system environment changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare interface EnvironmentCallback--><!--Device-unnamed-declare interface EnvironmentCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## onConfigurationUpdated

```TypeScript
onConfigurationUpdated(config: Configuration): void
```

Called when the system configuration changes, after [a listener has been registered for such events](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#on_abilityLifecycle) .

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnvironmentCallback-onConfigurationUpdated(config: Configuration): void--><!--Device-EnvironmentCallback-onConfigurationUpdated(config: Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [Configuration](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-configuration-configuration-i.md) | Yes | Configuration object after the change. |

## onMemoryLevel

```TypeScript
onMemoryLevel(level: AbilityConstant.MemoryLevel): void
```

Called when the system memory level changes, after [a listener has been registered for such events](../../apis-ability-kit/arkts-apis/arkts-ability-applicationcontext-c.md#on_abilityLifecycle) .

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnvironmentCallback-onMemoryLevel(level: AbilityConstant.MemoryLevel): void--><!--Device-EnvironmentCallback-onMemoryLevel(level: AbilityConstant.MemoryLevel): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | AbilityConstant.MemoryLevel | Yes | Memory level, indicating the available memory of the entire device. |

