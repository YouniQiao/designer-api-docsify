# Ability

The Ability class is the fundamental unit for application lifecycle scheduling. It is the base class of [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) and [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md#ExtensionAbility), and provides callbacks for system configuration updates and memory level updates. However, you cannot inherit directly from this base class. You should opt for either [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) or [ExtensionAbility](arkts-ability-app-ability-extensionability-extensionability-c.md#ExtensionAbility) based on your service needs. For details, see [Introduction to Ability Kit](../../../application-models/abilitykit-overview.md).

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class Ability--><!--Device-unnamed-declare class Ability-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { Ability } from '@kit.AbilityKit';
```

## onConfigurationUpdate

```TypeScript
onConfigurationUpdate(newConfig: Configuration): void
```

Called when a system environment variable changes. You can override this callback to respond to changes in the system environment variables. For example, when the system language changes, the application can perform customized processing in the callback. > **NOTE：**> > There are certain restrictions when this callback is actually triggered. For example, if you set the application > language by calling [setLanguage](arkts-ability-applicationcontext-c.md#setLanguage), the > system does not trigger the **onConfigurationUpdate** callback even if the system language changes. For details, > see [When to Use](../../../application-models/subscribe-system-environment-variable-changes.md#when-to-use).

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Ability-onConfigurationUpdate(newConfig: Configuration): void--><!--Device-Ability-onConfigurationUpdate(newConfig: Configuration): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newConfig | [Configuration](arkts-ability-app-ability-configuration-configuration-i.md) | Yes |

## Examples

```TypeScript
// You are not allowed to inherit from the top-level base class Ability. Therefore, the derived class UIAbility is used as an example.
import { UIAbility, Configuration } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onConfigurationUpdate(config: Configuration) {
    console.info(`onConfigurationUpdate, config: ${JSON.stringify(config)}`);
  }
}
```

## onMemoryLevel

```TypeScript
onMemoryLevel(level: AbilityConstant.MemoryLevel): void
```

Called when the available memory of the entire device changes to a specified level. You can override this callback to respond to changes in the memory level, for example, releasing cached data. > **NOTE：**> > Releasing UI components in the **onMemoryLevel** callback may block the main thread tasks of the current process. > Therefore, you are advised not to release UI components in this callback.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Ability-onMemoryLevel(level: AbilityConstant.MemoryLevel): void--><!--Device-Ability-onMemoryLevel(level: AbilityConstant.MemoryLevel): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| level | AbilityConstant.MemoryLevel | Yes |

## Examples

```TypeScript
// You are not allowed to inherit from the top-level base class Ability. Therefore, the derived class UIAbility is used as an example.
import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

class MyUIAbility extends UIAbility {
  onMemoryLevel(level: AbilityConstant.MemoryLevel) {
    console.info(`onMemoryLevel, level: ${JSON.stringify(level)}`);
  }
}
```
