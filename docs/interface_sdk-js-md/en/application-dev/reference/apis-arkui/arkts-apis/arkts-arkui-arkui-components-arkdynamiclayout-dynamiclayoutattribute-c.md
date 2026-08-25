# DynamicLayoutAttribute

The universal attributes are supported.

> **NOTE：**&gt;
> - When the layout algorithm is [RowLayoutAlgorithm](arkts-arkui-layoutalgorithm-rowlayoutalgorithm-c.md) or
> [ColumnLayoutAlgorithm](arkts-arkui-layoutalgorithm-columnlayoutalgorithm-c.md),
> the [Flex layout](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-flex-layout.md) attributes set
> for child components take effect.&gt;
> - When the layout algorithm is [StackLayoutAlgorithm](arkts-arkui-layoutalgorithm-stacklayoutalgorithm-c.md),
> the layoutGravity attribute set for child components takes effect.&gt;
> - When the layout algorithm is
> [CustomLayoutAlgorithm](arkts-arkui-layoutalgorithm-customlayoutalgorithm-c.md),
> the [setMeasuredSize](arkts-arkui-framenode-c.md#setmeasuredsize) method of the
> [FrameNode](arkts-arkui-framenode-c.md) component of **DynamicLayout** has a higher priority than the
> sizing and border styling attributes. The
> [measure](arkts-arkui-framenode-c.md#measure) and [layout](arkts-arkui-framenode-c.md#layout) methods
> of the child component [FrameNode](arkts-arkui-framenode-c.md) have a higher priority than the
> ignoreLayoutSafeArea attribute.
The [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md) are supported.

**Inheritance/Implementation:** DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute>

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Dyn, since version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { DynamicLayout, DynamicLayoutAttribute } from '@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(
      modifier: AttributeModifier<DynamicLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Called attributeModifier.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | AttributeModifier&lt;[DynamicLayoutAttribute](arkts-arkui-arkui-components-arkdynamiclayout-dynamiclayoutattribute-c.md)&gt; \| AttributeModifier & lt;CommonMethod & gt; \ | undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |
