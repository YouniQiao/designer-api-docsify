# StackLayoutAlgorithm

堆叠布局算法类。

> **说明：**
> 
> StackLayoutAlgorithm类对象可以作为
> [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md)组件的入参指定布局算法。

**Inheritance/Implementation:** StackLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class StackLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class StackLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(option?: StackLayoutAlgorithmOptions)
```

堆叠布局算法类的构造函数。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-StackLayoutAlgorithm-constructor(option?: StackLayoutAlgorithmOptions)--><!--Device-StackLayoutAlgorithm-constructor(option?: StackLayoutAlgorithmOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [StackLayoutAlgorithmOptions](arkts-arkui-layoutalgorithm-stacklayoutalgorithmoptions-i.md) | No | 堆叠布局算法的构造入参，设置九宫格对齐格式。 |

## alignContent

```TypeScript
public alignContent?: LocalizedAlignment
```

设置子组件在堆叠布局算法中对齐格式。非法值：按默认值处理。

**Type:** [LocalizedAlignment](arkts-arkui-enums-localizedalignment-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-StackLayoutAlgorithm-public alignContent?: LocalizedAlignment--><!--Device-StackLayoutAlgorithm-public alignContent?: LocalizedAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

