# TextController

Defines the controller of the **Text** component.

## Objects to Import

```ts controller: TextController = new TextController()```

**Since:** 11

<!--Device-unnamed-declare class TextController--><!--Device-unnamed-declare class TextController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

Closes the custom or default text selection menu.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextController-closeSelectionMenu(): void--><!--Device-TextController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager
```

Obtains the **LayoutManager** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextController-getLayoutManager(): LayoutManager--><!--Device-TextController-getLayoutManager(): LayoutManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LayoutManager](../arkts-apis/arkts-arkui-layoutmanager-i.md) |

## setStyledString

```TypeScript
setStyledString(value: StyledString): void
```

Binds to or updates the specified styled string.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextController-setStyledString(value: StyledString): void--><!--Device-TextController-setStyledString(value: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | Yes |

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number | undefined, selectionEnd: number | undefined,
                   options?: SelectionOptions): void
```

Sets the text selection area, which will be highlighted.

> **NOTE：**
> 
> If [copyOption](TextAttribute#copyOption) is set to **CopyOptions.None**, the setting of
> **setTextSelection** does not take effect.
> 
> If [textOverflow](TextAttribute#textOverflow) is set to **TextOverflow.MARQUEE**, the setting of
> **setTextSelection** does not take effect.
> 
> If the value of **selectionStart** is greater than or equal to that of **selectionEnd**, no text will be
> selected. The value range is [0, textSize], where **textSize** indicates the maximum number of characters in the
> text content. If the value is less than 0, the value **0** will be used. If the value is greater than
> **textSize**, **textSize** will be used.
> 
> If the selection range falls within a truncated or invisible area, selection is ignored. When truncation is
> disabled, selection can extend beyond the parent component's bounds.
> 
> On PC or 2-in-1 devices, calling **setTextSelection** does not show the menu even if **options** is set to
> **MenuPolicy.SHOW**.
> 
> When an emoji is truncated by the selection range, the emoji is selected if its start position is within the
> specified text selection range.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-TextController-setTextSelection(selectionStart: number | undefined, selectionEnd: number | undefined,                   options?: SelectionOptions): void--><!--Device-TextController-setTextSelection(selectionStart: number | undefined, selectionEnd: number | undefined,                   options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectionStart | number \| undefined | Yes |
| selectionEnd | number \| undefined | Yes |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | No |
