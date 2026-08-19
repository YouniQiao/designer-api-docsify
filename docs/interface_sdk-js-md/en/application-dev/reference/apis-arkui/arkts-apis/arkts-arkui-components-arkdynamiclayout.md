# @ohos.arkui.components.ArkDynamicLayout

## Modules to Import

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md) | The universal attributes are supported. &gt; **NOTE：**&gt; &gt; - When the layout algorithm is [RowLayoutAlgorithm](arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md) or &gt; [ColumnLayoutAlgorithm](arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md), &gt; the [Flex layout](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-flex-layout.md) attributes set &gt; for child components take effect. &gt; &gt; - When the layout algorithm is [StackLayoutAlgorithm](arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md), &gt; the layoutGravity attribute set for child components takes effect. &gt; &gt; - When the layout algorithm is &gt; [CustomLayoutAlgorithm](arkts-arkui-layoutalgorithm-customlayoutalgorithm-c.md), &gt; the [setMeasuredSize](../../apis-na/arkts-apis/arkts-na-framenode-c.md#setmeasuredsize) method of the &gt; [FrameNode](../../apis-na/arkts-apis/arkts-na-framenode-c.md) component of **DynamicLayout** has a higher priority than the &gt; sizing and border styling attributes. The &gt; [measure](../../apis-na/arkts-apis/arkts-na-framenode-c.md#measure) and [layout](../../apis-na/arkts-apis/arkts-na-framenode-c.md#layout) methods &gt; of the child component [FrameNode](../../apis-na/arkts-apis/arkts-na-framenode-c.md) have a higher priority than the &gt; ignoreLayoutSafeArea attribute. The [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md) are supported. |

### Interfaces

| Name | Description |
| --- | --- |
| [DynamicLayoutInterface](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutinterface-i.md) | Defines the dynamic layout container. |

### Constants

| Name | Description |
| --- | --- |
| [DynamicLayout](arkts-arkui-arkui-components-arkdynamiclayout-con.md#dynamiclayout) | Defines the dynamic layout container component, which supports dynamically switching between different layout algorithms at runtime without changing the status of child components. &gt; **Child Components** &gt; &gt; Child components are supported. |
| [DynamicLayoutInstance](arkts-arkui-arkui-components-arkdynamiclayout-con.md#dynamiclayoutinstance) | Defines DynamicLayout Component instance. |

