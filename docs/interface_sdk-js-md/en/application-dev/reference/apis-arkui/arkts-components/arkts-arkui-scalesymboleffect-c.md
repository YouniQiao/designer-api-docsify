# ScaleSymbolEffect

ScaleSymbolEffect继承自父类SymbolEffect。

**Inheritance/Implementation:** ScaleSymbolEffect extends [SymbolEffect](arkts-arkui-symboleffect-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class ScaleSymbolEffect extends SymbolEffect--><!--Device-unnamed-declare class ScaleSymbolEffect extends SymbolEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(scope?: EffectScope, direction?: EffectDirection)
```

ScaleSymbolEffect的构造函数，缩放动效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ScaleSymbolEffect-constructor(scope?: EffectScope, direction?: EffectDirection)--><!--Device-ScaleSymbolEffect-constructor(scope?: EffectScope, direction?: EffectDirection)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scope | [EffectScope](arkts-arkui-effectscope-e.md) | No | 动效范围。具体枚举值及说明请参考EffectScope枚举说明。 &lt;br&gt;默认值：EffectScope.LAYER |
| direction | [EffectDirection](../arkts-apis/arkts-arkui-symbolglyph-effectdirection-e.md) | No | 动效方向。具体枚举值及说明请参考EffectDirection枚举说明。 &lt;br&gt;默认值：EffectDirection.DOWN |

## direction

```TypeScript
direction?: EffectDirection
```

动效方向。具体枚举值及说明请参考EffectDirection枚举说明。

默认值：EffectDirection.DOWN

**Type:** [EffectDirection](../arkts-apis/arkts-arkui-symbolglyph-effectdirection-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ScaleSymbolEffect-direction?: EffectDirection--><!--Device-ScaleSymbolEffect-direction?: EffectDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scope

```TypeScript
scope?: EffectScope
```

动效范围。具体枚举值及说明请参考EffectScope枚举说明。

默认值：EffectScope.LAYER

**Type:** [EffectScope](arkts-arkui-effectscope-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ScaleSymbolEffect-scope?: EffectScope--><!--Device-ScaleSymbolEffect-scope?: EffectScope-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

