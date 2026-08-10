# WindowUpdateType

```TypeScript
type WindowUpdateType = 'add' | 'remove' | 'bounds' | 'active' | 'focus'
```

窗口变化类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-accessibility-type WindowUpdateType = 'add' | 'remove' | 'bounds' | 'active' | 'focus'--><!--Device-accessibility-type WindowUpdateType = 'add' | 'remove' | 'bounds' | 'active' | 'focus'-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

| Type | Description |
| --- | --- |
| 'add' | 表示添加窗口的窗口变化事件，值固定为'add'字符串。 |
| 'remove' | 表示一个窗口被删除的窗口变化事件，值固定为'remove'字符串。 |
| 'bounds' | 表示窗口边界已更改的窗口变化事件，值固定为'bounds'字符串。 |
| 'active' | 表示窗口变为活动或不活动的窗口变化事件，值固定为'active'字符串。 |
| 'focus' | 表示窗口焦点发生变化的窗口变化事件，值固定为'focus'字符串。 |

