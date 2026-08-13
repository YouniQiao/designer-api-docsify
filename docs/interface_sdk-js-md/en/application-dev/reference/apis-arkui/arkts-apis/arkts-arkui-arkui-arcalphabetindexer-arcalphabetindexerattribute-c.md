# ArcAlphabetIndexerAttribute

In addition to the universal attributes, the following attributes are supported. In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** ArcAlphabetIndexerAttribute extends CommonMethod<ArcAlphabetIndexerAttribute>

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-declare class ArcAlphabetIndexerAttribute--><!--Device-unnamed-declare class ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcAlphabetIndexerAttribute, ArcAlphabetIndexer } from '@kit.ArkUI';
```

## autoCollapse

```TypeScript
autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute
```

Sets whether to enable the adaptive collapse behavior for the indexer.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-autoCollapse(enable: Optional<boolean>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | Optional&lt;boolean&gt; | Yes | Whether to enable the adaptive collapse behavior for the indexer.&lt;br&gt;Default value: **true**.&lt;br&gt;**true**: Enable the adaptive collapse behavior.&lt;br&gt;**false**: Disable the adaptive collapse behavior. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## color

```TypeScript
color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the text color of the index items in the normal state.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-color(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Text color.&lt;br&gt;Default value: **0xFFFFFF**, displayed as white |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## font

```TypeScript
font(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

Sets the default font style of the index items.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-font(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | Yes | Default font style of the index items.&lt;br&gt;Default value:&lt;br&gt;{&lt;br&gt;size:'13.0fp',&lt;br &gt; style:FontStyle.Normal,&lt;br&gt; weight:500,&lt;br&gt; family:'HarmonyOS Sans'&lt;br&gt;} |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## itemSize

```TypeScript
itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute
```

Sets the size of the index item area.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-itemSize(size: Optional<LengthMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | Optional&lt;LengthMetrics&gt; | Yes | Size of the index item area. For the circular item area, this represents the diameter of the circle. Percentage values are not supported.&lt;br&gt;Default value: **24.0**&lt;br&gt;Unit: vp |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## onSelect

```TypeScript
onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute
```

Triggered when an index item is selected. The return value is the index of the selected item.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-onSelect(handler: Optional<OnSelectCallback>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | Optional&lt;[OnSelectCallback](../../apis-na/arkts-apis/arkts-na-onselectcallback-t.md)&gt; | Yes | Callback used to return the result. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupBackground

```TypeScript
popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the background color of the pop-up window.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupBackground(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Background color of the pop-up window.&lt;br&gt;Default value: **0xD8404040**, displayed as dark gray with slight transparency |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupBackgroundBlurStyle

```TypeScript
popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute
```

Sets the background blur style of the pop-up window. If this API is not used, the blur is disabled by default. The corresponding value is **NONE** in **BlurStyle**. > **NOTE：**> After configuring the pop-up window background blur style with **popupBackgroundBlurStyle**, avoid applying > background colors via [popupBackground](#popupBackground).

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupBackgroundBlurStyle(style: Optional<BlurStyle>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | Optional&lt;BlurStyle&gt; | Yes | Background blur style of the pop-up window. |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupColor

```TypeScript
popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the text color for the pop-up window.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Text color of the pop-up window.&lt;br&gt;Default value: **0xFFFFFF**, displayed as white |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## popupFont

```TypeScript
popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

Sets the font style of the pop-up window.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-popupFont(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | Yes | Font style of the pop-up window.&lt;br&gt;Default value:&lt;br&gt;{&lt;br&gt;size:'19.0fp',&lt;br&gt; style:FontStyle.Normal,&lt;br&gt; weight:500,&lt;br&gt; family:'HarmonyOS Sans'&lt;br&gt;} |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selected

```TypeScript
selected(index: Optional<number>): ArcAlphabetIndexerAttribute
```

Sets the index of the selected item.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<number>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selected(index: Optional<number>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | Optional&lt;number&gt; | Yes | Index of the selected item.&lt;br&gt;Default value: **0**&lt;br&gt;This parameter supports two-way binding through [!!](../../../ui/state-management/arkts-new-binding.md). |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selectedBackgroundColor

```TypeScript
selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the background color of the selected item.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedBackgroundColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Background color of the selected item.&lt;br&gt;Default value: **0x1F71FF**, displayed as dark blue |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selectedColor

```TypeScript
selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute
```

Sets the text color of the selected item.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedColor(color: Optional<ColorMetrics>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Optional&lt;ColorMetrics&gt; | Yes | Text color of the selected item.&lt;br&gt;Default value: **0xFFFFFF**, displayed as white |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## selectedFont

```TypeScript
selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute
```

Sets the font style of the selected item, including size, weight, style, and font family.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-selectedFont(font: Optional<Font>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | Optional&lt;Font&gt; | Yes | Font style of the selected item.&lt;br&gt;Default value: {&lt;br&gt;size:'13.0fp',&lt;br&gt; style: FontStyle.Normal,&lt;br&gt; weight:500,&lt;br&gt; family:'HarmonyOS Sans'&lt;br&gt;} |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

## usePopup

```TypeScript
usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute
```

Sets whether to display the pop-up window.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute--><!--Device-ArcAlphabetIndexerAttribute-usePopup(enabled: Optional<boolean>): ArcAlphabetIndexerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | Optional&lt;boolean&gt; | Yes | Whether to display the pop-up window.&lt;br&gt;**true**: yes; **false**: no&lt;br&gt; Default value: **false |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcAlphabetIndexerAttribute](arkts-arkui-arkui-arcalphabetindexer-arcalphabetindexerattribute-c.md) |  |

