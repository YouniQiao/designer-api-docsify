# ReplaceSymbolEffect

ReplaceSymbolEffect继承自父类SymbolEffect。

**Inheritance/Implementation:** ReplaceSymbolEffect extends [SymbolEffect](arkts-arkui-symboleffect-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class ReplaceSymbolEffect extends SymbolEffect--><!--Device-unnamed-declare class ReplaceSymbolEffect extends SymbolEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(scope?: EffectScope)
```

AppearSymbolEffect的构造函数，出现动效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ReplaceSymbolEffect-constructor(scope?: EffectScope)--><!--Device-ReplaceSymbolEffect-constructor(scope?: EffectScope)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scope | [EffectScope](arkts-arkui-effectscope-e.md) | No | 动效范围。具体枚举值及说明请参考EffectScope枚举说明。 &lt;br&gt;默认值：EffectScope.LAYER |

## constructor

```TypeScript
constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)
```

ReplaceSymbolEffect的构造函数，替换动效。支持指定具体的替换动效类型。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-ReplaceSymbolEffect-constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)--><!--Device-ReplaceSymbolEffect-constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scope | [EffectScope](arkts-arkui-effectscope-e.md) | No | 动效范围。 &lt;br&gt;默认值：EffectScope.LAYER |
| replaceType | [ReplaceEffectType](arkts-arkui-replaceeffecttype-e.md) | No | 替换动效类型。 &lt;br&gt;默认值：ReplaceEffectType.SEQUENTIAL |

## replaceType

```TypeScript
replaceType?: ReplaceEffectType
```

替换动效类型。具体枚举值及说明请参考ReplaceEffectType枚举说明。

默认值：ReplaceEffectType.SEQUENTIAL

**Type:** [ReplaceEffectType](arkts-arkui-replaceeffecttype-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-ReplaceSymbolEffect-replaceType?: ReplaceEffectType--><!--Device-ReplaceSymbolEffect-replaceType?: ReplaceEffectType-End-->

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

<!--Device-ReplaceSymbolEffect-scope?: EffectScope--><!--Device-ReplaceSymbolEffect-scope?: EffectScope-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

