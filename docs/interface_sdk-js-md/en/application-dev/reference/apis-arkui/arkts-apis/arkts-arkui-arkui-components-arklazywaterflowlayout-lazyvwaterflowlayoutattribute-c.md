# LazyVWaterFlowLayoutAttribute

Defines the lazy vertical waterflow layout attribute.@extends LazyWaterFlowLayoutAttribute&lt;LazyVWaterFlowLayoutAttribute&gt;

**Inheritance/Implementation:** LazyVWaterFlowLayoutAttribute extends LazyWaterFlowLayoutAttribute<LazyVWaterFlowLayoutAttribute>

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LazyVWaterFlowLayout, LazyVWaterFlowLayoutAttribute, LazyWaterFlowLayoutAttribute } from '@kit.ArkUI';
```

## attributeModifier

```TypeScript
default attributeModifier(
      modifier: AttributeModifier<LazyVWaterFlowLayoutAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | AttributeModifier&lt;[LazyVWaterFlowLayoutAttribute](arkts-arkui-arkui-components-arklazywaterflowlayout-lazyvwaterflowlayoutattribute-c.md)&gt; \| AttributeModifier & lt;CommonMethod & gt; \ | undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## columnsTemplate

```TypeScript
columnsTemplate(value: string | ItemFillPolicy | undefined): LazyVWaterFlowLayoutAttribute
```

This parameter specifies the number of columns in the current waterflow layout.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| ItemFillPolicy \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LazyVWaterFlowLayoutAttribute](arkts-arkui-arkui-components-arklazywaterflowlayout-lazyvwaterflowlayoutattribute-c.md) |

## setLazyVWaterFlowLayoutOptions

```TypeScript
default setLazyVWaterFlowLayoutOptions(): this
```

Set LazyVWaterFlowLayout options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |
