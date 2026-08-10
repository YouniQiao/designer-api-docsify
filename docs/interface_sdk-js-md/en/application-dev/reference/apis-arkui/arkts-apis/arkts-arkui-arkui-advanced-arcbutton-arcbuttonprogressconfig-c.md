# ArcButtonProgressConfig

ArcButton内进度条的参数配置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ArcButtonProgressConfig--><!--Device-unnamed-export declare class ArcButtonProgressConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcButtonPosition, ArcButton, ArcButtonStatus, ArcButtonStyleMode, ArcButtonOptions, ArcButtonProgressConfig } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(value: double, total?: double, color?: ResourceColor)
```

进度条参数配置的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-constructor(value: double, total?: double, color?: ResourceColor)--><!--Device-ArcButtonProgressConfig-constructor(value: double, total?: double, color?: ResourceColor)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | 设置进度条的进度值。&lt;br/&gt;取值范围：[0, total]，当设置小于0的值时，按0处理；当设置大于total的值时，按total处理。 |
| total | double | No | 设置进度条的总进度值。&lt;br/&gt;默认值：100&lt;br/&gt;取值范围：[0, 2147483647] |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) | No | 设置进度条的前景颜色。 |

## color

```TypeScript
public color?: ResourceColor
```

进度条前景色。如果组件设置了[ArcButtonOptions](arkts-arkui-arkui-advanced-arcbutton-arcbuttonoptions-c.md)的背景色（backgroundColor），进度条前景色默认值取组件背景色。进度条前景色不受按钮样式（  
[ArcButtonStyleMode](arkts-arkui-arkui-advanced-arcbutton-arcbuttonstylemode-e.md)）设置影响。进度条背景色仅依赖进度条前景色设置，取进度条前景色的25%透明度。 

默认值："#1F71FF"，显示为蓝色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-public color?: ResourceColor--><!--Device-ArcButtonProgressConfig-public color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## total

```TypeScript
public total?: double
```

进度的最大值。

默认值：100

取值范围：[0, 2147483647]，设置0或超出取值范围取默认值为100。

**Type:** double

**Default:** 100

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-public total?: double--><!--Device-ArcButtonProgressConfig-public total?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## value

```TypeScript
public value: double
```

进度条当前值。设置小于0的数值时置为0，设置大于total的数值时置为total。

默认值：0

取值范围：[0, total]

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcButtonProgressConfig-public value: double--><!--Device-ArcButtonProgressConfig-public value: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

