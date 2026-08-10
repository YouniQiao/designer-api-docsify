# ScaleSymbolEffect

ScaleSymbolEffect继承自父类SymbolEffect。

**Inheritance/Implementation:** ScaleSymbolEffect extends [SymbolEffect](../arkts-components/arkts-arkui-symboleffect-c.md/arkts-arkui-symboleffect-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ScaleSymbolEffect extends SymbolEffect--><!--Device-unnamed-export declare class ScaleSymbolEffect extends SymbolEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(scope?: EffectScope, direction?: EffectDirection)
```

ScaleSymbolEffect的构造函数，缩放动效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleSymbolEffect-constructor(scope?: EffectScope, direction?: EffectDirection)--><!--Device-ScaleSymbolEffect-constructor(scope?: EffectScope, direction?: EffectDirection)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scope | [EffectScope](../arkts-components/arkts-arkui-effectscope-e.md) | No | 动效范围。&lt;br/&gt;默认值：EffectScope.LAYER |
| direction | [EffectDirection](arkts-arkui-symbolglyph-effectdirection-e.md) | No | 动效方向。&lt;br/&gt;默认值：EffectDirection.DOWN |

## direction

```TypeScript
direction?: EffectDirection
```

动效方向。

默认值：EffectDirection.DOWN

**Type:** [EffectDirection](arkts-arkui-symbolglyph-effectdirection-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleSymbolEffect-direction?: EffectDirection--><!--Device-ScaleSymbolEffect-direction?: EffectDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scope

```TypeScript
scope?: EffectScope
```

动效范围。

默认值：EffectScope.LAYER

**Type:** [EffectScope](../arkts-components/arkts-arkui-effectscope-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScaleSymbolEffect-scope?: EffectScope--><!--Device-ScaleSymbolEffect-scope?: EffectScope-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

