# HierarchicalSymbolEffect

HierarchicalSymbolEffect继承自父类SymbolEffect。

**继承/实现关系：** HierarchicalSymbolEffect extends [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(fillStyle?: EffectFillStyle)
```

HierarchicalSymbolEffect的构造函数，层级动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fillStyle](#fillstyle) | [EffectFillStyle](arkts-arkui-symbolglyph-effectfillstyle-e.md) | 否 |

## fillStyle

```TypeScript
fillStyle?: EffectFillStyle
```

动效模式。默认值：EffectFillStyle.CUMULATIVE

**类型：** [EffectFillStyle](arkts-arkui-symbolglyph-effectfillstyle-e.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
