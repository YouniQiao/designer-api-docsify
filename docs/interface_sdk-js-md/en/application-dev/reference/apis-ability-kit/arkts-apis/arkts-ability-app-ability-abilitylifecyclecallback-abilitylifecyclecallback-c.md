# AbilityLifecycleCallback

The lifecycle of a [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) dynamically changes from creation to destruction. The AbilityLifecycleCallback module provides the capability to listen for these lifecycle changes, which can be used for scenarios such as tracking the runtime duration of each UIAbility and performing data loading decoupled from the service logic of UIAbility.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class AbilityLifecycleCallback--><!--Device-unnamed-declare class AbilityLifecycleCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { AbilityLifecycleCallback } from '@kit.AbilityKit';
```

## onAbilityBackground

```TypeScript
onAbilityBackground(ability: UIAbility): void
```

Called after the [onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onBackground) callback of the UIAbility is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onAbilityBackground(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityBackground(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityContinue

```TypeScript
onAbilityContinue(ability: UIAbility): void
```

Called after the [onContinue](arkts-ability-app-ability-uiability-uiability-c.md#onContinue) callback of the UIAbility is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onAbilityContinue(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityContinue(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityCreate

```TypeScript
onAbilityCreate(ability: UIAbility): void
```

Called after the [onCreate](arkts-ability-app-ability-uiability-uiability-c.md#onCreate) callback of the UIAbility is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onAbilityCreate(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityCreate(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityDestroy

```TypeScript
onAbilityDestroy(ability: UIAbility): void
```

Called after the [onDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onDestroy) callback of the UIAbility is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onAbilityDestroy(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityDestroy(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityForeground

```TypeScript
onAbilityForeground(ability: UIAbility): void
```

Called after the [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onForeground) callback of the UIAbility is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onAbilityForeground(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityForeground(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilitySaveState

```TypeScript
onAbilitySaveState?(ability: UIAbility): void
```

Called after the [onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onAbilitySaveState?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilitySaveState?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityWillBackground

```TypeScript
onAbilityWillBackground?(ability: UIAbility): void
```

Called before the [onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onBackground) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onAbilityWillBackground?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillBackground?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityWillContinue

```TypeScript
onAbilityWillContinue?(ability: UIAbility): void
```

Called before the [onContinue](arkts-ability-app-ability-uiability-uiability-c.md#onContinue) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onAbilityWillContinue?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillContinue?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityWillCreate

```TypeScript
onAbilityWillCreate?(ability: UIAbility): void
```

Called before the [onCreate](arkts-ability-app-ability-uiability-uiability-c.md#onCreate) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onAbilityWillCreate?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillCreate?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityWillDestroy

```TypeScript
onAbilityWillDestroy?(ability: UIAbility): void
```

Called before the [onDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onDestroy) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onAbilityWillDestroy?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillDestroy?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityWillForeground

```TypeScript
onAbilityWillForeground?(ability: UIAbility): void
```

Called before the [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onForeground) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onAbilityWillForeground?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillForeground?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilityWillSaveState

```TypeScript
onAbilityWillSaveState?(ability: UIAbility): void
```

Called before the [onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onAbilityWillSaveState?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onAbilityWillSaveState?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onNewWant

```TypeScript
onNewWant?(ability: UIAbility): void
```

Called after the [onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onNewWant) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onNewWant?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onNewWant?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWillNewWant

```TypeScript
onWillNewWant?(ability: UIAbility): void
```

Called before the [onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onNewWant) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onWillNewWant?(ability: UIAbility): void--><!--Device-AbilityLifecycleCallback-onWillNewWant?(ability: UIAbility): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageActive

```TypeScript
onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void
```

Called when the main window of the UIAbility gains focus.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageCreate

```TypeScript
onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void
```

Called after the [onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate) callback of the UIAbility is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageDestroy

```TypeScript
onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void
```

Called after the [onWindowStageDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageDestroy) callback of the UIAbility is triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageInactive

```TypeScript
onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void
```

Called when the main window of the UIAbility loses focus.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AbilityLifecycleCallback-onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageRestore

```TypeScript
onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void
```

Called after the [onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageRestore) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageWillCreate

```TypeScript
onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void
```

Called before the [onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageWillDestroy

```TypeScript
onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void
```

Called before the [onWindowStageDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageDestroy) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onWindowStageWillRestore

```TypeScript
onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void
```

Called before the [onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageRestore) callback of the UIAbility is triggered.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AbilityLifecycleCallback-onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void--><!--Device-AbilityLifecycleCallback-onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ability | [UIAbility](arkts-ability-app-ability-uiability-uiability-c.md) | Yes | UIAbility object associated with the callback event. |
| windowStage | window.WindowStage | Yes | Main window manager of the UIAbility associated with the callback event. |

## Examples

For details, see AbilityLifecycleCallback Usage Example.

## onAbilitySaveState

```TypeScript
onAbilitySaveState?: OnAbilitySaveStateFn
```

Called after the [onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState) callback of the UIAbility is triggered.

**Type:** [OnAbilitySaveStateFn](arkts-ability-onabilitysavestatefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onAbilitySaveState?: OnAbilitySaveStateFn--><!--Device-AbilityLifecycleCallback-onAbilitySaveState?: OnAbilitySaveStateFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillBackground

```TypeScript
onAbilityWillBackground?: OnAbilityWillBackgroundFn
```

Called before the [onBackground](arkts-ability-app-ability-uiability-uiability-c.md#onBackground) callback of the UIAbility is triggered.

**Type:** [OnAbilityWillBackgroundFn](arkts-ability-onabilitywillbackgroundfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onAbilityWillBackground?: OnAbilityWillBackgroundFn--><!--Device-AbilityLifecycleCallback-onAbilityWillBackground?: OnAbilityWillBackgroundFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillContinue

```TypeScript
onAbilityWillContinue?: OnAbilityWillContinueFn
```

Called before the [onContinue](arkts-ability-app-ability-uiability-uiability-c.md#onContinue) callback of the UIAbility is triggered.

**Type:** [OnAbilityWillContinueFn](arkts-ability-onabilitywillcontinuefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onAbilityWillContinue?: OnAbilityWillContinueFn--><!--Device-AbilityLifecycleCallback-onAbilityWillContinue?: OnAbilityWillContinueFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillCreate

```TypeScript
onAbilityWillCreate?: OnAbilityWillCreateFn
```

Called before the [onCreate](arkts-ability-app-ability-uiability-uiability-c.md#onCreate) callback of the UIAbility is triggered.

**Type:** [OnAbilityWillCreateFn](arkts-ability-onabilitywillcreatefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onAbilityWillCreate?: OnAbilityWillCreateFn--><!--Device-AbilityLifecycleCallback-onAbilityWillCreate?: OnAbilityWillCreateFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillDestroy

```TypeScript
onAbilityWillDestroy?: OnAbilityWillDestroyFn
```

Called before the [onDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onDestroy) callback of the UIAbility is triggered.

**Type:** [OnAbilityWillDestroyFn](arkts-ability-onabilitywilldestroyfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onAbilityWillDestroy?: OnAbilityWillDestroyFn--><!--Device-AbilityLifecycleCallback-onAbilityWillDestroy?: OnAbilityWillDestroyFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillForeground

```TypeScript
onAbilityWillForeground?: OnAbilityWillForegroundFn
```

Called before the [onForeground](arkts-ability-app-ability-uiability-uiability-c.md#onForeground) callback of the UIAbility is triggered.

**Type:** [OnAbilityWillForegroundFn](arkts-ability-onabilitywillforegroundfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onAbilityWillForeground?: OnAbilityWillForegroundFn--><!--Device-AbilityLifecycleCallback-onAbilityWillForeground?: OnAbilityWillForegroundFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onAbilityWillSaveState

```TypeScript
onAbilityWillSaveState?: OnAbilityWillSaveStateFn
```

Called before the [onSaveState](arkts-ability-app-ability-uiability-uiability-c.md#onSaveState) callback of the UIAbility is triggered.

**Type:** [OnAbilityWillSaveStateFn](arkts-ability-onabilitywillsavestatefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onAbilityWillSaveState?: OnAbilityWillSaveStateFn--><!--Device-AbilityLifecycleCallback-onAbilityWillSaveState?: OnAbilityWillSaveStateFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onNewWant

```TypeScript
onNewWant?: OnNewWantFn
```

Called after the [onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onNewWant) callback of the UIAbility is triggered.

**Type:** [OnNewWantFn](arkts-ability-onnewwantfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onNewWant?: OnNewWantFn--><!--Device-AbilityLifecycleCallback-onNewWant?: OnNewWantFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWillNewWant

```TypeScript
onWillNewWant?: OnWillNewWantFn
```

Called before the [onNewWant](arkts-ability-app-ability-uiability-uiability-c.md#onNewWant) callback of the UIAbility is triggered.

**Type:** [OnWillNewWantFn](arkts-ability-onwillnewwantfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onWillNewWant?: OnWillNewWantFn--><!--Device-AbilityLifecycleCallback-onWillNewWant?: OnWillNewWantFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageRestore

```TypeScript
onWindowStageRestore?: OnWindowStageRestoreFn
```

Called after the [onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageRestore) callback of the UIAbility is triggered.

**Type:** [OnWindowStageRestoreFn](arkts-ability-onwindowstagerestorefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onWindowStageRestore?: OnWindowStageRestoreFn--><!--Device-AbilityLifecycleCallback-onWindowStageRestore?: OnWindowStageRestoreFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageWillCreate

```TypeScript
onWindowStageWillCreate?: OnWindowStageWillCreateFn
```

Called before the [onWindowStageCreate](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageCreate) callback of the UIAbility is triggered.

**Type:** [OnWindowStageWillCreateFn](arkts-ability-onwindowstagewillcreatefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onWindowStageWillCreate?: OnWindowStageWillCreateFn--><!--Device-AbilityLifecycleCallback-onWindowStageWillCreate?: OnWindowStageWillCreateFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageWillDestroy

```TypeScript
onWindowStageWillDestroy?: OnWindowStageWillDestroyFn
```

Called before the [onWindowStageDestroy](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageDestroy) callback of the UIAbility is triggered.

**Type:** [OnWindowStageWillDestroyFn](arkts-ability-onwindowstagewilldestroyfn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onWindowStageWillDestroy?: OnWindowStageWillDestroyFn--><!--Device-AbilityLifecycleCallback-onWindowStageWillDestroy?: OnWindowStageWillDestroyFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onWindowStageWillRestore

```TypeScript
onWindowStageWillRestore?: OnWindowStageWillRestoreFn
```

Called before the [onWindowStageRestore](arkts-ability-app-ability-uiability-uiability-c.md#onWindowStageRestore) callback of the UIAbility is triggered.

**Type:** [OnWindowStageWillRestoreFn](arkts-ability-onwindowstagewillrestorefn-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbilityLifecycleCallback-onWindowStageWillRestore?: OnWindowStageWillRestoreFn--><!--Device-AbilityLifecycleCallback-onWindowStageWillRestore?: OnWindowStageWillRestoreFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

