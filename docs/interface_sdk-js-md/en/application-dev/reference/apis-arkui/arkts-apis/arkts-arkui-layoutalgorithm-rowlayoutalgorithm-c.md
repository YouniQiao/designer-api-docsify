# RowLayoutAlgorithm

水平方向线性布局算法类。

> **说明：**
> 
> RowLayoutAlgorithm类对象可以作为
> [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md)组件的入参指定布局算法。

**Inheritance/Implementation:** RowLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class RowLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class RowLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: RowLayoutAlgorithmOptions)
```

水平方向线性布局算法类的构造函数。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)--><!--Device-RowLayoutAlgorithm-constructor(option?: RowLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [RowLayoutAlgorithmOptions](arkts-arkui-layoutalgorithm-rowlayoutalgorithmoptions-i.md) | No | 水平方向线性布局算法的构造入参， 设置布局算法的间距、主轴对齐方式、交叉轴对齐方式及主轴排列方向。 |

## alignItems

```TypeScript
public alignItems?: VerticalAlign
```

所有子组件在垂直方向上的对齐格式。非法值：按默认值处理。

**Type:** [VerticalAlign](arkts-arkui-enums-verticalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RowLayoutAlgorithm-public alignItems?: VerticalAlign--><!--Device-RowLayoutAlgorithm-public alignItems?: VerticalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

```TypeScript
public isReverse?: boolean
```

子组件在水平方向上的排列是否反转。取值为true表示子组件在水平方向上反转排列，由于水平方向受通用属性  
[direction](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-location.md#direction)影响，如果[direction](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-location.md#direction)属性生效，再做一次反转。取值为false表示子组件在水平方向上正序排列。非法值：按默认值处理。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RowLayoutAlgorithm-public isReverse?: boolean--><!--Device-RowLayoutAlgorithm-public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
public justifyContent?: FlexAlign
```

所有子组件在水平方向上的对齐格式。非法值：按默认值处理。

**Type:** [FlexAlign](arkts-arkui-enums-flexalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RowLayoutAlgorithm-public justifyContent?: FlexAlign--><!--Device-RowLayoutAlgorithm-public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
public space?: LengthMetrics
```

横向布局元素水平方向间距。非法值：按默认值处理。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-RowLayoutAlgorithm-public space?: LengthMetrics--><!--Device-RowLayoutAlgorithm-public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

