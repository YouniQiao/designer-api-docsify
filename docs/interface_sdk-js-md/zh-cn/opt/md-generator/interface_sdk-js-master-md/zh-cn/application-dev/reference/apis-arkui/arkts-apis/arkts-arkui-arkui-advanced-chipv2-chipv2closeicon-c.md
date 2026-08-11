# ChipV2CloseIcon

ChipV2CloseIcon用于定义ChipV2组件关闭图标的功能属性类，包括无障碍功能属性。

继承自[ChipV2Accessibility](arkts-arkui-arkui-advanced-chipv2-chipv2accessibility-c.md)。

**继承/实现关系：** ChipV2CloseIcon extends [ChipV2Accessibility](arkts-arkui-arkui-advanced-chipv2-chipv2accessibility-c.md)

**起始版本：** 26.0.0

**装饰器类型：** @ObservedV2

<!--Device-unnamed-export declare class ChipV2CloseIcon extends ChipV2Accessibility--><!--Device-unnamed-export declare class ChipV2CloseIcon extends ChipV2Accessibility-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(config: ChipV2CloseConfig)
```

ChipV2CloseIcon的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2CloseIcon-constructor(config: ChipV2CloseConfig)--><!--Device-ChipV2CloseIcon-constructor(config: ChipV2CloseConfig)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ChipV2CloseConfig](arkts-arkui-arkui-advanced-chipv2-chipv2closeconfig-i.md) | 是 |

## fontSize

```TypeScript
public fontSize?: LengthMetrics
```

设置ChipV2组件默认关闭图标的大小，不支持百分比。传入百分比时按默认值处理。

默认值：

size为ChipV2Size.SMALL时，默认值：`\$r('sys.float.chip_small_font_size')`。

size不为ChipV2Size.SMALL时，默认值：`\$r('sys.float.chip_normal_font_size')`

单位：fp

值为undefined时，按默认值处理。

**类型：** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ChipV2CloseIcon-public fontSize?: LengthMetrics--><!--Device-ChipV2CloseIcon-public fontSize?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
