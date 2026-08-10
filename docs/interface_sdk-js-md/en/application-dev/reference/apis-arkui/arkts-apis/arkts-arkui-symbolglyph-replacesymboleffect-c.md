# ReplaceSymbolEffect

ReplaceSymbolEffect继承自父类SymbolEffect。

**Inheritance/Implementation:** ReplaceSymbolEffect extends [SymbolEffect](../arkts-components/arkts-arkui-symboleffect-c.md/arkts-arkui-symboleffect-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ReplaceSymbolEffect extends SymbolEffect--><!--Device-unnamed-export declare class ReplaceSymbolEffect extends SymbolEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)
```

ReplaceSymbolEffect的构造函数，替换动效。支持指定具体的替换动效类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReplaceSymbolEffect-constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)--><!--Device-ReplaceSymbolEffect-constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scope | [EffectScope](../arkts-components/arkts-arkui-effectscope-e.md) | No | 动效范围。&lt;br/&gt;默认值：EffectScope.LAYER |
| replaceType | [ReplaceEffectType](../arkts-components/arkts-arkui-replaceeffecttype-e.md) | No | 替换动效类型。&lt;br/&gt;默认值：ReplaceEffectType.SEQUENTIAL |

## replaceType

```TypeScript
replaceType?: ReplaceEffectType
```

替换动效类型。

默认值：ReplaceEffectType.SEQUENTIAL

**Type:** [ReplaceEffectType](../arkts-components/arkts-arkui-replaceeffecttype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReplaceSymbolEffect-replaceType?: ReplaceEffectType--><!--Device-ReplaceSymbolEffect-replaceType?: ReplaceEffectType-End-->

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

<!--Device-ReplaceSymbolEffect-scope?: EffectScope--><!--Device-ReplaceSymbolEffect-scope?: EffectScope-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

