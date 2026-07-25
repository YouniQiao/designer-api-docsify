# ChipV2SuffixSymbolIcon

ChipV2SuffixSymbolIcon定义后缀Symbol图标类。

继承自[ChipV2SymbolIcon](arkts-arkui-arkui-advanced-chipv2-chipv2symbolicon-c.md)。

**继承/实现关系：** ChipV2SuffixSymbolIcon extends [ChipV2SymbolIcon](arkts-arkui-arkui-advanced-chipv2-chipv2symbolicon-c.md)

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export declare class ChipV2SuffixSymbolIcon extends ChipV2SymbolIcon--><!--Device-unnamed-export declare class ChipV2SuffixSymbolIcon extends ChipV2SymbolIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ChipV2SuffixSymbolIconConfig, ChipV2Label, ChipV2PrefixSymbolIconConfig, IChipV2OptionsConfig, ChipV2SymbolIcon, ChipV2SuffixImageIconConfig, ChipV2LocalizedLabelMarginConfig, ChipV2SymbolIconConfig, ChipV2LabelConfig, ChipV2SuffixSymbolIcon, ChipV2AccessibilityConfig, ChipV2Icon, ChipV2Size, ChipV2CloseConfig, ChipV2SuffixImageIcon, ChipV2Accessibility, ChipV2Options, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2PrefixImageIcon, ChipV2LabelMarginConfig, ChipV2PrefixSymbolIcon, ChipV2, ChipV2CloseIcon, ChipV2PrefixImageIconConfig, ChipV2AccessibilitySelectedType } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(config: ChipV2SuffixSymbolIconConfig)
```

ChipV2SuffixSymbolIcon的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2SuffixSymbolIcon-constructor(config: ChipV2SuffixSymbolIconConfig)--><!--Device-ChipV2SuffixSymbolIcon-constructor(config: ChipV2SuffixSymbolIconConfig)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ChipV2SuffixSymbolIconConfig](arkts-arkui-arkui-advanced-chipv2-chipv2suffixsymboliconconfig-i.md) | 是 | 后缀Symbol图标属性配置，用于设置后缀Symbol图标的显示属性和无障碍功能，继承自ChipV2SymbolIconConfig，包含normal、activated、normalAccessibility、activatedAccessibility、action等配置项。 |

## action

```TypeScript
public action?: VoidCallback
```

后缀图标点击事件回调函数。点击后缀图标时调用此回调函数。

默认值：不设定后缀图标事件。

值为undefined时，按默认值处理。

**类型：** VoidCallback

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2SuffixSymbolIcon-public action?: VoidCallback--><!--Device-ChipV2SuffixSymbolIcon-public action?: VoidCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## activatedAccessibility

```TypeScript
public activatedAccessibility?: ChipV2Accessibility
```

激活态无障碍朗读功能属性。

默认值：undefined，无朗读内容。

**类型：** ChipV2Accessibility

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2SuffixSymbolIcon-public activatedAccessibility?: ChipV2Accessibility--><!--Device-ChipV2SuffixSymbolIcon-public activatedAccessibility?: ChipV2Accessibility-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## normalAccessibility

```TypeScript
public normalAccessibility?: ChipV2Accessibility
```

非激活态无障碍朗读功能属性。

默认值：undefined，无朗读内容。

**类型：** ChipV2Accessibility

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2SuffixSymbolIcon-public normalAccessibility?: ChipV2Accessibility--><!--Device-ChipV2SuffixSymbolIcon-public normalAccessibility?: ChipV2Accessibility-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

