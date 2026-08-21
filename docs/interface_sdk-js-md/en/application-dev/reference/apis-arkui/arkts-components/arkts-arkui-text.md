# Text

The **Text** component is used to display a piece of textual information.

## Child Components

This component can contain the Span, ImageSpan, SymbolSpan, and ContainerSpan child components.

> **NOTE：**
> 
> Use [child components](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#child-components) to
> implement [text and image layout](../../../ui/arkts-text-image-layout.md) scenarios.

## Text

```TypeScript
Text(content?: string | Resource, value?: TextOptions)
```

Defines the constructor of Text.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextInterface-(content?: string | Resource, value?: TextOptions): TextAttribute--><!--Device-TextInterface-(content?: string | Resource, value?: TextOptions): TextAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string \| Resource | No | Plain text. This parameter takes effect when the child component Span is not included and styled string is not set.<br>Default value: **' '**<br>**NOTE**<br>Priority of displayed content: Styled string > Content of the **Span** component > Text content of the **Text** component. |
| value | [TextOptions](arkts-arkui-textoptions-i.md) | No | Initialization options of the component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |

### Enums

| Name | Description |
| --- | --- |

