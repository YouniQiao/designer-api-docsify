# ScrollableCommonMethod

CommonScrollableMethod

**Inheritance/Implementation:** ScrollableCommonMethod extends CommonMethod<T>

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-declare class ScrollableCommonMethod--><!--Device-unnamed-declare class ScrollableCommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoAdjustScrollBarMargin

```TypeScript
autoAdjustScrollBarMargin(enable: boolean | undefined): T
```

Set the scroll bar auto adjust the margin to avoid the padding, safeAreaPadding, and contentStartOffset/contentEndOffset of the component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-autoAdjustScrollBarMargin(enable: boolean | undefined): T--><!--Device-ScrollableCommonMethod-autoAdjustScrollBarMargin(enable: boolean | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes | Whether to enable automatic adjustment of scroll bar margin. &lt;br&gt;Default value: false. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## backToTop

```TypeScript
backToTop(backToTop: boolean): T
```

Sets whether to enable the back-to-top feature for a scrollable component when the status bar is touched.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ScrollableCommonMethod-backToTop(backToTop: boolean): T--><!--Device-ScrollableCommonMethod-backToTop(backToTop: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| backToTop | boolean | Yes | Whether to enable the back-to-top feature for a scrollable component when the status bar is touched. &lt;br&gt;Default value: &lt;em&gt;false&lt;/em&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## clipContent

```TypeScript
clipContent(clip: ContentClipMode | RectShape): T
```

Sets the content clipping area for this scrollable component.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ScrollableCommonMethod-clipContent(clip: ContentClipMode | RectShape): T--><!--Device-ScrollableCommonMethod-clipContent(clip: ContentClipMode | RectShape): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| clip | [ContentClipMode](arkts-arkui-contentclipmode-e.md) \| [RectShape](arkts-arkui-rectshape-t.md) | Yes | A value from enum ContentClipMode or a customized clip rect. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## contentEndOffset

```TypeScript
contentEndOffset(offset: number | Resource): T
```

Sets the offset from the end of the content to the boundary of the scrollable display area.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollableCommonMethod-contentEndOffset(offset: number | Resource): T--><!--Device-ScrollableCommonMethod-contentEndOffset(offset: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number \| Resource | Yes | Offset from the end of the content to the boundary of the scrollable display area. &lt;br&gt;Default value: &lt;em&gt;0&lt;/em&gt; &lt;br&gt;Unit: vp |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## contentStartOffset

```TypeScript
contentStartOffset(offset: number | Resource): T
```

Sets the offset from the start of the content to the boundary of the scrollable display area.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollableCommonMethod-contentStartOffset(offset: number | Resource): T--><!--Device-ScrollableCommonMethod-contentStartOffset(offset: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number \| Resource | Yes | Offset from the start of the content to the boundary of the scrollable display area. &lt;br&gt;Default value: &lt;em&gt;0&lt;/em&gt; &lt;br&gt;Unit: vp |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T
```

Set the sensitivity of rotating crown.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScrollableCommonMethod-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T--><!--Device-ScrollableCommonMethod-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensitivity | [Optional](arkts-arkui-optional-t.md)&lt;CrownSensitivity&gt; | Yes | The sensitivity of rotating crown, default value is { MEDIUM }. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The component instance. |

## edgeEffect

```TypeScript
edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T
```

Sets the effect used when the scroll boundary is reached.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T--><!--Device-ScrollableCommonMethod-edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| edgeEffect | EdgeEffect | Yes | Effect used when the scroll boundary is reached. The spring and shadow effects are supported. &lt;br&gt;Default value: &lt;em&gt;EdgeEffect.None&lt;/em&gt; for the &lt;em&gt;Grid&lt;/em&gt;, &lt;em&gt;Scroll&lt;/em&gt;, and &lt;em&gt;WaterFlow&lt;/em&gt; components and &lt;em&gt;EdgeEffect.Spring&lt;/em&gt; for the &lt;em&gt;List&lt;/em&gt; component |
| options | [EdgeEffectOptions](arkts-arkui-edgeeffectoptions-i.md) | No | Whether to enable the scroll effect when the component content is smaller than the component itself. The value &lt;em&gt;{ alwaysEnabled: true }&lt;/em&gt; means to enable the scroll effect, and &lt;em&gt;{ alwaysEnabled: false }&lt; /em&gt; means the opposite. &lt;br&gt;Default value:&lt;br&gt;&lt;em&gt;{ alwaysEnabled: false }&lt;/em&gt; for the &lt;em&gt;List&lt;/em&gt;, &lt;em&gt;Grid&lt;/em&gt;, and &lt;em&gt;WaterFlow &lt;/em&gt; components, and &lt;em&gt;{ alwaysEnabled: true }&lt;/em&gt; for the &lt;em&gt;Scroll&lt;/em&gt; component |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean): T
```

Sets whether to support scroll gestures.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-enableScrollInteraction(value: boolean): T--><!--Device-ScrollableCommonMethod-enableScrollInteraction(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to support scroll gestures.&lt;br&gt;Default value: &lt;em&gt;true&lt;/em&gt; |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## enableScrollWithMouse

```TypeScript
enableScrollWithMouse(enabled: boolean | undefined): T
```

Enable left mouse button press-and-drag scrolling.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-enableScrollWithMouse(enabled: boolean | undefined): T--><!--Device-ScrollableCommonMethod-enableScrollWithMouse(enabled: boolean | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Enable left mouse button press-and-drag scrolling. &lt;br&gt;Default value: false. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## fadingEdge

```TypeScript
fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T
```

Called when setting whether to enable fading Edge effect.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ScrollableCommonMethod-fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T--><!--Device-ScrollableCommonMethod-fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes | Whether to turn on the edge fade effect |
| options | [FadingEdgeOptions](arkts-arkui-fadingedgeoptions-i.md) | No | The options of fadingEdge. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## flingSpeedLimit

```TypeScript
flingSpeedLimit(speedLimit: number): T
```

Sets the maximum initial velocity at the start of the fling animation that occurs after gesture-driven scrolling ends.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-flingSpeedLimit(speedLimit: number): T--><!--Device-ScrollableCommonMethod-flingSpeedLimit(speedLimit: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| speedLimit | number | Yes | Maximum initial velocity at the start of the fling animation. &lt;br&gt;Default value: &lt;em&gt;9000&lt;/em&gt; &lt;br&gt;Unit: vp/s &lt;br&gt;Value range: (0, +∞). If this parameter is set to a value less than or equal to 0, the default value is used. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## friction

```TypeScript
friction(value: number | Resource): T
```

Sets the friction coefficient.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-friction(value: number | Resource): T--><!--Device-ScrollableCommonMethod-friction(value: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| Resource | Yes | Friction coefficient. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions): T
```

Sets the nested scrolling options.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-nestedScroll(value: NestedScrollOptions): T--><!--Device-ScrollableCommonMethod-nestedScroll(value: NestedScrollOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](arkts-arkui-nestedscrolloptions-i.md) | Yes | options for nested scrolling. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onDidScroll

```TypeScript
onDidScroll(handler: OnScrollCallback): T
```

Triggered when the scrollable component scrolls.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ScrollableCommonMethod-onDidScroll(handler: OnScrollCallback): T--><!--Device-ScrollableCommonMethod-onDidScroll(handler: OnScrollCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [OnScrollCallback](arkts-arkui-onscrollcallback-t.md) | Yes | Callback triggered when the scrollable component scrolls. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onDidStopDragging

```TypeScript
onDidStopDragging(handler: OnDidStopDraggingCallback): T
```

Called when the scrollable did end dragging.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onDidStopDragging(handler: OnDidStopDraggingCallback): T--><!--Device-ScrollableCommonMethod-onDidStopDragging(handler: OnDidStopDraggingCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [OnDidStopDraggingCallback](arkts-arkui-ondidstopdraggingcallback-t.md) | Yes | callback of end dragging. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onDidStopFling

```TypeScript
onDidStopFling(handler: VoidCallback): T
```

Called when the scrollable did end fling.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onDidStopFling(handler: VoidCallback): T--><!--Device-ScrollableCommonMethod-onDidStopFling(handler: VoidCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | VoidCallback | Yes | callback of end fling. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onReachEnd

```TypeScript
onReachEnd(event: () => void): T
```

Triggered when the scrollable component reaches the end position.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onReachEnd(event: () => void): T--><!--Device-ScrollableCommonMethod-onReachEnd(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes | Callback function, triggered when the scrollable reaches the end position. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onReachStart

```TypeScript
onReachStart(event: () => void): T
```

Triggered when the scrollable component reaches the start position.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onReachStart(event: () => void): T--><!--Device-ScrollableCommonMethod-onReachStart(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes | Callback function, triggered when the scrollable reaches the start position. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onScroll

```TypeScript
onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T
```

Triggered when the scrollable component scrolls.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 12

**Substitutes:** [onDidScroll](#onDidScroll)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T--><!--Device-ScrollableCommonMethod-onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (scrollOffset: number, scrollState: ScrollState) =&gt; void | Yes | callback of scrollable, scrollOffset is offset per frame scrolling, ScrollState is current scroll state. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onScrollStart

```TypeScript
onScrollStart(event: () => void): T
```

Triggered when the scrollable component starts scrolling initiated by the user's finger dragging the component or its scrollbar.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onScrollStart(event: () => void): T--><!--Device-ScrollableCommonMethod-onScrollStart(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes | Callback function, triggered when the scrollable starts scrolling. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onScrollStop

```TypeScript
onScrollStop(event: () => void): T
```

Triggered when scrolling stops after the user's finger leaves the screen.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onScrollStop(event: () => void): T--><!--Device-ScrollableCommonMethod-onScrollStop(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes | Callback function, triggered when the scrollable stops scrolling. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onWillScroll

```TypeScript
onWillScroll(handler: Optional<OnWillScrollCallback>): T
```

Called when the scrollable will scroll.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollableCommonMethod-onWillScroll(handler: Optional<OnWillScrollCallback>): T--><!--Device-ScrollableCommonMethod-onWillScroll(handler: Optional<OnWillScrollCallback>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [Optional](arkts-arkui-optional-t.md)&lt;[OnWillScrollCallback](arkts-arkui-onwillscrollcallback-t.md)&gt; | Yes | callback of scrollable. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onWillStartDragging

```TypeScript
onWillStartDragging(handler: VoidCallback): T
```

Called when the scrollable will start dragging.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onWillStartDragging(handler: VoidCallback): T--><!--Device-ScrollableCommonMethod-onWillStartDragging(handler: VoidCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | VoidCallback | Yes | callback of start dragging. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onWillStartFling

```TypeScript
onWillStartFling(handler: VoidCallback): T
```

Called when the scrollable will start fling.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onWillStartFling(handler: VoidCallback): T--><!--Device-ScrollableCommonMethod-onWillStartFling(handler: VoidCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | VoidCallback | Yes | callback of start fling. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## onWillStopDragging

```TypeScript
onWillStopDragging(handler: OnWillStopDraggingCallback): T
```

Called when the scrollable will end dragging.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-ScrollableCommonMethod-onWillStopDragging(handler: OnWillStopDraggingCallback): T--><!--Device-ScrollableCommonMethod-onWillStopDragging(handler: OnWillStopDraggingCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [OnWillStopDraggingCallback](arkts-arkui-onwillstopdraggingcallback-t.md) | Yes | callback of end dragging. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## scrollBar

```TypeScript
scrollBar(barState: BarState): T
```

Sets the scrollbar state.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-scrollBar(barState: BarState): T--><!--Device-ScrollableCommonMethod-scrollBar(barState: BarState): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| barState | BarState | Yes | Scrollbar state.&lt;br&gt;Default value: &lt;em&gt;BarState.Auto&lt;/em&gt; for the &lt;em&gt;List&lt;/em&gt;, &lt;em &gt;Grid&lt;/em&gt;, and &lt;em&gt;Scroll&lt;/em&gt; components and &lt;em&gt;BarState.Off&lt;/em&gt; for the &lt;em&gt;WaterFlow&lt;/em&gt; component |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string): T
```

Sets the scrollbar color.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string): T--><!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Color \| number \| string | Yes | Scrollbar color.&lt;br&gt;Default value: &lt;em&gt;'\#182431'&lt;/em&gt; (40% opacity) &lt;br&gt;A number value indicates a HEX color in RGB or ARGB format, for example, &lt;em&gt;0xffffff&lt;/em&gt;. A string value indicates a color in RGB or ARGB format, for example, &lt;em&gt;'# ffffff'&lt;/em&gt;. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string | Resource): T
```

Sets the scrollbar color.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string | Resource): T--><!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | Color \| number \| string \| Resource | Yes | Scrollbar color.&lt;br&gt;Default value: &lt;em&gt;'\#182431'&lt;/em&gt; (40% opacity) &lt;br&gt;A number value indicates a HEX color in RGB or ARGB format, for example, &lt;em&gt;0xffffff&lt;/em&gt;. A string value indicates a color in RGB or ARGB format, for example, &lt;em&gt;'#ffffff'&lt;/em&gt;. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## scrollBarHeight

```TypeScript
scrollBarHeight(height: LengthMetrics | undefined): T
```

Sets the scrollbar track height.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-scrollBarHeight(height: LengthMetrics | undefined): T--><!--Device-ScrollableCommonMethod-scrollBarHeight(height: LengthMetrics | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| height | LengthMetrics \| undefined | Yes | Scrollbar track height. &lt;br&gt;The value must be greater than or equal to 0, If set to undefined or a value less than 0, the default value is used. If set to 0, the scrollbar is not displayed. &lt;br&gt; Default value: adaptive to the height of the scrollable component. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## scrollBarMargin

```TypeScript
scrollBarMargin(margin: ScrollBarMargin): T
```

Margin of the scrollbar.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollableCommonMethod-scrollBarMargin(margin: ScrollBarMargin): T--><!--Device-ScrollableCommonMethod-scrollBarMargin(margin: ScrollBarMargin): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| margin | ScrollBarMargin | Yes | Margin of the scrollbar. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string): T
```

Sets the scrollbar width.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string): T--><!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string | Yes | Scrollbar width.&lt;br&gt;Default value: &lt;em&gt;4&lt;/em&gt; &lt;br&gt;Unit: vp &lt;br&gt;If this parameter is set to a value less than or equal to 0, the default value is used. The value &lt;em&gt;0&lt;/em&gt; means not to show the scrollbar. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string | Resource): T
```

Sets the scrollbar width.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string | Resource): T--><!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| Resource | Yes | Scrollbar width. &lt;br&gt;Unit: vp &lt;br&gt;Default value: &lt;em&gt;4&lt;/em&gt; &lt;br&gt;If this parameter is set to a value less than 0, the default value is used. The value &lt;em&gt;0&lt;/em&gt; means not to show the scrollbar. |

**Return value:**

| Type | Description |
| --- | --- |
| T |  |

