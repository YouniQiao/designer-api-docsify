# AtomicServiceBar

interface AtomicServiceBar

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface AtomicServiceBar--><!--Device-unnamed-export interface AtomicServiceBar-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getBarRect

```TypeScript
getBarRect(): Frame
```

Get size and position of the bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicServiceBar-getBarRect(): Frame--><!--Device-AtomicServiceBar-getBarRect(): Frame-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Frame](../../apis-arkui/arkts-apis/arkts-arkui-graphics-frame-i.md) | The size and position of bar in vp relative to window. |

## setBackgroundColor

```TypeScript
setBackgroundColor(color: Nullable< Color | int | string>): void
```

Set the background color of the bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicServiceBar-setBackgroundColor(color: Nullable< Color | int | string>): void--><!--Device-AtomicServiceBar-setBackgroundColor(color: Nullable< Color | int | string>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Nullable&lt;Color \| int \| string&gt; | Yes | the color to set, undefined indicates using default. |

## setIconColor

```TypeScript
setIconColor(color: Nullable< Color | int | string>): void
```

Set the color of the icon on the bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicServiceBar-setIconColor(color: Nullable< Color | int | string>): void--><!--Device-AtomicServiceBar-setIconColor(color: Nullable< Color | int | string>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Nullable&lt;Color \| int \| string&gt; | Yes | the color to set to icon, undefined indicates using default. |

## setTitleContent

```TypeScript
setTitleContent(content: string): void
```

Set the title of the bar.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicServiceBar-setTitleContent(content: string): void--><!--Device-AtomicServiceBar-setTitleContent(content: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string | Yes | the content of the bar. |

## setTitleFontStyle

```TypeScript
setTitleFontStyle(font: FontStyle): void
```

Set the font style of the bar's title.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicServiceBar-setTitleFontStyle(font: FontStyle): void--><!--Device-AtomicServiceBar-setTitleFontStyle(font: FontStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| font | FontStyle | Yes | the font style of the bar's title. |

## setVisible

```TypeScript
setVisible(visible: boolean): void
```

Set the visibility of the bar, except the icon.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtomicServiceBar-setVisible(visible: boolean): void--><!--Device-AtomicServiceBar-setVisible(visible: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| visible | boolean | Yes | whether this bar is visible. |

