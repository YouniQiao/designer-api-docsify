# DynamicLayoutAttribute

The universal attributes are supported. &gt; **NOTE：**&gt; &gt; - When the layout algorithm is [RowLayoutAlgorithm](arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md) or &gt; [ColumnLayoutAlgorithm](arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md), &gt; the [Flex layout](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-flex-layout.md) attributes set &gt; for child components take effect. &gt; &gt; - When the layout algorithm is [StackLayoutAlgorithm](arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md), &gt; the layoutGravity attribute set for child components takes effect. &gt; &gt; - When the layout algorithm is &gt; [CustomLayoutAlgorithm](arkts-arkui-layoutalgorithm-customlayoutalgorithm-c.md), &gt; the [setMeasuredSize](../../apis-na/arkts-apis/arkts-na-framenode-c.md#setmeasuredsize) method of the &gt; [FrameNode](../../apis-na/arkts-apis/arkts-na-framenode-c.md) component of **DynamicLayout** has a higher priority than the &gt; sizing and border styling attributes. The &gt; [measure](../../apis-na/arkts-apis/arkts-na-framenode-c.md#measure) and [layout](../../apis-na/arkts-apis/arkts-na-framenode-c.md#layout) methods &gt; of the child component [FrameNode](../../apis-na/arkts-apis/arkts-na-framenode-c.md) have a higher priority than the &gt; ignoreLayoutSafeArea attribute. The [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md) are supported.

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

