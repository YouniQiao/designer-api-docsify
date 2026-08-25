# EnvironmentCallback

The EnvironmentCallback module provides capabilities to listen for system environment changes.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { EnvironmentCallback } from 'kits/@kit.AbilityKit';
```

## onConfigurationUpdated

```TypeScript
onConfigurationUpdated(config: Configuration): void
```

Called when the system configuration changes, after [a listener has been registered for such events](arkts-ability-applicationcontext-c.md#onenvironment).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes |

## onMemoryLevel

```TypeScript
onMemoryLevel(level: AbilityConstant.MemoryLevel): void
```

Called when the system memory level changes, after [a listener has been registered for such events](arkts-ability-applicationcontext-c.md#onenvironment).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | AbilityConstant.MemoryLevel | Yes |
