# ScrollBarOptions

滚动条组件参数。

> **说明：**
> 
> - ScrollBar组件用于显示并控制所绑定可滚动组件的滚动位置。设置子组件时，该子组件作为自定义滚动条滑块，并随可滚动组件的滚动位置移动。
> 
> - 滚动条组件与可滚动组件通过Scroller进行绑定，且只有当两者方向相同时，才能联动。一个可滚动组件可以绑定多个ScrollBar组件，一个ScrollBar组件只能绑定一个可滚动组件。
> 
> - 从API version 12开始，ScrollBar组件没有子节点时，支持显示默认样式的滚动条。
> 
> - ScrollBar组件的显隐是通过BarState设置，组件内部会自动根据BarState设置调整opacity来控制显隐，因此ScrollBar组件设置
> [opacity](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#opacity)属性不生效。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface ScrollBarOptions--><!--Device-unnamed-declare interface ScrollBarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction?: ScrollBarDirection
```

滚动条的方向，控制可滚动组件对应方向的滚动。&lt;br/&gt;默认值：ScrollBarDirection.Vertical

**Type:** [ScrollBarDirection](arkts-arkui-scrollbardirection-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollBarOptions-direction?: ScrollBarDirection--><!--Device-ScrollBarOptions-direction?: ScrollBarDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scroller

```TypeScript
scroller: Scroller
```

可滚动组件的控制器。用于与可滚动组件进行绑定。

**Type:** [Scroller](../arkts-apis/arkts-arkui-scroll-scroller-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollBarOptions-scroller: Scroller--><!--Device-ScrollBarOptions-scroller: Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
state?: BarState
```

滚动条状态。&lt;br/&gt;默认值：BarState.Auto

**Type:** [BarState](../arkts-apis/arkts-arkui-barstate-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollBarOptions-state?: BarState--><!--Device-ScrollBarOptions-state?: BarState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

