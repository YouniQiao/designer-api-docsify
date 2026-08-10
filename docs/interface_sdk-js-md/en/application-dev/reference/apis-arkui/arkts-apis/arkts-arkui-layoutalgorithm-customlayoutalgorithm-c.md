# CustomLayoutAlgorithm

自定义布局算法类。

> **说明：**
> 
> CustomLayoutAlgorithm类对象可以作为
> [DynamicLayout](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md)组件的入参指定布局算法。

**Inheritance/Implementation:** CustomLayoutAlgorithm implements [LayoutAlgorithm](arkts-arkui-layoutalgorithm-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class CustomLayoutAlgorithm implements LayoutAlgorithm--><!--Device-unnamed-export declare class CustomLayoutAlgorithm implements LayoutAlgorithm-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLayout

```TypeScript
onLayout(self: FrameNode, position: NodePosition): void
```

通过重写此函数，开发者可以自定义排列子组件的位置。ArkUI框架会在动态布局组件确定位置时，将该组件对应的FrameNode和布局位置通过onLayout传递给开发者。不允许在onLayout函数中改变状态变量。

> **说明：**
> 
> 在此函数中，开发者可以调用
> [FrameNode](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#framenode-1)的
> [getChild()](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#getchild12)方法获取子组件FrameNode，
> 调用[FrameNode](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#framenode-1)的
> [layout()](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#layout12)方法设置子组件位置，
> 参考DynamicLayout组件
> [示例1（自定义布局算法实现瀑布流布局）](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md#示例1自定义布局算法实现瀑布流布局)。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void--><!--Device-CustomLayoutAlgorithm-onLayout(self: FrameNode, position: NodePosition): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 动态布局组件在组件树上的实体节点。 |
| position | [NodePosition](arkts-arkui-nodeposition-t.md) | Yes | 动态布局组件进行布局时使用的位置信息。 |

## onMeasure

```TypeScript
onMeasure(self: FrameNode, constraint: LayoutConstraint): void
```

通过重写此函数，开发者可以自定义测量子组件的大小。ArkUI框架会在动态布局组件确定尺寸时，将该组件对应的FrameNode和布局约束通过onMeasure传递给开发者。不允许在onMeasure函数中改变状态变量。

> **说明：**
> 
> 在此函数中，开发者可以调用
> [FrameNode](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#framenode-1)的
> [getChild()](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#getchild12)方法获取子组件FrameNode，
> 调用[FrameNode](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#framenode-1)的
> [measure()](../../../reference/apis-arkui/js-apis-arkui-frameNode.md#measure12)方法测量子组件大小，
> 参考DynamicLayout组件
> [示例1（自定义布局算法实现瀑布流布局）](../../../reference/apis-arkui/arkui-ts/ts-container-dynamiclayout.md#示例1自定义布局算法实现瀑布流布局)。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void--><!--Device-CustomLayoutAlgorithm-onMeasure(self: FrameNode, constraint: LayoutConstraint): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| self | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 动态布局组件在组件树上的实体节点。 |
| constraint | [LayoutConstraint](arkts-arkui-framenode-layoutconstraint-i.md) | Yes | 动态布局组件进行测量时使用的布局约束。 |

