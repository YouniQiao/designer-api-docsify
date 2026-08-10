# ColumnLayoutAlgorithm

垂直方向线性布局算法类。

> **说明：**
> 
> ColumnLayoutAlgorithm类对象可以作为
> [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md)组件的入参指定布局算法。

**Inheritance/Implementation:** ColumnLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ColumnLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class ColumnLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: ColumnLayoutAlgorithmOptions)
```

垂直方向线性布局算法类的构造函数。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)--><!--Device-ColumnLayoutAlgorithm-constructor(option?: ColumnLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [ColumnLayoutAlgorithmOptions](arkts-arkui-layoutalgorithm-columnlayoutalgorithmoptions-i.md) | No | 垂直方向线性布局算法的构造入参， 设置布局算法的间距、主轴对齐方式、交叉轴对齐方式及主轴排列方向。 |

## alignItems

```TypeScript
public alignItems?: HorizontalAlign
```

所有子组件在水平方向上的对齐格式。非法值：按默认值处理。

**Type:** [HorizontalAlign](arkts-arkui-enums-horizontalalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ColumnLayoutAlgorithm-public alignItems?: HorizontalAlign--><!--Device-ColumnLayoutAlgorithm-public alignItems?: HorizontalAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isReverse

```TypeScript
public isReverse?: boolean
```

子组件在垂直方向上的排列是否反转。取值为true表示子组件在垂直方向上反转排列。取值为false表示子组件在垂直方向上正序排列。非法值：按默认值处理。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ColumnLayoutAlgorithm-public isReverse?: boolean--><!--Device-ColumnLayoutAlgorithm-public isReverse?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## justifyContent

```TypeScript
public justifyContent?: FlexAlign
```

所有子组件在垂直方向上的对齐格式。非法值：按默认值处理。

**Type:** [FlexAlign](arkts-arkui-enums-flexalign-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ColumnLayoutAlgorithm-public justifyContent?: FlexAlign--><!--Device-ColumnLayoutAlgorithm-public justifyContent?: FlexAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
public space?: LengthMetrics
```

纵向布局元素垂直方向间距。非法值：按默认值处理。

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-ColumnLayoutAlgorithm-public space?: LengthMetrics--><!--Device-ColumnLayoutAlgorithm-public space?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

