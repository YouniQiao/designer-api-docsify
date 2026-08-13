# @ohos.arkui.components.ArkDynamicLayout

## Modules to Import

```TypeScript
import { DynamicLayoutAttribute, DynamicLayout } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md) | The universal attributes are supported. > **NOTE：**> > - When the layout algorithm is [RowLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-rowlayoutalgorithm-c.md#RowLayoutAlgorithm) or > [ColumnLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-columnlayoutalgorithm-c.md#ColumnLayoutAlgorithm), > the [Flex layout](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-flex-layout.md) attributes set > for child components take effect. > > - When the layout algorithm is [StackLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-stacklayoutalgorithm-c.md#StackLayoutAlgorithm), > the layoutGravity attribute set for child components takes effect. > > - When the layout algorithm is > [CustomLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-customlayoutalgorithm-c.md#CustomLayoutAlgorithm), > the [setMeasuredSize](arkts-arkui-framenode-c.md#setMeasuredSize) method of the > [FrameNode](arkts-arkui-framenode-c.md#FrameNode) component of **DynamicLayout** has a higher priority than the > sizing and border styling attributes. The > [measure](arkts-arkui-framenode-c.md#measure) and [layout](arkts-arkui-framenode-c.md#layout) methods > of the child component [FrameNode](arkts-arkui-framenode-c.md#FrameNode) have a higher priority than the > ignoreLayoutSafeArea attribute. The [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md) are supported. |

### Interfaces

| Name | Description |
| --- | --- |
| [DynamicLayoutInterface](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutinterface-i.md) | Defines the dynamic layout container. |

### Constants

| Name | Description |
| --- | --- |
| [DynamicLayout](arkts-arkui-arkui-components-arkdynamiclayout-con.md#DynamicLayout) | Defines the dynamic layout container component, which supports dynamically switching between different layout algorithms at runtime without changing the status of child components. > **Child Components** > > Child components are supported. |
| [DynamicLayoutInstance](arkts-arkui-arkui-components-arkdynamiclayout-con.md#DynamicLayoutInstance) | Defines DynamicLayout Component instance. |

