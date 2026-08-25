# ListScroller

Scroll controller for list component.

**Inheritance/Implementation:** ListScroller extends Scroller

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeAllSwipeActions

```TypeScript
closeAllSwipeActions(options?: CloseSwipeActionOptions): void
```

Collapses the list items in the EXPANDED state and sets callback events.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>- A &lt;em&gt;ListScroller&lt;/em&gt; must be bound to the &lt;em&gt;List&lt;/em&gt; component. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CloseSwipeActionOptions](arkts-arkui-list-closeswipeactionoptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## getItemRectInGroup

```TypeScript
getItemRectInGroup(index: int, indexInGroup: int): RectResult
```

Obtains the size of a list item in a list item group and its position relative to the list.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>- The value of &lt;em&gt;index&lt;/em&gt; must be the index of a child component visible in the display area. Otherwise, the value is considered invalid. <br>- The child component for which &lt;em&gt;index&lt;/em&gt; is set must be a list item group. Otherwise, the &lt;em&gt;index &lt;/em&gt;value is considered invalid. <br>- The value of &lt;em&gt;indexInGroup&lt;/em&gt; must be the index of a list item in the list item group visible in the display area. Otherwise, the value is considered invalid. <br>- When &lt;em&gt;index&lt;/em&gt; or &lt;em&gt;indexInGroup&lt;/em&gt; is set to an invalid value, the returned size and position are both &lt;em&gt;0&lt;/em&gt;. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | int | Yes |
| indexInGroup | int | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RectResult](../arkts-components/arkts-arkui-rectresult-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## getVisibleListContentInfo

```TypeScript
getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo
```

Obtains the index information of the child component at the specified coordinates.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>- If the provided value of &lt;em&gt;x&lt;/em&gt; or &lt;em&gt;y&lt;/em&gt; is invalid, the returned VisibleListContentInfo object has the &lt;em&gt;index&lt;/em&gt; property set to &lt;em&gt;-1&lt;/em&gt;, and both &lt;em&gt;itemGroupArea&lt;/em&gt; and &lt;em&gt;itemIndexInGroup&lt;/em&gt; are &lt;em&gt;undefined&lt;/em&gt;. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [VisibleListContentInfo](arkts-arkui-list-visiblelistcontentinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |

## scrollToItemInGroup

```TypeScript
scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void
```

Scrolls to the specified list item in the specified list item group.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | int | Yes |
| indexInGroup | int | Yes |
| [smooth](arkts-arkui-viewmodel-scrollparam-i.md) | boolean | No |
| align | [ScrollAlign](../arkts-components/arkts-arkui-scrollalign-e.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |
