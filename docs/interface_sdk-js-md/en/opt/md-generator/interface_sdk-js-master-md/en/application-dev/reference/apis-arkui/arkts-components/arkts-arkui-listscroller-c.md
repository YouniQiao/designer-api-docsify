# ListScroller

Implements the scroll controller of the **List** component. A **List** component is bound to a **ListScroller** on a one-to-one basis. > **NOTE：**> > **ListScroller** inherits from [Scroller](arkts-arkui-scroller-c.md#Scroller) and has all methods of > [Scroller](arkts-arkui-scroller-c.md#Scroller).

**Inheritance/Implementation:** ListScroller extends [Scroller](arkts-arkui-scroller-c.md#Scroller)

**Since:** 11

**Deprecated since:** -1

<!--Device-unnamed-declare class ListScroller--><!--Device-unnamed-declare class ListScroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeAllSwipeActions

```TypeScript
closeAllSwipeActions(options?: CloseSwipeActionOptions): void
```

Collapses the list items in the [EXPANDED](arkts-arkui-swipeactionstate-e.md#SwipeActionState) state and sets callback events.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void--><!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CloseSwipeActionOptions](arkts-arkui-closeswipeactionoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## getItemRectInGroup

```TypeScript
getItemRectInGroup(index: number, indexInGroup: number): RectResult
```

Obtains the size of a list item in a list item group and its position relative to the list. > **NOTE：**> > - The value of **index** must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. > - The child component for which **index** is set must be a list item group. Otherwise, the **index** value is considered invalid. > - The value of **indexInGroup** must be the index of a list item in the list item group visible in the display area. Otherwise, the value is considered invalid. > - When **index** or **indexInGroup** is set to an invalid value, the returned size and position are both **0**.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ListScroller-getItemRectInGroup(index: number, indexInGroup: number): RectResult--><!--Device-ListScroller-getItemRectInGroup(index: number, indexInGroup: number): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| indexInGroup | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectResult](arkts-arkui-rectresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## getVisibleListContentInfo

```TypeScript
getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo
```

Obtains the index information of the child component at the specified coordinates.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ListScroller-getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo--><!--Device-ListScroller-getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## scrollToItemInGroup

```TypeScript
scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void
```

Scrolls to the specified list item in the specified list item group.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ListScroller-scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void--><!--Device-ListScroller-scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| indexInGroup | number | Yes |
| [smooth](../arkts-apis/arkts-arkui-viewmodel-scrollparam-i.md) | boolean | No |
| align | [ScrollAlign](arkts-arkui-scrollalign-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |
