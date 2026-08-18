# Text

The **Text** component is used to display a piece of textual information.

## Child Components This component can contain the Span, ImageSpan, SymbolSpan, and ContainerSpan child components. > **NOTE** > > Use [child components](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#child-components) to > implement [text and image layout](../../../ui/arkts-text-image-layout.md) scenarios.

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
| [TextMarqueeOptions](arkts-arkui-textmarqueeoptions-i.md) | Describes the initialization options of the **Marquee** component. |
| [TextOptions](arkts-arkui-textoptions-i.md) | Describes the initialization options of the **Text** component. |
| [TextOverflowOptions](arkts-arkui-textoverflowoptions-i.md) | Defines the configuration object for text overflow behavior. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |

### Enums

| Name | Description |
| --- | --- |
| [MarqueeStartPolicy](arkts-arkui-marqueestartpolicy-e.md) | Enumerates the marquee scrolling modes. |
| [MarqueeState](arkts-arkui-marqueestate-e.md) | Enumerates the return values of the marquee state callback. |
| [MarqueeUpdatePolicy](arkts-arkui-marqueeupdatepolicy-e.md) | Sets the scrolling policy of the marquee after its attributes are updated. |
| [TextResponseType](arkts-arkui-textresponsetype-e.md) | Response type of the menu. > **NOTE：**> > The system follows the priority order below when determining the menu type to display during text interactions: > |
| [TextSpanType](arkts-arkui-textspantype-e.md) | Provides the span type information. > **NOTE：**> > The system follows the priority order below when determining the menu type to display during text interactions: > |

