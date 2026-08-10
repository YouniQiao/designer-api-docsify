# EnvironmentCallback

EnvironmentCallback模块提供对系统环境变化监听回调的能力。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-export default class EnvironmentCallback--><!--Device-unnamed-export default class EnvironmentCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { EnvironmentCallback } from 'kits/@kit.AbilityKit';
```

## onConfigurationUpdated

```TypeScript
onConfigurationUpdated(config: Configuration): void
```

[注册系统环境变化的监听](./application/ApplicationContext:ApplicationContext.on(type: 'environment', callback: EnvironmentCallback))后，在系统环境变化时触发回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EnvironmentCallback-onConfigurationUpdated(config: Configuration): void--><!--Device-EnvironmentCallback-onConfigurationUpdated(config: Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes | 变化后的Configuration对象。 |

## Examples

See [Usage of EnvironmentCallback](#usage-of-environmentcallback).

## onMemoryLevel

```TypeScript
onMemoryLevel(level: AbilityConstant.MemoryLevel): void
```

[注册系统环境变化的监听](./application/ApplicationContext:ApplicationContext.on(type: 'environment', callback: EnvironmentCallback))后，在系统内存变化时触发回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-EnvironmentCallback-onMemoryLevel(level: AbilityConstant.MemoryLevel): void--><!--Device-EnvironmentCallback-onMemoryLevel(level: AbilityConstant.MemoryLevel): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| level | AbilityConstant.MemoryLevel | Yes | 整机可用内存级别，对应的触发场景详见 [AbilityConstant.MemoryLevel](arkts-ability-abilityconstant-memorylevel-e.md)。 |

## Examples

See [Usage of EnvironmentCallback](#usage-of-environmentcallback).

