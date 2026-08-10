# ListScroller

List组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。

> **说明：**
> 
> ListScroller继承自[Scroller](../arkts-apis/arkts-arkui-scroll-scroller-c.md/arkts-arkui-scroll-scroller-c.md)，具有[Scroller](../arkts-apis/arkts-arkui-scroll-scroller-c.md/arkts-arkui-scroll-scroller-c.md)的全部方法。

## 导入对象

```ts listScroller: ListScroller = new ListScroller();```

**Inheritance/Implementation:** ListScroller extends [Scroller](../arkts-apis/arkts-arkui-scroll-scroller-c.md/arkts-arkui-scroll-scroller-c.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare class ListScroller extends Scroller--><!--Device-unnamed-declare class ListScroller extends Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeAllSwipeActions

```TypeScript
closeAllSwipeActions(options?: CloseSwipeActionOptions): void
```

将[EXPANDED](../arkts-apis/arkts-arkui-listitem-swipeactionstate-e.md/arkts-arkui-listitem-swipeactionstate-e.md)状态的[ListItem](./list_item)收起，并设置回调事件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void--><!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CloseSwipeActionOptions](../arkts-apis/arkts-arkui-list-closeswipeactionoptions-i.md) | No | 收起[EXPANDED](../arkts-apis/arkts-arkui-listitem-swipeactionstate-e.md/arkts-arkui-listitem-swipeactionstate-e.md)状态的[ListItem](./list_item)的回 调事件集合。不传入时不设置回调事件。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## getItemRectInGroup

```TypeScript
getItemRectInGroup(index: number, indexInGroup: number): RectResult
```

获取[ListItemGroup](./list_item_group)中的[ListItem](./list_item)的大小和相对于List的位置。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ListScroller-getItemRectInGroup(index: number, indexInGroup: number): RectResult--><!--Device-ListScroller-getItemRectInGroup(index: number, indexInGroup: number): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | ListItemGroup在List中的索引值。 |
| indexInGroup | number | Yes | ListItem在ListItemGroup中的索引值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](arkts-arkui-rectresult-i.md) | ListItemGroup中的ListItem的大小和相对于List的位置。&lt;br/&gt;单位：vp。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## getVisibleListContentInfo

```TypeScript
getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo
```

根据坐标获取子组件的索引信息。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ListScroller-getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo--><!--Device-ListScroller-getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | x轴坐标，单位为vp。 |
| y | number | Yes | y轴坐标，单位为vp。 |

**Return value:**

| Type | Description |
| --- | --- |
| [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) | 入参坐标处的子组件的索引信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## scrollToItemInGroup

```TypeScript
scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void
```

滑动到指定的ListItemGroup中指定的ListItem。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ListScroller-scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void--><!--Device-ListScroller-scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 要滑动到的目标元素所在的ListItemGroup在当前容器中的索引值。 &lt;br/&gt;**说明：** &lt;br/&gt;index值设置成负值或者大于当前容器子组件的最大索引值， 视为异常值，本次跳转不生效。 |
| indexInGroup | number | Yes | 要滑动到的目标元素在index指定的ListItemGroup中的索引值。 &lt;br/&gt;**说明：** &lt;br/&gt;indexInGroup值设置成负值或者大 于index指定的ListItemGroup容器子组件的最大索引值，视为异常值，本次跳转不生效。 |
| smooth | boolean | No | 设置该次滑动是否有动效，true表示有动效，false表示没有动效。&lt;br/&gt;默认值：false&lt;br/&gt;**说明：** &lt;br/&gt;开启动效时，会对经过的所有item进行加载 和布局计算，当大量加载item时会导致性能问题。 |
| align | [ScrollAlign](arkts-arkui-scrollalign-e.md) | No | 指定滑动到的元素与当前容器的对齐方式。&lt;br/&gt;默认值：ScrollAlign.START。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

