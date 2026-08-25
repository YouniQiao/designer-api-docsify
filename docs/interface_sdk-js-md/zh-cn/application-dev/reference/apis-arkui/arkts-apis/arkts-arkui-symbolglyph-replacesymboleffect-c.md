# ReplaceSymbolEffect

ReplaceSymbolEffect继承自父类SymbolEffect。

**继承/实现关系：** ReplaceSymbolEffect extends [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)
```

ReplaceSymbolEffect的构造函数，替换动效。支持指定具体的替换动效类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [scope](#scope) | [EffectScope](arkts-arkui-symbolglyph-effectscope-e.md) | 否 |
| [replaceType](#replacetype) | [ReplaceEffectType](arkts-arkui-symbolglyph-replaceeffecttype-e.md) | 否 |

## replaceType

```TypeScript
replaceType?: ReplaceEffectType
```

替换动效类型。默认值：ReplaceEffectType.SEQUENTIAL

**类型：** [ReplaceEffectType](arkts-arkui-symbolglyph-replaceeffecttype-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scope

```TypeScript
scope?: EffectScope
```

动效范围。默认值：EffectScope.LAYER

**类型：** [EffectScope](arkts-arkui-symbolglyph-effectscope-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
