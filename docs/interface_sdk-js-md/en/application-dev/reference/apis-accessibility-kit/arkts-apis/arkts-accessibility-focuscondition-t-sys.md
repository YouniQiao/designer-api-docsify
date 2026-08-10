# FocusCondition (System API)

```TypeScript
export type FocusCondition = 'forward' | 'backward' |
'findLast' | 'getForwardScrollAncestor' | 'getBackwardScrollAncestor' | 'getScrollableAncestor'
```

表示查询可聚焦节点方式。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export type FocusCondition = 'forward' | 'backward' |'findLast' | 'getForwardScrollAncestor' | 'getBackwardScrollAncestor' | 'getScrollableAncestor'--><!--Device-unnamed-export type FocusCondition = 'forward' | 'backward' |'findLast' | 'getForwardScrollAncestor' | 'getBackwardScrollAncestor' | 'getScrollableAncestor'-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

| Type | Description |
| --- | --- |
| 'forward' | 表示当前节点下一个可聚焦节点，值固定为'forward' 字符串。 |
| 'backward' | 表示当前节点上一个可聚焦节点，值固定为'backward'字符串。 |
| 'findLast' | 表示查找起始节点的子节点中的最后一个节点，值固定为'findLast'字符串。 |
| 'getForwardScrollAncestor' | 表示查找支持前向滚动父组件，值固定为'getForwardScrollAncestor'字符串。 |
| 'getBackwardScrollAncestor' | 表示查找支持后向滚动父组件，值固定为'getBackwardScrollAncestor'字符串。 |
| 'getScrollableAncestor' | 表示查找支持任意滚动父组件，值固定为'getScrollableAncestor'字符串。 |

