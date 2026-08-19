# ScrollBar

## ScrollBar

```TypeScript
ScrollBar(value: ScrollBarOptions)
```

Creates a scroll bar.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollBarInterface-(value: ScrollBarOptions): ScrollBarAttribute--><!--Device-ScrollBarInterface-(value: ScrollBarOptions): ScrollBarAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollBarOptions](arkts-arkui-scrollbaroptions-i.md) | Yes | Parameters of the **ScrollBar** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [ScrollBarOptions](arkts-arkui-scrollbaroptions-i.md) | Parameters of the **ScrollBar** component. &gt; **NOTE：**&gt; &gt; - The **ScrollBar** component defines the behavior style of the scrollable area, and its child nodes define the &gt; behavior style of the scrollbar. &gt; &gt; - This component is bound to a scrollable component through **scroller**, and can be used to scroll the scrollable &gt; component only when their directions are the same. The **ScrollBar** component can be bound to only one scrollable &gt; component, and vice versa. &gt; &gt; - Since API version 12, the **ScrollBar** component displays a default scrollbar style when without child nodes. &gt; &gt; - The visibility of the **ScrollBar** component is set through **BarState**. The component automatically adjusts &gt; **opacity** based on the **BarState** setting to control its visibility. Therefore, setting the &gt; opacity attribute for the **ScrollBar** &gt; component does not take effect. |

### Enums

| Name | Description |
| --- | --- |
| [ScrollBarDirection](arkts-arkui-scrollbardirection-e.md) | Enumerates the scrolling directions. |

