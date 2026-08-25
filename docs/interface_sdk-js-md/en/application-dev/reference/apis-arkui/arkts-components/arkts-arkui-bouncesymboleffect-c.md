# BounceSymbolEffect

Defines BounceSymbolEffect class, which inherits from **SymbolEffect**.

**Inheritance/Implementation:** BounceSymbolEffect extends [SymbolEffect](arkts-arkui-symboleffect-c.md)

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(scope?: EffectScope, direction?: EffectDirection)
```

A constructor used to create a **ScaleSymbolEffect** instance, which comes with a scaling animation effect.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [scope](#scope) | [EffectScope](arkts-arkui-effectscope-e.md) | No |
| [direction](#direction) | [EffectDirection](arkts-arkui-effectdirection-e.md) | No |

## direction

```TypeScript
direction?: EffectDirection
```

Effect direction.Default value: **EffectDirection.DOWN**

**Type:** [EffectDirection](arkts-arkui-effectdirection-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scope

```TypeScript
scope?: EffectScope
```

Effect scope.Default value: **EffectScope.LAYER**

**Type:** [EffectScope](arkts-arkui-effectscope-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
