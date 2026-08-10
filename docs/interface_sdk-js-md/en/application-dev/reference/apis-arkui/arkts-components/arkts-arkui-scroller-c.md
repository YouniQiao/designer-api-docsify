# Scroller

可滚动容器组件的控制器，可以将此组件绑定至容器组件，然后通过它控制容器组件的滚动。同一个控制器不可以控制多个容器组件，目前支持绑定到ArcList、ArcScrollBar、List、Scroll、ScrollBar、Grid、WaterFlow上。

> **说明：**
> 
> 1. Scroller控制器与滚动容器组件的绑定发生在组件创建阶段。

> 2. Scroller控制器与滚动容器组件绑定后才可以正常调用Scroller方法，否则根据调用接口不同会不生效或者抛异常。

> 3. 以[aboutToAppear](../../../reference/apis-arkui/arkui-ts/ts-custom-component-lifecycle.md#abouttoappear)为例，
> aboutToAppear在创建自定义组件的新实例后，在执行其build()方法之前执行。因此如果滚动组件在自定义组件build内，在该自定义组件aboutToAppear执行时，内部滚动组件还没有创建，是不能正常调用上述
> Scroller方法的。

> 4. 以[onAppear](../arkts-apis/arkts-arkui-common-commonmethod-i.md/arkts-arkui-common-commonmethod-i.md#onappear)为例，组件挂载显示后触发此回调。因此在滚动组件的onAppear回调执行时，滚动组件已经创建并已经和Scroller绑定成功，是可以正常调用
> Scroller方法的。

## 导入对象

```ts scroller: Scroller = new Scroller();```

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare class Scroller--><!--Device-unnamed-declare class Scroller-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor()
```

Scroller的构造函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-constructor()--><!--Device-Scroller-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentSize

```TypeScript
contentSize(): SizeResult
```

获取滚动组件内容总大小。

> **说明：**
> 
> - Grid、List、WaterFlow和Scroll组件主轴方向内容大小为所有子组件布局后的总大小，交叉轴方向内容大小为组件自身交叉轴方向大小减去padding和border后的大小。
> 
> - Grid、List、WaterFlow组件有懒加载机制，该接口依赖已布局的子节点进行估算。如果组件内容没有布局完成且子组件高度不一致，估算结果可能会有误差，开发者需要适配。例如，List组件可以通过
> childrenMainSize属性解决估算不准问题。
> 
> - 如果应用动态增删子节点，则需要应用动态获取内容总大小，来保证接口获取结果的即时性。
> 
> - 当Scroll组件设置scrollable为ScrollDirection.FREE自由滚动模式时，获取到的内容总大小为子组件缩放后的总大小。
> 
> - 当Scroll组件设置scrollable为ScrollDirection.None不可滚动时，获取到的内容总大小为0。
> 
> - 当Grid组件同时设置columnsTemplate和rowsTemplate，或columnsTemplate和rowsTemplate都不设置时即为不可滚动场景，此时获取到的内容总大小高度为0，宽度为Grid组件内容区
> 宽度。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Scroller-contentSize(): SizeResult--><!--Device-Scroller-contentSize(): SizeResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [SizeResult](arkts-arkui-sizeresult-i.md) | 滚动组件内容总大小。主轴方向内容大小为所有子组件布局后的总大小，交叉轴方向内容大小为组件自身交叉轴方向大小减去padding和border后的大小。&lt;br/&gt;单位：vp |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100004 | Controller not bound to a component. |

## currentOffset

```TypeScript
currentOffset() : OffsetResult
```

获取当前的滚动总偏移量。

> **说明：**
> 
> 1. 当Scroller没有和组件绑定时，该接口会返回undefined，但是接口中没有声明。推荐使用[offset](arkts-arkui-scroller-c.md#offset)函数，其返回类型显式包含undefined。
> 
> 2. Grid、List、WaterFlow组件有懒加载机制，组件内容没有加载并布局完成时，内容总偏移量通过估算得到，估算结果可能会有误差。其中List组件可以通过
> [childrenMainSize](../arkts-apis/arkts-arkui-list-listattribute-i.md/arkts-arkui-list-listattribute-i.md#childrenmainsize)属性解决估算不准确的问题，Grid与WaterFlow估算不准暂无解决方案。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-currentOffset() : OffsetResult--><!--Device-Scroller-currentOffset() : OffsetResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OffsetResult](arkts-arkui-offsetresult-i.md) | 返回当前的滚动总偏移量。xOffset表示水平滚动总偏移量，yOffset表示竖直滚动总偏移量。&lt;br/&gt; |

## fling

```TypeScript
fling(velocity: number): void
```

滚动类组件根据传入的初始速度进行惯性滚动，可用于模拟抛滑效果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Scroller-fling(velocity: number): void--><!--Device-Scroller-fling(velocity: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| velocity | number | Yes | 惯性滚动的初始速度值。单位：vp/s&lt;br/&gt;**说明：**&lt;br/&gt;velocity值设置为0时，本次滚动不生效且不会产生滚动动画。如果值为正数，则向顶部滚动；如果值为负 数，则向底部滚动。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## getFrameNode

```TypeScript
getFrameNode(): FrameNode | undefined
```

获取与当前Scroller绑定的FrameNode。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Scroller-getFrameNode(): FrameNode | undefined--><!--Device-Scroller-getFrameNode(): FrameNode | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [FrameNode](../arkts-apis/arkts-arkui-framenode-t.md) | 当Scroller已绑定到Scroll、List、Grid、WaterFlow等滚动类组件时，返回对应组件的FrameNode；如果Scroller未绑定组件， 则返回undefined。 |

## getItemIndex

```TypeScript
getItemIndex(x: number, y: number): number
```

通过坐标获取子组件的索引。

> **说明：**
> 
> 支持List、Grid、WaterFlow组件。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Scroller-getItemIndex(x: number, y: number): number--><!--Device-Scroller-getItemIndex(x: number, y: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | x轴坐标，单位为vp。 |
| y | number | Yes | y轴坐标，单位为vp。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回坐标命中的子组件索引。坐标未命中子组件时，返回-1。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## getItemRect

```TypeScript
getItemRect(index: number): RectResult
```

获取子组件的大小及相对容器组件的位置。

> **说明：**
> 
> 支持ArcList、Scroll、List、Grid、WaterFlow组件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Scroller-getItemRect(index: number): RectResult--><!--Device-Scroller-getItemRect(index: number): RectResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 子组件的索引值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](arkts-arkui-rectresult-i.md) | 子组件的大小和相对于组件的位置。&lt;br/&gt;单位：vp。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

## isAtEnd

```TypeScript
isAtEnd(): boolean
```

查询组件是否滚动到底部。

> **说明：**
> 
> 支持ArcList、Scroll、List、Grid、WaterFlow组件。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-isAtEnd(): boolean--><!--Device-Scroller-isAtEnd(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示组件已经滚动到底部，false表示组件还没滚动到底部。 |

## offset

```TypeScript
offset() : OffsetResult | undefined
```

获取当前的滚动总偏移量。除接口声明有undefined以外，其他与[currentOffset](arkts-arkui-scroller-c.md#currentoffset)接口保持一致。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Scroller-offset() : OffsetResult | undefined--><!--Device-Scroller-offset() : OffsetResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [OffsetResult](arkts-arkui-offsetresult-i.md) | 返回当前的滚动总偏移量。xOffset表示水平滚动总偏移量，yOffset表示竖直滚动总偏移量。当Scroller没有和组件绑定时，该接口会返回 undefined。 |

## scrollBy

```TypeScript
scrollBy(dx: Length, dy: Length)
```

滑动指定距离。

> **说明：**
> 
> - 支持ArcList、Scroll、List、Grid、WaterFlow组件。
> 
> - 各组件行为存在差异：
> 
> - [ArcList](../arkts-apis/arkts-arkui-arclist.md/arkts-arkui-arclist.md)和[List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)组件会对所有经过的item进行加载和布局。
> 
> - Grid组件和[SLIDING_WINDOW](../arkts-apis/arkts-arkui-waterflow-waterflowlayoutmode-e.md/arkts-arkui-waterflow-waterflowlayoutmode-e.md)模式的WaterFlow组件在跳转距离较大（大于2倍组件主轴高度）时，会直接估算出要显示的item。跳转指一帧滑动。
> 
> - [ALWAYS_TOP_DOWN](../arkts-apis/arkts-arkui-waterflow-waterflowlayoutmode-e.md/arkts-arkui-waterflow-waterflowlayoutmode-e.md)模式的WaterFlow组件向后跳转（即dx或dy为正值时）会加载和布局所有经过的item，向前跳转（即dx或dy为负值时）会直接跳转
> 到对应位置。跳转指一帧滑动。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollBy(dx: Length, dy: Length)--><!--Device-Scroller-scrollBy(dx: Length, dy: Length)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dx | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | 水平方向滚动距离，不支持百分比形式。 &lt;br/&gt;取值范围：(-∞, +∞) |
| dy | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | 竖直方向滚动距离，不支持百分比形式。 &lt;br/&gt;取值范围：(-∞, +∞) |

## scrollEdge

```TypeScript
scrollEdge(value: Edge, options?: ScrollEdgeOptions)
```

滚动到容器边缘，不区分滚动轴方向，Edge.Top和Edge.Start表现相同，Edge.Bottom和Edge.End表现相同。可用于返回顶部、跳转到内容末尾等场景。

Scroll组件默认有动画，Grid、List、WaterFlow组件默认无动画。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions)--><!--Device-Scroller-scrollEdge(value: Edge, options?: ScrollEdgeOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Edge](../arkts-apis/arkts-arkui-edge-e.md) | Yes | 滚动到的边缘位置。 |
| options | [ScrollEdgeOptions](arkts-arkui-scrolledgeoptions-i.md) | No | 设置滚动到边缘位置的模式。 &lt;br&gt;&lt;em&gt;原子化服务API&lt;/em&gt;：该API可在原子化服务中使用，从API version 12开始。<br>**Since:** 12 |

## scrollPage

```TypeScript
scrollPage(value: ScrollPageOptions)
```

滚动到下一页或者上一页。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollPage(value: ScrollPageOptions)--><!--Device-Scroller-scrollPage(value: ScrollPageOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollPageOptions](arkts-arkui-scrollpageoptions-i.md) | Yes | 设置翻页模式。包含next（是否向下翻页）和animation（是否开启翻页动画）字段，用于指定翻页行为。<br>**Since:** 14 |

## scrollPage

```TypeScript
scrollPage(value: { next: boolean; direction?: Axis })
```

滚动到下一页或者上一页。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [Scroller#scrollPage](arkts-arkui-scroller-c.md#scrollpage)

<!--Device-Scroller-scrollPage(value: { next: boolean; direction?: Axis })--><!--Device-Scroller-scrollPage(value: { next: boolean; direction?: Axis })-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { next: boolean; direction?: Axis } | Yes | next：是否向下翻页。true表示向下翻页，false表示向上翻页。 &lt;br&gt; direction：设置滚动方向为水平或竖直方向。 |

## scrollTo

```TypeScript
scrollTo(options: ScrollOptions)
```

滑动到指定位置，可用于目录跳转、返回顶部、搜索结果定位等场景。

> **说明：**
> 
> - scrollTo动画速度大于200vp/s时，滚动组件区域内的组件不响应点击事件。
> 
> - 各组件行为存在差异：
> 
> - [ArcList](../arkts-apis/arkts-arkui-arclist.md/arkts-arkui-arclist.md)和[List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)组件会对所有经过的item进行加载和布局。
> 
> - Grid组件和[SLIDING_WINDOW](../arkts-apis/arkts-arkui-waterflow-waterflowlayoutmode-e.md/arkts-arkui-waterflow-waterflowlayoutmode-e.md)模式的[WaterFlow](./water_flow)组件在跳转距离较大（大于2倍组件主轴高度）时，会直接估
> 算出要显示的item。跳转指一帧滑动。
> 
> - [ALWAYS_TOP_DOWN](../arkts-apis/arkts-arkui-waterflow-waterflowlayoutmode-e.md/arkts-arkui-waterflow-waterflowlayoutmode-e.md)模式的WaterFlow组件向后跳转（即dx或dy为正值时）会加载和布局所有经过的item，向前跳转（即dx或dy为负值时）会直接跳转
> 到对应位置。跳转指一帧滑动。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollTo(options: ScrollOptions)--><!--Device-Scroller-scrollTo(options: ScrollOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ScrollOptions](../arkts-apis/arkts-arkui-viewmodel-scrolloptions-i.md) | Yes | 滑动到指定位置的参数，包含xOffset、yOffset、animation、canOverScroll等字段，用于指定滚动目标位置和滚动行 为。<br>**Since:** 18 |

## scrollToIndex

```TypeScript
scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)
```

滑动到指定Index，支持设置滑动额外偏移量。

开启smooth动画时，会对经过的所有item进行加载和布局计算。当大量加载item时会导致性能问题，开发者应先调用scrollToIndex不带动画跳转到目标附近位置，再调用scrollToIndex带动画滚动到目标位置，以优化性能。

> **说明：**
> 
> 1. 仅支持ArcList、Grid、List、WaterFlow组件。
> 
> 2. 在[LazyForEach](./lazy_for_each)、[ForEach](./for_each)、[Repeat](../arkts-apis/arkts-arkui-repeat-repeat-f.md/arkts-arkui-repeat-repeat-f.md#repeat)刷新数据源时，需确保在数据刷新完成之后再
> 调用此接口。
> 
> 3. 从API version 11开始，在List中支持[contentStartOffset](../arkts-apis/arkts-arkui-list-listattribute-i.md/arkts-arkui-list-listattribute-i.md#contentstartoffset)和
> [contentEndOffset](../arkts-apis/arkts-arkui-list-listattribute-i.md/arkts-arkui-list-listattribute-i.md#contentendoffset)。从API version 22开始，在Grid和WaterFlow组件中支持设置
> [contentStartOffset](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#contentstartoffset22)
> 和
> [contentEndOffset](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#contentendoffset22)。
> 
> - 当滚动容器组件设置contentStartOffset时，如果ScrollAlign设置为START，滚动结束时，指定item首部会与滚动容器组件contentStartOffset处对齐。
> 
> - 当滚动容器组件设置contentEndOffset时，如果ScrollAlign设置为END，滚动结束时，指定item尾部会与滚动容器组件contentEndOffset处对齐。
> 
> - 当滚动容器组件设置contentStartOffset或contentEndOffset时，如果ScrollAlign设置为AUTO，且指定item完全处于显示区内，不做调整；否则依照滚动距离最短的原则，将指定item首部
> 与滚动组件contentStartOffset处对齐，或指定item尾部与滚动组件contentEndOffset处对齐，使指定item完全显示。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Scroller-scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)--><!--Device-Scroller-scrollToIndex(value: number, smooth?: boolean, align?: ScrollAlign, options?: ScrollToIndexOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 要滑动到的目标元素在当前容器中的索引值。 &lt;br/&gt;**说明：** &lt;br/&gt;value值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。 |
| smooth | boolean | No | 设置滑动到列表项在列表中的索引值时是否有动画，true表示有动画，false表示没有动画。不传入时默认无动画。&lt;br/&gt;默认值：false。<br>**Since:** 12 |
| align | [ScrollAlign](arkts-arkui-scrollalign-e.md) | No | 指定滑动到的元素与当前容器的对齐方式，可根据期望item首部、尾部或居中显示选择对应对齐方式。&lt;br/&gt;默认值：List为ScrollAlign.START， Grid为ScrollAlign.AUTO，WaterFlow为ScrollAlign.START。&lt;br/&gt;**说明：** &lt;br/&gt;仅List、Grid、WaterFlow组件支持该参数。<br>**Since:** 12 |
| options | [ScrollToIndexOptions](../arkts-apis/arkts-arkui-scroll-scrolltoindexoptions-i.md) | No | 设置滑动到指定Index的选项，包含extraOffset字段，用于指定滚动后的额外偏移量。&lt;br/&gt;不传入时无额外偏移量。&lt;br/ &gt;<br>**Since:** 12 |

