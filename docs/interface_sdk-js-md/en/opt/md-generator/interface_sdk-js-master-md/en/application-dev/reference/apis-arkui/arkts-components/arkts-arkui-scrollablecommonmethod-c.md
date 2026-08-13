# ScrollableCommonMethod

CommonScrollableMethod

**Inheritance/Implementation:** ScrollableCommonMethod extends CommonMethod<T>

**Since:** 12

**Deprecated since:** -1

<!--Device-unnamed-declare class ScrollableCommonMethod--><!--Device-unnamed-declare class ScrollableCommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoAdjustScrollBarMargin

```TypeScript
autoAdjustScrollBarMargin(enable: boolean | undefined): T
```

Set the scroll bar auto adjust the margin to avoid the padding, safeAreaPadding, and contentStartOffset/contentEndOffset of the component.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-autoAdjustScrollBarMargin(enable: boolean | undefined): T--><!--Device-ScrollableCommonMethod-autoAdjustScrollBarMargin(enable: boolean | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## backToTop

```TypeScript
backToTop(backToTop: boolean): T
```

Sets whether to enable the back-to-top feature for a scrollable component when the status bar is touched.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ScrollableCommonMethod-backToTop(backToTop: boolean): T--><!--Device-ScrollableCommonMethod-backToTop(backToTop: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [backToTop](#backToTop) | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## clipContent

```TypeScript
clipContent(clip: ContentClipMode | RectShape): T
```

Sets the content clipping area for this scrollable component.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ScrollableCommonMethod-clipContent(clip: ContentClipMode | RectShape): T--><!--Device-ScrollableCommonMethod-clipContent(clip: ContentClipMode | RectShape): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| clip | [ContentClipMode](arkts-arkui-contentclipmode-e.md) \| [RectShape](arkts-arkui-rectshape-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## contentEndOffset

```TypeScript
contentEndOffset(offset: number | Resource): T
```

Sets the offset from the end of the content to the boundary of the scrollable display area.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollableCommonMethod-contentEndOffset(offset: number | Resource): T--><!--Device-ScrollableCommonMethod-contentEndOffset(offset: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## contentStartOffset

```TypeScript
contentStartOffset(offset: number | Resource): T
```

Sets the offset from the start of the content to the boundary of the scrollable display area.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollableCommonMethod-contentStartOffset(offset: number | Resource): T--><!--Device-ScrollableCommonMethod-contentStartOffset(offset: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T
```

Set the sensitivity of rotating crown.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ScrollableCommonMethod-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T--><!--Device-ScrollableCommonMethod-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sensitivity | [Optional](arkts-arkui-optional-t.md)&lt;[CrownSensitivity](../arkts-apis/arkts-arkui-crownsensitivity-e.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## edgeEffect

```TypeScript
edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T
```

Sets the effect used when the scroll boundary is reached.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T--><!--Device-ScrollableCommonMethod-edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [edgeEffect](#edgeEffect) | [EdgeEffect](../arkts-apis/arkts-arkui-edgeeffect-e.md) | Yes |
| options | [EdgeEffectOptions](arkts-arkui-edgeeffectoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean): T
```

Sets whether to support scroll gestures.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-enableScrollInteraction(value: boolean): T--><!--Device-ScrollableCommonMethod-enableScrollInteraction(value: boolean): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## enableScrollWithMouse

```TypeScript
enableScrollWithMouse(enabled: boolean | undefined): T
```

Enable left mouse button press-and-drag scrolling.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-enableScrollWithMouse(enabled: boolean | undefined): T--><!--Device-ScrollableCommonMethod-enableScrollWithMouse(enabled: boolean | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## fadingEdge

```TypeScript
fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T
```

Called when setting whether to enable fading Edge effect.

**Since:** 14

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ScrollableCommonMethod-fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T--><!--Device-ScrollableCommonMethod-fadingEdge(enabled: Optional<boolean>, options?: FadingEdgeOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |
| options | [FadingEdgeOptions](arkts-arkui-fadingedgeoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## flingSpeedLimit

```TypeScript
flingSpeedLimit(speedLimit: number): T
```

Sets the maximum initial velocity at the start of the fling animation that occurs after gesture-driven scrolling ends.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-flingSpeedLimit(speedLimit: number): T--><!--Device-ScrollableCommonMethod-flingSpeedLimit(speedLimit: number): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| speedLimit | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## friction

```TypeScript
friction(value: number | Resource): T
```

Sets the friction coefficient.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-friction(value: number | Resource): T--><!--Device-ScrollableCommonMethod-friction(value: number | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions): T
```

Sets the nested scrolling options.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-nestedScroll(value: NestedScrollOptions): T--><!--Device-ScrollableCommonMethod-nestedScroll(value: NestedScrollOptions): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [NestedScrollOptions](arkts-arkui-nestedscrolloptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDidScroll

```TypeScript
onDidScroll(handler: OnScrollCallback): T
```

Triggered when the scrollable component scrolls.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-ScrollableCommonMethod-onDidScroll(handler: OnScrollCallback): T--><!--Device-ScrollableCommonMethod-onDidScroll(handler: OnScrollCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnScrollCallback](arkts-arkui-onscrollcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDidStopDragging

```TypeScript
onDidStopDragging(handler: OnDidStopDraggingCallback): T
```

Called when the scrollable did end dragging.

**Since:** 21

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onDidStopDragging(handler: OnDidStopDraggingCallback): T--><!--Device-ScrollableCommonMethod-onDidStopDragging(handler: OnDidStopDraggingCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnDidStopDraggingCallback](arkts-arkui-ondidstopdraggingcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onDidStopFling

```TypeScript
onDidStopFling(handler: VoidCallback): T
```

Called when the scrollable did end fling.

**Since:** 21

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onDidStopFling(handler: VoidCallback): T--><!--Device-ScrollableCommonMethod-onDidStopFling(handler: VoidCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onReachEnd

```TypeScript
onReachEnd(event: () => void): T
```

Triggered when the scrollable component reaches the end position.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onReachEnd(event: () => void): T--><!--Device-ScrollableCommonMethod-onReachEnd(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onReachStart

```TypeScript
onReachStart(event: () => void): T
```

Triggered when the scrollable component reaches the start position.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onReachStart(event: () => void): T--><!--Device-ScrollableCommonMethod-onReachStart(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onScroll

```TypeScript
onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T
```

Triggered when the scrollable component scrolls.

**Since:** 11

**Deprecated since:** 12

**Substitutes:** [onDidScroll](#onDidScroll)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T--><!--Device-ScrollableCommonMethod-onScroll(event: (scrollOffset: number, scrollState: ScrollState) => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | (scrollOffset: number, scrollState: ScrollState) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onScrollStart

```TypeScript
onScrollStart(event: () => void): T
```

Triggered when the scrollable component starts scrolling initiated by the user's finger dragging the component or its scrollbar.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onScrollStart(event: () => void): T--><!--Device-ScrollableCommonMethod-onScrollStart(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onScrollStop

```TypeScript
onScrollStop(event: () => void): T
```

Triggered when scrolling stops after the user's finger leaves the screen.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-onScrollStop(event: () => void): T--><!--Device-ScrollableCommonMethod-onScrollStop(event: () => void): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onWillScroll

```TypeScript
onWillScroll(handler: Optional<OnWillScrollCallback>): T
```

Called when the scrollable will scroll.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ScrollableCommonMethod-onWillScroll(handler: Optional<OnWillScrollCallback>): T--><!--Device-ScrollableCommonMethod-onWillScroll(handler: Optional<OnWillScrollCallback>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [Optional](arkts-arkui-optional-t.md)&lt;[OnWillScrollCallback](arkts-arkui-onwillscrollcallback-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onWillStartDragging

```TypeScript
onWillStartDragging(handler: VoidCallback): T
```

Called when the scrollable will start dragging.

**Since:** 21

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onWillStartDragging(handler: VoidCallback): T--><!--Device-ScrollableCommonMethod-onWillStartDragging(handler: VoidCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onWillStartFling

```TypeScript
onWillStartFling(handler: VoidCallback): T
```

Called when the scrollable will start fling.

**Since:** 21

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-ScrollableCommonMethod-onWillStartFling(handler: VoidCallback): T--><!--Device-ScrollableCommonMethod-onWillStartFling(handler: VoidCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## onWillStopDragging

```TypeScript
onWillStopDragging(handler: OnWillStopDraggingCallback): T
```

Called when the scrollable will end dragging.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-ScrollableCommonMethod-onWillStopDragging(handler: OnWillStopDraggingCallback): T--><!--Device-ScrollableCommonMethod-onWillStopDragging(handler: OnWillStopDraggingCallback): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnWillStopDraggingCallback](arkts-arkui-onwillstopdraggingcallback-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scrollBar

```TypeScript
scrollBar(barState: BarState): T
```

Sets the scrollbar state.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-scrollBar(barState: BarState): T--><!--Device-ScrollableCommonMethod-scrollBar(barState: BarState): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| barState | [BarState](../arkts-apis/arkts-arkui-barstate-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string): T
```

Sets the scrollbar color.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string): T--><!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | Color \| number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string | Resource): T
```

Sets the scrollbar color.

**Since:** 22

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string | Resource): T--><!--Device-ScrollableCommonMethod-scrollBarColor(color: Color | number | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | Color \| number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scrollBarHeight

```TypeScript
scrollBarHeight(height: LengthMetrics | undefined): T
```

Sets the scrollbar track height.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-scrollBarHeight(height: LengthMetrics | undefined): T--><!--Device-ScrollableCommonMethod-scrollBarHeight(height: LengthMetrics | undefined): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| height | LengthMetrics \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scrollBarMargin

```TypeScript
scrollBarMargin(margin: ScrollBarMargin): T
```

Margin of the scrollbar.

**Since:** 20

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ScrollableCommonMethod-scrollBarMargin(margin: ScrollBarMargin): T--><!--Device-ScrollableCommonMethod-scrollBarMargin(margin: ScrollBarMargin): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| margin | [ScrollBarMargin](../arkts-apis/arkts-arkui-scrollbarmargin-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string): T
```

Sets the scrollbar width.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string): T--><!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string | Resource): T
```

Sets the scrollbar width.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string | Resource): T--><!--Device-ScrollableCommonMethod-scrollBarWidth(value: number | string | Resource): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
