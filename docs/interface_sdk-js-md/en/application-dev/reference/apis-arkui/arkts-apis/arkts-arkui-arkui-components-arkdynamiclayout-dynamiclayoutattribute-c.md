# DynamicLayoutAttribute

The [universal attributes](CommonMethod) are supported.

> **NOTE：**
> 
> - When the layout algorithm is [RowLayoutAlgorithm](arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md#RowLayoutAlgorithm) or
> [ColumnLayoutAlgorithm](arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md#ColumnLayoutAlgorithm),
> the [Flex layout](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-flex-layout.md) attributes set
> for child components take effect.
> 
> - When the layout algorithm is [StackLayoutAlgorithm](arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md#StackLayoutAlgorithm),
> the [layoutGravity](CommonMethod#layoutGravity) attribute set for child components takes effect.
> 
> - When the layout algorithm is
> [CustomLayoutAlgorithm](arkts-arkui-layoutalgorithm-customlayoutalgorithm-c.md#CustomLayoutAlgorithm),
> the [setMeasuredSize](arkts-arkui-framenode-c.md#setMeasuredSize) method of the
> [FrameNode](arkts-arkui-framenode-c.md#FrameNode) component of **DynamicLayout** has a higher priority than the
> [sizing](CommonMethod#size) and [border styling](CommonMethod#border) attributes. The
> [measure](arkts-arkui-framenode-c.md#measure) and [layout](arkts-arkui-framenode-c.md#layout) methods
> of the child component [FrameNode](arkts-arkui-framenode-c.md#FrameNode) have a higher priority than the
> [ignoreLayoutSafeArea](CommonMethod#ignoreLayoutSafeArea) attribute.

The [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md) are supported.

**Inheritance/Implementation:** DynamicLayoutAttribute extends [CommonMethod<DynamicLayoutAttribute>](CommonMethod<DynamicLayoutAttribute>)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**Widget capability:** This API can be used in ArkTS widgets since API version 24.

<!--Device-unnamed-export declare class DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute>--><!--Device-unnamed-export declare class DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DynamicLayoutAttribute, DynamicLayout } from '@kit.ArkUI';
```

