# FastScrollMode

```TypeScript
declare enum FastScrollMode
```

枚举滚动到指定索引的快速滚动模式，配合ScrollToIndexOptions的fastScroll字段使用。

> **说明：** 
> 
> - 当滚动距离较大且触发跳跃时，通常先从起始位置连续滚动约2屏，再跳到距离最终停靠位置约2屏的位置，继续滚动至最终位置。一屏指滚动组件可视区域在滚动方向上的长度。
> - 跳过创建或测量只针对上述被跳过的滚动路径；前后两段连续滚动中需要显示的子组件仍会按需创建和测量。实际创建和测量的范围还受对齐方式、额外偏移量和子组件大小等因素影响，并非固定为4屏。
> - 快速滚动不保证遍历并显示滚动路径上的每一个子组件。
> - fastScroll传入本枚举未定义的值时，按FastScrollMode.NONE处理，不启用快速滚动优化，其余滚动参数仍按原有规则生效。

**起始版本：** 26.1.0

<!--Device-unnamed-declare enum FastScrollMode--><!--Device-unnamed-declare enum FastScrollMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

不启用快速滚动优化，使用组件原有的 `scrollToIndex` 行为。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-FastScrollMode-NONE = 0--><!--Device-FastScrollMode-NONE = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SKIP_CREATE_AND_MEASURE

```TypeScript
SKIP_CREATE_AND_MEASURE = 2
```

跳过实际显示及确定目标实际布局不需要的中间子组件创建和测量。对于多列且 `ListItem` 和 `ListItemGroup` 同时存在的 `List`，请使用 `SKIP_MEASURE`。对于 `WaterFlow`，建议使用此模式。在 `SLIDING_WINDOW` 布局模式下，WaterFlow 定位目标 `FlowItem` 不依赖中间子组件，而 `SKIP_MEASURE` 仍会创建沿途的中间子组件，带来多余的创建开销。对于 `Grid`，如果目标项或中间项的跨行、跨列信息尚未确定，需通过 `GridLayoutOptions` 提前提供完整、准确的跨度信息。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-FastScrollMode-SKIP_CREATE_AND_MEASURE = 2--><!--Device-FastScrollMode-SKIP_CREATE_AND_MEASURE = 2-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SKIP_MEASURE

```TypeScript
SKIP_MEASURE = 1
```

跳过实际显示及确定目标实际布局不需要的中间子项测量。组件可创建中间子项，以取得其占用的行列信息。对于多列且 `ListItem` 和 `ListItemGroup` 同时存在的 `List`，需要取得子组件类型以确定行位置。对于 `Grid`，可按需创建中间 `GridItem` 以确认其跨行或跨列信息。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-FastScrollMode-SKIP_MEASURE = 1--><!--Device-FastScrollMode-SKIP_MEASURE = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
