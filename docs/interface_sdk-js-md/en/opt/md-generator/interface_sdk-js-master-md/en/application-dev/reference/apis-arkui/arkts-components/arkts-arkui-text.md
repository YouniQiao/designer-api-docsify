# Text

The **Text** component is used to display a piece of textual information.

## Child Components

This component can contain the [Span]{@link ./span}, [ImageSpan]{@link ./image_span},  
[SymbolSpan]{@link ./symbol_span}, and [ContainerSpan]{@link ./container_span} child components.

> **NOTE：**
> 
> Use [child components](docroot://reference/apis-arkui/arkui-ts/ts-basic-components-text.md#child-components) to
> implement [text and image layout](docroot://ui/arkts-text-image-layout.md) scenarios.

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| content | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | No |
| value | [TextOptions](arkts-arkui-textoptions-i.md) | No |

## Summary

- [TextMarqueeOptions](arkts-arkui-text-textmarqueeoptions-i.md)
- [TextOptions](arkts-arkui-text-textoptions-i.md)
- [TextOverflowOptions](arkts-arkui-text-textoverflowoptions-i.md)
- [MarqueeStartPolicy](arkts-arkui-text-marqueestartpolicy-e.md)
- [MarqueeState](arkts-arkui-text-marqueestate-e.md)
- [MarqueeUpdatePolicy](arkts-arkui-text-marqueeupdatepolicy-e.md)
- [TextResponseType](arkts-arkui-text-textresponsetype-e.md)
- [TextSpanType](arkts-arkui-text-textspantype-e.md)
