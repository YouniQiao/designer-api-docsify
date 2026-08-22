# ListScroller

Scroll controller for list component.

**Inheritance/Implementation:** ListScroller extends Scroller

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class ListScroller--><!--Device-unnamed-export declare class ListScroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeAllSwipeActions

```TypeScript
closeAllSwipeActions(options?: CloseSwipeActionOptions): void
```

Collapses the list items in the EXPANDED state and sets callback events.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>- A &lt;em&gt;ListScroller&lt;/em&gt; must be bound to the &lt;em&gt;List&lt;/em&gt; component. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void--><!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CloseSwipeActionOptions](arkts-list-closeswipeactionoptions-i.md) | No | Callback events for collapsing list items in the EXPANDED state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## getItemRectInGroup

```TypeScript
getItemRectInGroup(index: int, indexInGroup: int): RectResult
```

Obtains the size of a list item in a list item group and its position relative to the list.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. <br>- The child component for which &lt;em&gt;index&lt;/em&gt; is set must be a list item group. Otherwise, the &lt;em&gt;index &lt;/em&gt;value is considered invalid. <br>- The value of &lt;em&gt;indexInGroup&lt;/em&gt; must be the index of a list item in the list item group visible in the display area. Otherwise, the value is considered invalid. <br>- When &lt;em&gt;index&lt;/em&gt; or &lt;em&gt;indexInGroup&lt;/em&gt; is set to an invalid value, the returned size and position are both &lt;em&gt;0&lt;/em&gt;. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-getItemRectInGroup(index: int, indexInGroup: int): RectResult--><!--Device-ListScroller-getItemRectInGroup(index: int, indexInGroup: int): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the list item group in the list. <br>The value should be an integer. |
| indexInGroup | int | Yes | Index of the list item in the list item group. <br>The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](../../apis-arkui/arkts-components/arkts-arkui-rectresult-i.md) | Size of the list item in the list item group and its position relative to the list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## getVisibleListContentInfo

```TypeScript
getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo
```

Obtains the index information of the child component at the specified coordinates.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>- If the provided value of &lt;em&gt;x&lt;/em&gt; or &lt;em&gt;y&lt;/em&gt; is invalid, the returned VisibleListContentInfo object has the &lt;em&gt;index&lt;/em&gt; property set to &lt;em&gt;-1&lt;/em&gt;, and both &lt;em&gt;itemGroupArea&lt;/em&gt; and &lt;em&gt;itemIndexInGroup&lt;/em&gt; are &lt;em&gt;undefined&lt;/em&gt;. </p>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo--><!--Device-ListScroller-getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | X-coordinate, in vp. |
| y | double | Yes | Y-coordinate, in vp. |

**Return value:**

| Type | Description |
| --- | --- |
| [VisibleListContentInfo](arkts-list-visiblelistcontentinfo-i.md) | Index information of the child component at the specified coordinates. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

## scrollToItemInGroup

```TypeScript
scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void
```

Scrolls to the specified list item in the specified list item group.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void--><!--Device-ListScroller-scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the target list item group in the current container. <br>The value should be an integer. <br>&lt;em&gt;NOTE&lt;/em&gt; <br>If the value set is a negative value or greater than the maximum index of the items in the container, the value is deemed abnormal, and no scrolling will be performed. |
| indexInGroup | int | Yes | Index of the target list item in the list item group specified by &lt;em&gt;index&lt;/em&gt;. <br>The value should be an integer. <br>&lt;em&gt;NOTE&lt;/em&gt; <br>If the value set is a negative value or greater than the maximum index of the items in the list item group, the value is deemed abnormal, and no scrolling will be performed. |
| smooth | boolean | No | Whether to enable the smooth animation for scrolling to the item with the specified index. <br>Default value: false<br/>**Note: **<br/>When the validity period is enabled, all items that pass through the system will be processed. Load and layout calculation are performed. When a large number of items are loaded, performance problems occur. The value &lt;em&gt;true&lt;/em&gt; means to enable that the smooth animation, and &lt;em&gt;false&lt;/em&gt; means the opposite.<br>Default value: &lt;em&gt;false&lt;/em&gt; |
| align | [ScrollAlign](../../apis-arkui/arkts-components/arkts-arkui-scrollalign-e.md) | No | How the list item to scroll to is aligned with the container. <br>Default value: &lt;em&gt;ScrollAlign.START&lt;/em&gt;. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100004](../../apis-arkui/errorcode-router.md#100004-incorrect-route-name) | Controller not bound to a component. |

