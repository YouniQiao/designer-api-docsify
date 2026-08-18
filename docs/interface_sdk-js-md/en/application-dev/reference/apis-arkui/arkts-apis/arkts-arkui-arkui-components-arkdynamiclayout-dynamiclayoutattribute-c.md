# DynamicLayoutAttribute

The universal attributes are supported. > **NOTE：**> > - When the layout algorithm is [RowLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-rowlayoutalgorithm-c.md) or > [ColumnLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-columnlayoutalgorithm-c.md), > the [Flex layout](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-flex-layout.md) attributes set > for child components take effect. > > - When the layout algorithm is [StackLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-stacklayoutalgorithm-c.md), > the layoutGravity attribute set for child components takes effect. > > - When the layout algorithm is > [CustomLayoutAlgorithm](../../apis-na/arkts-apis/arkts-na-layoutalgorithm-customlayoutalgorithm-c.md), > the [setMeasuredSize](../../apis-na/arkts-apis/arkts-na-framenode-c.md#setmeasuredsize) method of the > [FrameNode](../../apis-na/arkts-apis/arkts-na-framenode-c.md) component of **DynamicLayout** has a higher priority than the > sizing and border styling attributes. The > [measure](../../apis-na/arkts-apis/arkts-na-framenode-c.md#measure) and [layout](../../apis-na/arkts-apis/arkts-na-framenode-c.md#layout) methods > of the child component [FrameNode](../../apis-na/arkts-apis/arkts-na-framenode-c.md) have a higher priority than the > ignoreLayoutSafeArea attribute. The [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md) are supported.

**Inheritance/Implementation:** DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute>

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-unnamed-export declare class DynamicLayoutAttribute--><!--Device-unnamed-export declare class DynamicLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

