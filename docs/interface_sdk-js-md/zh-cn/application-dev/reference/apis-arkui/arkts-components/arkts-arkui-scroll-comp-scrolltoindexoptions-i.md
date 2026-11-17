# ScrollToIndexOptions

```TypeScript
declare interface ScrollToIndexOptions
```

滑动到指定Index的参数选项。

**起始版本：** 12

<!--Device-unnamed-declare interface ScrollToIndexOptions--><!--Device-unnamed-declare interface ScrollToIndexOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## extraOffset

```TypeScript
extraOffset?: LengthMetrics
```

滚动到指定索引的额外偏移量。

**类型：** LengthMetrics

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ScrollToIndexOptions-extraOffset?: LengthMetrics--><!--Device-ScrollToIndexOptions-extraOffset?: LengthMetrics-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## fastScroll

```TypeScript
fastScroll?: FastScrollMode
```

快速滚动模式，用于滚动到指定索引。取值为 `SKIP_MEASURE` 时不测量中间子组件；取值为 `SKIP_CREATE_AND_MEASURE` 时既不创建也不测量中间子组件。该参数支持 `List`、`Grid` 以及采用 `SLIDING_WINDOW` 布局模式的 `WaterFlow`，且仅当 `scrollToIndex` 的 `smooth`参数为 `true` 时生效。默认值：`FastScrollMode.NONE`，与不设置该参数时的行为相同。取值范围：本枚举定义的 `0`、`1`、`2`。传入其他值时，按 `FastScrollMode.NONE` 处理，不启用快速滚动优化，其余滚动参数仍按原有规则生效。此设置只对本次调用生效。下一次调用省略 `fastScroll` 时使用 `NONE`。

对于 `Grid`，特殊行列位置通过 `GridLayoutOptions` 表达。`SKIP_CREATE_AND_MEASURE` 无法发现仅在创建冷`GridItem` 时才设置的显式位置；该限制不影响 `SKIP_MEASURE` 和 `NONE`。

对于 `Grid`，保留的子项包括动画开始和结束时视口内的子项、确定目标实际布局所需的子项，以及与目标视口相交的跨行跨列项。

使用 `SKIP_CREATE_AND_MEASURE` 时，若尚未创建的子项跨度未知，须在请求滚动前通过 [GridLayoutOptions](arkts-arkui-grid-comp-gridlayoutoptions-i.md)配置完整行列跨度，确保相应 `GridItem` 创建前可获取这些信息。`GridLayoutOptions.regularSize` 描述规则子项的跨度，`irregularIndexes` 指定不规则子项的索引，`onGetIrregularSizeByIndex` 提供对应子项的跨度。这些字段须遵循 `GridLayoutOptions` 文档中的使用要求。自定义定位须遵循 `GridLayoutOptions.onGetRectByIndex`文档规定的行列位置和跨度要求。跨度信息须覆盖所有占用行列会影响目标位置的跨行跨列项，包括目标视口外的中间项。调用者不能只提供目标项的跨度。每个跨度须与实际内容一致。此要求针对占用的行列，不要求预先知道测量后的像素尺寸。

此模式仅支持满足上述跨度前提的输入。所需跨度缺失或与实际内容不一致时，不保证滚动结果。此模式不自动降级到其他模式。滚动请求不提供同步到达结果或跨度缺失错误。`SKIP_MEASURE` 和 `NONE` 不增加上述跨度要求。

**类型：** [FastScrollMode](arkts-arkui-scroll-comp-fastscrollmode-e.md)

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-ScrollToIndexOptions-fastScroll?: FastScrollMode--><!--Device-ScrollToIndexOptions-fastScroll?: FastScrollMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
