# ArcAlphabetIndexerAttribute

In addition to the universal attributes, the following attributes are supported. In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** ArcAlphabetIndexerAttribute extends CommonMethod<ArcAlphabetIndexerAttribute>

**Since:** 18

<!--Device-unnamed-declare class ArcAlphabetIndexerAttribute--><!--Device-unnamed-declare class ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
```

## autoCollapse

```TypeScript
autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute
```

Sets whether to enable the adaptive collapse behavior for the indexer.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## color

```TypeScript
color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the text color of the index items in the normal state.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [color](#color) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## font

```TypeScript
font(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

Sets the default font style of the index items.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [font](#font) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;Font&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## itemSize

```TypeScript
itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute
```

Sets the size of the index item area.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## onSelect

```TypeScript
onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute
```

Triggered when an index item is selected. The return value is the index of the selected item.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[OnSelectCallback](arkts-arkui-onselectcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## popupBackground

```TypeScript
popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the background color of the pop-up window.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [color](#color) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute
```

Sets the background blur style of the pop-up window. If this API is not used, the blur is disabled by default. The corresponding value is **NONE** in **BlurStyle**. > **NOTE：**> After configuring the pop-up window background blur style with **popupBackgroundBlurStyle**, avoid applying > background colors via [popupBackground](#popupbackground).

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;BlurStyle&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## popupColor

```TypeScript
popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the text color for the pop-up window.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [color](#color) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## popupFont

```TypeScript
popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

Sets the font style of the pop-up window.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [font](#font) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;Font&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## selected

```TypeScript
selected(index: Optional<number>): ArcAlphabetIndexerAttribute
```

Sets the index of the selected item.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<number>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<number>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the background color of the selected item.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [color](#color) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## selectedColor

```TypeScript
selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the text color of the selected item.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [color](#color) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## selectedFont

```TypeScript
selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

Sets the font style of the selected item, including size, weight, style, and font family.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [font](#font) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;Font&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |

## usePopup

```TypeScript
usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute
```

Sets whether to display the pop-up window.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |
