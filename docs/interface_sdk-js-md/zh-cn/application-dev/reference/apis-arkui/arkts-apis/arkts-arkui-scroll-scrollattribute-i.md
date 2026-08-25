# ScrollAttribute

除支持通用属性和滚动组件通用属性外，还支持 以下属性：

**继承/实现关系：** ScrollAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ScrollAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置Scroll组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ScrollAttribute](arkts-arkui-scroll-scrollattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## edgeEffect

```TypeScript
default edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions | undefined): this
```

设置边缘滑动效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [edgeEffect](#edgeeffect) | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | 是 |
| options | [EdgeEffectOptions](../arkts-components/arkts-arkui-edgeeffectoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| this |

## enableBouncesZoom

```TypeScript
default enableBouncesZoom(enable: boolean | undefined): this
```

启用过缩放回弹效果。未通过该接口设置时，默认启用该效果。

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

## enablePaging

```TypeScript
default enablePaging(value: boolean | undefined): this
```

设置是否支持划动翻页。如果同时设置了划动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效，enablePaging不生效。

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

## enableScrollInteraction

```TypeScript
default enableScrollInteraction(value: boolean | undefined): this
```

设置是否支持滚动手势。

> **说明：**

> 组件无法通过鼠标按下拖动操作进行滚动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## friction

```TypeScript
default friction(value: double | Resource | undefined): this
```

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## initialOffset

```TypeScript
default initialOffset(value: OffsetOptions | undefined): this
```

设置初始滚动偏移量。只在首次布局时生效，后续动态修改该属性值不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [OffsetOptions](arkts-arkui-scroll-offsetoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## maxZoomScale

```TypeScript
default maxZoomScale(scale: double | undefined): this
```

设置Scroll组件内容的最大手势缩放比例。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## minZoomScale

```TypeScript
default minZoomScale(scale: double | undefined): this
```

设置Scroll组件内容的最小手势缩放比例。

> **说明：**

> 当maxZoomScale和minZoomScale不同时为1时，Scroll组件会启用缩放手势。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## nestedScroll

```TypeScript
default nestedScroll(value: NestedScrollOptions | undefined): this
```

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NestedScrollOptions](../arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDidScroll

```TypeScript
default onDidScroll(handler: ScrollOnScrollCallback | undefined): this
```

滚动事件回调，Scroll滚动时触发。返回当前帧滚动的偏移量和当前滚动状态。触发该事件的条件：1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。2、通过滚动控制器API接口调用。3、越界回弹。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [ScrollOnScrollCallback](arkts-arkui-scrollonscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onDidZoom

```TypeScript
default onDidZoom(event: ScrollOnDidZoomCallback | undefined): this
```

每帧缩放完成时触发。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [ScrollOnDidZoomCallback](arkts-arkui-scrollondidzoomcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollEdge

```TypeScript
default onScrollEdge(event: OnScrollEdgeCallback | undefined): this
```

滚动到边缘事件回调。触发该事件的条件：1、滚动组件滚动到边缘时触发，支持键鼠操作等其他触发滚动的输入设置。2、通过滚动控制器API接口调用。3、越界回弹。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnScrollEdgeCallback](arkts-arkui-onscrolledgecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollFrameBegin

```TypeScript
default onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

该接口回调时，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。支持[offsetRemain](arkts-arkui-scroll-onscrollframebeginhandlerresult-i.md)为负值。若通过onScrollFrameBegin事件和[scrollBy](arkts-arkui-scroll-scroller-c.md#scrollby)方法实现容器嵌套滚动，需设置子滚动节点的[EdgeEffect](#edgeeffect)为 None。如Scroll嵌套List滚动时，List组件的 edgeEffect属性需设置为EdgeEffect.None，否则抛滑 List，会触发List的边缘回弹动画，导致嵌套滚动失效。满足以下任一条件时触发该事件：
1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. Scroll惯性滚动。
3. 调用[fling](arkts-arkui-scroll-scroller-c.md#fling)接口触发滚动。
不触发该事件的条件：
1. 调用除[fling](arkts-arkui-scroll-scroller-c.md#fling)接口外的其他滚动控制接口。
2. 越界回弹。
3. 拖动滚动条。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnScrollFrameBeginCallback](arkts-arkui-onscrollframebegincallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollStart

```TypeScript
default onScrollStart(event: VoidCallback | undefined): this
```

滚动开始时触发。手指拖动Scroll或拖动Scroll的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](arkts-arkui-scroll-scroller-c.md)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。触发该事件的条件：1、滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。2、通过滚动控制器API接口调用后开始，带过渡动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onScrollStop

```TypeScript
default onScrollStop(event: VoidCallback | undefined): this
```

滚动停止时触发。手拖动Scroll或拖动Scroll的滚动条触发的滚动，手离开屏幕后滚动停止时会触发该事件。使用[Scroller](arkts-arkui-scroll-scroller-c.md)滚动控制器触发的带动画的滚动，动画停止时会触发该事件。触发该事件的条件：1、滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。2、通过滚动控制器API接口调用后开始，带过渡动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onWillScroll

```TypeScript
default onWillScroll(handler: ScrollOnWillScrollCallback | undefined): this
```

滚动事件回调，Scroll滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。触发该事件的条件：1、滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。2、通过滚动控制器API接口调用。3、越界回弹。

> **说明：**&gt;
> 滚动事件的回调函数在滚动过程中会被频繁触发，因此应避免在该回调函数中执行耗时操作，以防止应用出现卡顿和丢帧的问题。最佳实践请参考
> [主线程耗时操作优化指导-高频回调场景](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread#section10112623611)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [ScrollOnWillScrollCallback](arkts-arkui-scrollonwillscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onZoomStart

```TypeScript
default onZoomStart(event: VoidCallback | undefined): this
```

手势缩放开始触发。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onZoomStop

```TypeScript
default onZoomStop(event: VoidCallback | undefined): this
```

手势缩放停止时触发。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollable

```TypeScript
default scrollable(value: ScrollDirection | undefined): this
```

设置滚动方向。该值被修改后会重置滚动偏移量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScrollDirection](arkts-arkui-scroll-scrolldirection-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBar

```TypeScript
default scrollBar(barState: BarState | undefined): this
```

设置滚动条状态。如果容器组件无法滚动，则滚动条不显示。如果容器组件的子组件大小为无穷大，则滚动条不支持拖动和伴随滚动。从API version 10开始，当滚动组件存在圆角时，为避免滚动条被圆角截断，滚动条会自动计算距顶部和底部的避让距离。

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

设置滚动条的颜色。与[scrollBarColor](#scrollbarcolor)相比，color参数开始支持Resource类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Color](arkts-arkui-color-e.md) \| int \| string \| [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollBarWidth

```TypeScript
default scrollBarWidth(value: double | string | undefined): this
```

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的高度，则滚动条的宽度会变为默认值。

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

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的高度，则滚动条的宽度会变为4vp，支持Resource资源类型。未通过该接口设置时，设置滚动条的宽度为4vp。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scrollSnap

```TypeScript
default scrollSnap(value: ScrollSnapOptions | undefined): this
```

设置Scroll组件的限位滚动模式。限位动画期间[onWillScroll](#onwillscroll)事件上报的滚动操作来源类型为ScrollSource.FLING。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScrollSnapOptions](arkts-arkui-scroll-scrollsnapoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setScrollOptions

```TypeScript
default setScrollOptions(scroller?: Scroller): this
```

设置滚动选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scroller | [Scroller](arkts-arkui-scroll-scroller-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ScrollAttribute](arkts-arkui-scroll-scrollattribute-i.md) |

## zoomScale

```TypeScript
default zoomScale(scale: double | Bindable<double> | undefined): this
```

设置Scroll组件内容的缩放比例。未通过该接口设置时，内容的缩放比例默认为1。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | double \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;double&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |
