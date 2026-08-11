# EnvironmentCallback

The EnvironmentCallback module provides capabilities to listen for system environment changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-declare interface EnvironmentCallback--><!--Device-unnamed-declare interface EnvironmentCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { EnvironmentCallback } from 'kits/@kit.AbilityKit';
```

## onConfigurationUpdated

```TypeScript
onConfigurationUpdated(config: Configuration): void
```

Called when the system configuration changes, after  
[a listener has been registered for such events](./application/ApplicationContext:ApplicationContext#on(type:'environment', callback: EnvironmentCallback)).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnvironmentCallback-onConfigurationUpdated(config: Configuration): void--><!--Device-EnvironmentCallback-onConfigurationUpdated(config: Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes | Configuration object after the change. |

## onMemoryLevel

```TypeScript
onMemoryLevel(level: AbilityConstant.MemoryLevel): void
```

Called when the system memory level changes, after  
[a listener has been registered for such events](./application/ApplicationContext:ApplicationContext#on(type:'environment', callback: EnvironmentCallback)).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnvironmentCallback-onMemoryLevel(level: AbilityConstant.MemoryLevel): void--><!--Device-EnvironmentCallback-onMemoryLevel(level: AbilityConstant.MemoryLevel): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | AbilityConstant.MemoryLevel | Yes | Memory level, indicating the available memory of the entire device. |

