# ListScroller

List组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。

> **说明：**
> 
> ListScroller继承自[Scroller](arkts-arkui-scroll-scroller-c.md)，具有[Scroller](arkts-arkui-scroll-scroller-c.md)的全部方法。

**Inheritance/Implementation:** ListScroller extends [Scroller](arkts-arkui-scroll-scroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class ListScroller extends Scroller--><!--Device-unnamed-export declare class ListScroller extends Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeAllSwipeActions

```TypeScript
closeAllSwipeActions(options?: CloseSwipeActionOptions): void
```

将[EXPANDED](arkts-arkui-listitem-swipeactionstate-e.md)状态的[ListItem](list_item)收起，并设置回调事件。

&lt;p&gt;&lt;strong&gt;注意&lt;/strong&gt;：&lt;br&gt;-一个&lt;em&gt;ListScroller&lt;/em&gt;必须绑定到&lt;em&gt;List&lt;/em&gt;组件。&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void--><!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CloseSwipeActionOptions](arkts-arkui-list-closeswipeactionoptions-i.md) | No | 收起[EXPANDED](arkts-arkui-listitem-swipeactionstate-e.md)状态的[ListItem](list_item) 的回调事件集合。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## getItemRectInGroup

```TypeScript
getItemRectInGroup(index: int, indexInGroup: int): RectResult
```

获取[ListItemGroup](list_item_group)中的[ListItem](list_item)的大小和相对于List的位置。

&lt;p&gt;&lt;strong&gt;注意&lt;/strong&gt;：&lt;br&gt;-&lt;em&gt;index&lt;/em&gt;的值必须是显示区域中可见的子组件的索引。否则，该值将被视为无效值。&lt;br&gt;-设置&lt;em&gt;index&lt;/em&gt;的子组件必须是列表项组。否则，&lt;em&gt;index &lt;/em&gt;值被认为是无效的。&lt;br&gt;-&lt;em&gt;indexInGroup&lt;/em&gt;的值必须是列表项组中某个列表项的索引在显示区域中可见。否则，该值将被视为无效值。&lt;br&gt;-当&lt;em&gt;index&lt;/em&gt;或&lt;em&gt;indexInGroup&lt;/em&gt;设置为无效值时，返回的大小和位置均为&lt;em&gt;0&lt;/em&gt;。&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-getItemRectInGroup(index: int, indexInGroup: int): RectResult--><!--Device-ListScroller-getItemRectInGroup(index: int, indexInGroup: int): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | ListItemGroup在List中的索引值。 &lt;br&gt;取值限定为整数。 |
| indexInGroup | int | Yes | ListItemGroup在List中的索引值。 &lt;br&gt;取值限定为整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](../arkts-components/arkts-arkui-rectresult-i.md) | ListItemGroup中的ListItem的大小和相对于List的位置。&lt;br/&gt;单位：vp。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## getVisibleListContentInfo

```TypeScript
getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo
```

根据坐标获取子组件的索引信息。

&lt;p&gt;&lt;strong&gt;注意&lt;/strong&gt;：&lt;br&gt;-如果提供的&lt;em&gt;x&lt;/em&gt;或&lt;em&gt;y&lt;/em&gt;的值无效，返回的VisibleListContentInfo对象的&lt;em&gt;index&lt;/em&gt;属性设置为&lt;em&gt;-1&lt;/em&gt;。且&lt;em&gt;itemGroupArea&lt;/em&gt;和&lt;em&gt;itemIndexInGroup&lt;/em&gt;均为&lt;em&gt;未定义&lt;/em&gt;。&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo--><!--Device-ListScroller-getVisibleListContentInfo(x: double, y: double): VisibleListContentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | x轴坐标，单位为vp。 |
| y | double | Yes | y轴坐标，单位为vp。 |

**Return value:**

| Type | Description |
| --- | --- |
| [VisibleListContentInfo](../arkts-components/arkts-arkui-visiblelistcontentinfo-i.md) | 入参坐标处的子组件的索引信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## scrollToItemInGroup

```TypeScript
scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void
```

滑动到指定的ListItemGroup中指定的ListItem。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListScroller-scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void--><!--Device-ListScroller-scrollToItemInGroup(index: int, indexInGroup: int, smooth?: boolean, align?: ScrollAlign): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 要滑动到的目标元素所在的ListItemGroup在当前容器中的索引值。 &lt;br/&gt;**说明：** &lt;br/&gt;index值设置成负值或者大于当前容器子组件的最大索引值，视 为异常值，本次跳转不生效。 &lt;br&gt;取值限定为整数。 &lt;br&gt; &lt;em&gt;注意&lt;/em&gt; &lt;br&gt;如果设置的值为负值或大于容器中项目的最大索引，则 则认为值异常，不进行滚动。 |
| indexInGroup | int | Yes | 要滑动到的目标元素所在的ListItemGroup在当前容器中的索引值。 &lt;br/&gt;**说明：** &lt;br/&gt;index值设置成负值或者大于当前容器子组件的最大索引值，视 为异常值，本次跳转不生效。 &lt;br&gt;取值限定为整数。 &lt;br&gt; &lt;em&gt;注意&lt;/em&gt; &lt;br&gt;如果设置的值为负值或大于容器中项目的最大索引，则 则认为值异常，不进行滚动。 |
| smooth | boolean | No | 设置该次滑动是否有动效，true表示有动效，false表示没有动效。&lt;br/&gt;。 &lt;br&gt;默认值：false&lt;br/&gt;**说明：** &lt;br/&gt;开启动效时，会对经过的所有item 进行加载和布局计算，当大量加载item时会导致性能问题。 |
| align | [ScrollAlign](../arkts-components/arkts-arkui-scrollalign-e.md) | No | 指定滑动到的元素与当前容器的对齐方式。&lt;br/&gt;。 &lt;br&gt;默认值：&lt;em&gt;ScrollAlign.START&lt;/em&gt;。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

