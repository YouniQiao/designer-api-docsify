# ArcButtonProgressConfig

ArcButton内进度条的参数配置。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 导入模块

```TypeScript
import { ArcButton, ArcButtonOptions, ArcButtonProgressConfig, ArcButtonPosition, ArcButtonStyleMode, ArcButtonStatus } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(value: double, total?: double, color?: ResourceColor)
```

进度条参数配置的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | double | 是 |
| [total](#total) | double | 否 |
| [color](#color) | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 否 |

## color

```TypeScript
color?: ResourceColor
```

进度条前景色。如果组件设置了背景色（[backgroundColor](arkts-arkui-arkui-advanced-arcbutton-arcbuttonoptions-c.md)），进度条前景色默认值取组件背景色。进度条前景色不受按钮样式（ [ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)）设置影响。进度条背景色仅依赖进度条前景色设置，取进度条前景色的25%透明度。默认值："#1F71FF"，显示为蓝色。

**类型：** ResourceColor

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## total

```TypeScript
total?: number
```

进度的最大值。默认值：100取值范围：[0, 2147483647]，设置0或超出取值范围取默认值为100。

**类型：** number

**默认值：** 100

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## value

```TypeScript
value: number
```

进度条当前值。设置小于0的数值时置为0，设置大于total的数值时置为total。默认值：0取值范围：[0, total]

**类型：** number

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle
