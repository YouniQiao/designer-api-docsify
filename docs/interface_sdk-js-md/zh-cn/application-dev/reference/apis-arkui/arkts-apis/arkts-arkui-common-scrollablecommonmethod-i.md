# ScrollableCommonMethod

CommonScrollableMethod@extends CommonMethod

**继承/实现关系：** ScrollableCommonMethod extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## autoAdjustScrollBarMargin

```TypeScript
default autoAdjustScrollBarMargin(enable: boolean | undefined): this
```

Set the scroll bar auto adjust the margin to avoid the padding, safeAreaPadding, and contentStartOffset/contentEndOffset of the component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## backToTop

```TypeScript
default backToTop(backToTop: boolean | undefined): this
```

Sets whether to enable the back-to-top feature for a scrollable component when the status bar is touched.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [backToTop](#backtotop) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## clipContent

```TypeScript
default clipContent(clip: ContentClipMode | RectShape | undefined): this
```

Sets the content clipping area for this scrollable component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| clip | [ContentClipMode](arkts-arkui-common-contentclipmode-e.md) \| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## contentEndOffset

```TypeScript
default contentEndOffset(offset: double | Resource | undefined): this
```

Sets the offset from the end of the content to the boundary of the scrollable display area.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## contentStartOffset

```TypeScript
default contentStartOffset(offset: double | Resource | undefined): this
```

Sets the offset from the start of the content to the boundary of the scrollable display area.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

Set the sensitivity of rotating crown.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## edgeEffect

```TypeScript
default edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions): this
```

Sets the effect used when the scroll boundary is reached.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [edgeEffect](#edgeeffect) | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | 是 |
| options | [EdgeEffectOptions](arkts-arkui-common-edgeeffectoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## enableScrollInteraction

```TypeScript
default enableScrollInteraction(value: boolean | undefined): this
```

Sets whether to support scroll gestures.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## enableScrollWithMouse

```TypeScript
default enableScrollWithMouse(enabled: boolean | undefined): this
```

Enable left mouse button press-and-drag scrolling.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## fadingEdge

```TypeScript
default fadingEdge(enabled: boolean | undefined, options?: FadingEdgeOptions): this
```

Called when setting whether to enable fading Edge effect.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |
| options | [FadingEdgeOptions](arkts-arkui-common-fadingedgeoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## flingSpeedLimit

```TypeScript
default flingSpeedLimit(speedLimit: double | undefined): this
```

Sets the maximum initial velocity at the start of the fling animation that occurs after gesture-driven scrolling ends.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speedLimit | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## friction

```TypeScript
default friction(value: double | Resource | undefined): this
```

Sets the friction coefficient.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## nestedScroll

```TypeScript
default nestedScroll(value: NestedScrollOptions | undefined): this
```

Sets the nested scrolling options.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NestedScrollOptions](arkts-arkui-common-nestedscrolloptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDidStopDragging

```TypeScript
default onDidStopDragging(handler: OnDidStopDraggingCallback | undefined): this
```

Called when the scrollable did end dragging.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnDidStopDraggingCallback](arkts-arkui-ondidstopdraggingcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDidStopFling

```TypeScript
default onDidStopFling(handler: VoidCallback | undefined): this
```

Called when the scrollable did stop fling.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onReachEnd

```TypeScript
default onReachEnd(event: (() => void) | undefined): this
```

Triggered when the scrollable component reaches the end position.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onReachStart

```TypeScript
default onReachStart(event: (() => void) | undefined): this
```

Triggered when the scrollable component reaches the start position.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollStart

```TypeScript
default onScrollStart(event: (() => void) | undefined): this
```

Triggered when the scrollable component starts scrolling initiated by the user's finger dragging the component or its scrollbar.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollStop

```TypeScript
default onScrollStop(event: (() => void) | undefined): this
```

Triggered when scrolling stops after the user's finger leaves the screen.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onWillStartDragging

```TypeScript
default onWillStartDragging(handler: VoidCallback | undefined): this
```

Called when the scrollable will start dragging.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onWillStartFling

```TypeScript
default onWillStartFling(handler: VoidCallback | undefined): this
```

Called when the scrollable will start fling.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onWillStopDragging

```TypeScript
default onWillStopDragging(handler: OnWillStopDraggingCallback | undefined): this
```

Called when the scrollable will end dragging.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnWillStopDraggingCallback](arkts-arkui-onwillstopdraggingcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBar

```TypeScript
default scrollBar(barState: BarState | undefined): this
```

Sets the scrollbar state.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| barState | [BarState](arkts-arkui-barstate-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarColor

```TypeScript
default scrollBarColor(color: Color | int | string | Resource | undefined): this
```

Sets the scrollbar color.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Color](arkts-arkui-color-e.md) \| int \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarHeight

```TypeScript
default scrollBarHeight(height: LengthMetrics | undefined): this
```

Sets the scrollbar track height.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| height | [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarMargin

```TypeScript
default scrollBarMargin(margin: ScrollBarMargin | undefined): this
```

Margin of the scrollbar.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| margin | [ScrollBarMargin](arkts-arkui-scrollbarmargin-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarWidth

```TypeScript
default scrollBarWidth(value: double | string | undefined): this
```

Sets the scrollbar width.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarWidth

```TypeScript
default scrollBarWidth(value: Resource | undefined): this
```

Sets the scrollbar width.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
