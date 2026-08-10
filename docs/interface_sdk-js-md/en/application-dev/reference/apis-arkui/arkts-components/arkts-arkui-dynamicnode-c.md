# DynamicNode

Define DynamicNode.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class DynamicNode<T>--><!--Device-unnamed-declare class DynamicNode<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMove

```TypeScript
onMove(handler: Optional<OnMoveHandler>): T
```

拖拽排序数据移动回调。当父容器组件为[List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)或[Grid](../arkts-apis/arkts-arkui-grid-grid-f.md/arkts-arkui-grid-grid-f.md#grid)，并且ForEach/LazyForEach/Repeat每次迭代都生成一个ListItem或GridItem组件时才生效。调用后开启拖拽排序功能；拖拽排序离手后，如果数据位置发生变化，将触发handler回调，上报数据移动起始索引号和目标索引号。需要在回调中修改数据源，并确保数据仅顺序发生变化，才能正常执行落位动画。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>): T--><!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [Optional](../arkts-apis/arkts-arkui-optional-t.md)&lt;OnMoveHandler&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

## onMove

```TypeScript
onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T
```

拖拽排序数据移动回调。当父容器组件为[List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)或[Grid](../arkts-apis/arkts-arkui-grid-grid-f.md/arkts-arkui-grid-grid-f.md#grid)，并且ForEach/LazyForEach/Repeat每次迭代都生成一个ListItem或GridItem组件时才生效。调用后开启拖拽排序功能；拖拽排序离手后，如果数据位置发生变化，将触发handler回调，上报数据移动起始索引号和目标索引号。需要在回调中修改数据源，并确保数据仅顺序发生变化，才能正常执行落位动画。与  
[onMove](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-drag-sorting.md#onmove)相比，新增eventHandler参数，可监听长按、开始拖拽、经过其他组件、拖拽结束等拖拽阶段事件。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T--><!--Device-DynamicNode-onMove(handler: Optional<OnMoveHandler>, eventHandler: ItemDragEventHandler): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [Optional](../arkts-apis/arkts-arkui-optional-t.md)&lt;OnMoveHandler&gt; | Yes |  |
| eventHandler | [ItemDragEventHandler](arkts-arkui-itemdrageventhandler-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

