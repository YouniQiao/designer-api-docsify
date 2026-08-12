# ChipV2SymbolIcon

ChipV2SymbolIcon定义Symbol图标类。

继承自[ChipV2Icon](arkts-arkui-arkui-advanced-chipv2-chipv2icon-c.md#ChipV2Icon)。

**继承/实现关系：** ChipV2SymbolIcon extends [ChipV2Icon](arkts-arkui-arkui-advanced-chipv2-chipv2icon-c.md#ChipV2Icon)

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export abstract class ChipV2SymbolIcon extends ChipV2Icon--><!--Device-unnamed-export abstract class ChipV2SymbolIcon extends ChipV2Icon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(config: ChipV2SymbolIconConfig)
```

ChipV2SymbolIcon的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2SymbolIcon-constructor(config: ChipV2SymbolIconConfig)--><!--Device-ChipV2SymbolIcon-constructor(config: ChipV2SymbolIconConfig)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ChipV2SymbolIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2symboliconconfig-i.md) | 是 |

## activated

```TypeScript
public activated?: SymbolGlyphModifier
```

激活时图标设定。

默认值：不显示前缀图标或后缀图标。

值为undefined时，按默认值处理。

不支持使用[SymbolEffect](SymbolGlyphAttribute#symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean))修改动效类型及  
[effectStrategy](SymbolGlyphAttribute#effectStrategy)设置动效。

**类型：** [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2SymbolIcon-public activated?: SymbolGlyphModifier--><!--Device-ChipV2SymbolIcon-public activated?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## normal

```TypeScript
public normal?: SymbolGlyphModifier
```

非激活时图标设定。

默认值：不显示前缀图标或后缀图标。

值为undefined时，按默认值处理。

不支持使用[SymbolEffect](SymbolGlyphAttribute#symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean))修改动效类型及  
[effectStrategy](SymbolGlyphAttribute#effectStrategy)设置动效。

**类型：** [SymbolGlyphModifier](../arkts-components/arkts-arkui-symbolglyphmodifier-t.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2SymbolIcon-public normal?: SymbolGlyphModifier--><!--Device-ChipV2SymbolIcon-public normal?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
