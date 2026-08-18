# ListScroller

List组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。 > **说明：** > > ListScroller继承自[Scroller](arkts-arkui-scroller-c.md#scroller)，具有[Scroller](arkts-arkui-scroller-c.md#scroller)的全部方法。

## 导入对象 ```ts listScroller: ListScroller = new ListScroller(); ```

**继承/实现关系：** ListScroller extends [Scroller](arkts-arkui-scroller-c.md#scroller)

**起始版本：** 11

<!--Device-unnamed-declare class ListScroller--><!--Device-unnamed-declare class ListScroller-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## closeAllSwipeActions

```TypeScript
closeAllSwipeActions(options?: CloseSwipeActionOptions): void
```

将[EXPANDED](arkts-arkui-swipeactionstate-e.md#swipeactionstate)状态的ListItem收起，并设置回调事件。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void--><!--Device-ListScroller-closeAllSwipeActions(options?: CloseSwipeActionOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CloseSwipeActionOptions](arkts-arkui-closeswipeactionoptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## getItemRectInGroup

```TypeScript
getItemRectInGroup(index: number, indexInGroup: number): RectResult
```

获取ListItemGroup中的ListItem的大小和相对于List的位置。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ListScroller-getItemRectInGroup(index: number, indexInGroup: number): RectResult--><!--Device-ListScroller-getItemRectInGroup(index: number, indexInGroup: number): RectResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| indexInGroup | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RectResult](arkts-arkui-rectresult-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## getVisibleListContentInfo

```TypeScript
getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo
```

根据坐标获取子组件的索引信息。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-ListScroller-getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo--><!--Device-ListScroller-getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [VisibleListContentInfo](arkts-arkui-visiblelistcontentinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## scrollToItemInGroup

```TypeScript
scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void
```

滑动到指定的ListItemGroup中指定的ListItem。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ListScroller-scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void--><!--Device-ListScroller-scrollToItemInGroup(index: number, indexInGroup:number, smooth?: boolean, align?: ScrollAlign): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| indexInGroup | number | 是 |
| smooth | boolean | 否 |
| align | [ScrollAlign](arkts-arkui-scrollalign-e.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |
