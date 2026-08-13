# Text

The **Text** component is used to display a piece of textual information.

## Child Components This component can contain the Span, ImageSpan, SymbolSpan, and ContainerSpan child components. > **NOTE** > > Use [child components](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#child-components) to > implement [text and image layout](../../../ui/arkts-text-image-layout.md) scenarios.

## Text

```TypeScript
Text(content?: string | Resource, value?: TextOptions)
```

Defines the constructor of Text.

**Since:** 7

**Deprecated since:** -1

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

- [TextMarqueeOptions](arkts-arkui-textmarqueeoptions-i.md)
- [TextOptions](arkts-arkui-textoptions-i.md)
- [TextOverflowOptions](arkts-arkui-textoverflowoptions-i.md)
- [MarqueeStartPolicy](arkts-arkui-marqueestartpolicy-e.md)
- [MarqueeState](arkts-arkui-marqueestate-e.md)
- [MarqueeUpdatePolicy](arkts-arkui-marqueeupdatepolicy-e.md)
- [TextResponseType](arkts-arkui-textresponsetype-e.md)
- [TextSpanType](arkts-arkui-textspantype-e.md)
