# Scroll属性/事件

除支持通用属性和[滚动组件通用属性](arkts-arkui-scrollablecommonmethod-c.md)外，还 支持以下属性：除支持通用事件和[滚动组件通用事件](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#事件)外，还 支持以下事件：

**继承/实现关系：** ScrollAttribute extends ScrollableCommonMethod<ScrollAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## edgeEffect

```TypeScript
edgeEffect(edgeEffect: EdgeEffect, options?: EdgeEffectOptions)
```

设置边缘滑动效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [edgeEffect](#edgeeffect) | [EdgeEffect](../arkts-apis/arkts-arkui-edgeeffect-e.md) | 是 |
| options | [EdgeEffectOptions](arkts-arkui-edgeeffectoptions-i.md) | 否 |

## enableBouncesZoom

```TypeScript
enableBouncesZoom(enable: boolean)
```

设置是否启用过缩放回弹效果。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## enablePaging

```TypeScript
enablePaging(value: boolean)
```

设置是否支持滑动翻页。如果同时设置了滑动翻页enablePaging和限位滚动scrollSnap，则scrollSnap优先生效，enablePaging不生效。可用于书籍翻页、卡片分页浏览等场景。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean)
```

设置是否支持滚动手势。可用于在自定义拖动、自定义滚动等业务需要接管滑动手势的场景中，临时禁用滚动组件的用户手势滚动。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## friction

```TypeScript
friction(value: number | Resource)
```

设置摩擦系数，手动滑动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## initialOffset

```TypeScript
initialOffset(value: OffsetOptions)
```

设置初始滚动偏移量。只在首次布局时生效，后续动态修改该属性值不生效。可用于页面首次显示时定位到指定滚动位置。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [OffsetOptions](arkts-arkui-offsetoptions-i.md) | 是 |

## maxZoomScale

```TypeScript
maxZoomScale(scale: number)
```

设置Scroll组件内容的最大手势缩放比例。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number | 是 |

## minZoomScale

```TypeScript
minZoomScale(scale: number)
```

设置Scroll组件内容的最小手势缩放比例。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number | 是 |

## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions)
```

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。适用于页面内列表与外层滚动区域联动等嵌套滚动场景。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NestedScrollOptions](arkts-arkui-nestedscrolloptions-i.md) | 是 |

## onDidScroll

```TypeScript
onDidScroll(handler: ScrollOnScrollCallback)
```

滚动事件回调，Scroll滚动时触发。返回当前帧滚动的偏移量和当前滚动状态。触发该事件的条件：
1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用。
3. 越界回弹。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [ScrollOnScrollCallback](arkts-arkui-scrollonscrollcallback-t.md) | 是 |

## onDidZoom

```TypeScript
onDidZoom(event: ScrollOnDidZoomCallback)
```

每帧缩放完成时触发。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [ScrollOnDidZoomCallback](arkts-arkui-scrollondidzoomcallback-t.md) | 是 |

## onScroll

```TypeScript
onScroll(event: (xOffset: number, yOffset: number) => void)
```

滚动事件回调，返回滚动时水平、竖直方向偏移量，单位vp。触发该事件的条件：
1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用。
3. 越界回弹。

**起始版本：** 7

**废弃版本：** 12

**替代接口：** onWillScroll

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (xOffset: number, yOffset: number) = & gt; void | 是 |

## onScrollEdge

```TypeScript
onScrollEdge(event: OnScrollEdgeCallback)
```

滚动到边缘事件回调。触发该事件的条件：
1. 滚动组件滚动到边缘时触发，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用。
3. 越界回弹。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnScrollEdgeCallback](arkts-arkui-onscrolledgecallback-t.md) | 是 |

## onScrollEnd

```TypeScript
onScrollEnd(event: () => void)
```

滚动停止事件回调。触发该事件的条件：
1. 滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用后停止，带过渡动效。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** onScrollStop

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback)
```

该接口回调时，事件参数传入即将发生的滚动量，事件处理函数中可根据应用场景计算实际需要的滚动量并作为事件处理函数的返回值返回，Scroll将按照返回值的实际滚动量进行滚动。支持[offsetRemain](arkts-arkui-onscrollframebeginhandlerresult-i.md)为负值。若通过onScrollFrameBegin事件和[scrollBy](arkts-arkui-scroller-c.md#scrollby)方法实现容器嵌套滚动，需设置子滚动节点的 [EdgeEffect](#edgeeffect)为None。如Scroll嵌套List滚动时，List组件的 edgeEffect属性需设置为EdgeEffect.None，否则抛滑List，会触发List的边缘回弹动画，导致嵌套滚动失效。满足以下任一条件时触发该事件：
1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. Scroll惯性滚动。
3. 调用[fling](arkts-arkui-scroller-c.md#fling)接口触发滚动。
不触发该事件的条件：
1. 调用除[fling](arkts-arkui-scroller-c.md#fling)接口外的其他滚动控制接口。
2. 越界回弹。
3. 拖动滚动条。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnScrollFrameBeginCallback](arkts-arkui-onscrollframebegincallback-t.md) | 是 |

## onScrollStart

```TypeScript
onScrollStart(event: VoidCallback)
```

滚动开始时触发。手指拖动Scroll或拖动Scroll的滚动条触发的滚动开始时，会触发该事件。使用[Scroller](arkts-arkui-scroller-c.md)滚动控制器触发的带动画的滚动，动画开始时会触发该事件。触发该事件的条件：
1. 滚动组件开始滚动时触发，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用后开始，带过渡动效。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | 是 |

## onScrollStop

```TypeScript
onScrollStop(event: VoidCallback)
```

滚动停止时触发。手拖动Scroll或拖动Scroll的滚动条触发的滚动，手离开屏幕后滚动停止时会触发该事件。使用[Scroller](arkts-arkui-scroller-c.md)滚动控制器触发的带动画的滚动，动画停止时会触发该事件。触发该事件的条件：
1. 滚动组件触发滚动后停止，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用后开始，带过渡动效。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | 是 |

## onWillScroll

```TypeScript
onWillScroll(handler: ScrollOnWillScrollCallback)
```

滚动事件回调，Scroll滚动前触发。回调当前帧将要滚动的偏移量和当前滚动状态和滚动操作来源，其中回调的偏移量为计算得到的将要滚动的偏移量值，并非最终实际滚动偏移。可以通过该回调返回值指定Scroll将要滚动的偏移。触发该事件的条件：
1. 滚动组件触发滚动时触发，支持键鼠操作等其他触发滚动的输入设置。
2. 通过滚动控制器API接口调用。
3. 越界回弹。

> **说明：**&gt;
> 滚动事件的回调函数在滚动过程中会被频繁触发，因此应避免在该回调函数中执行耗时操作，以防止应用出现卡顿和丢帧的问题。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [ScrollOnWillScrollCallback](arkts-arkui-scrollonwillscrollcallback-t.md) | 是 |

## onZoomStart

```TypeScript
onZoomStart(event: VoidCallback)
```

手势缩放开始触发。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | 是 |

## onZoomStop

```TypeScript
onZoomStop(event: VoidCallback)
```

手势缩放停止时触发。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](../arkts-apis/arkts-arkui-voidcallback-t.md) | 是 |

## scrollable

```TypeScript
scrollable(value: ScrollDirection)
```

设置滚动方向。该值被修改后会重置滚动偏移量。可根据布局选择竖直滚动、水平滚动或自由滚动。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScrollDirection](arkts-arkui-scrolldirection-e.md) | 是 |

## scrollBar

```TypeScript
scrollBar(barState: BarState)
```

设置滚动条状态。如果容器组件无法滚动，则滚动条不显示。如果容器组件的子组件大小为无穷大，则滚动条不支持拖动和伴随滚动。可用于控制滚动条是否常驻显示、自动显示或隐藏。从API version 10开始，当滚动组件存在圆角时，为避免滚动条被圆角截断，滚动条会自动计算距顶部和底部的避让距离。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| barState | [BarState](../arkts-apis/arkts-arkui-barstate-e.md) | 是 |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string)
```

设置滚动条的颜色。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | Color \| number \| string | 是 |

## scrollBarColor

```TypeScript
scrollBarColor(color: Color | number | string | Resource)
```

设置滚动条的颜色。与[scrollBarColor](#scrollbarcolor)相比，color参数开始支持 Resource类型。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | Color \| number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string)
```

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的可视尺寸，则滚动条的宽度会变为默认值4vp。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string | 是 |

## scrollBarWidth

```TypeScript
scrollBarWidth(value: number | string | Resource)
```

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Scroll组件主轴方向的可视尺寸，则滚动条的宽度会变为默认值4vp，支持Resource资源类型。未通过该接口设置时，设置滚动条的宽度为4vp。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## scrollSnap

```TypeScript
scrollSnap(value: ScrollSnapOptions)
```

设置Scroll组件的限位滚动模式，用于实现分页滚动、卡片对齐等需要滚动结束后定位到指定位置的场景。限位动画期间[onWillScroll](#onwillscroll)事件上报的滚动操作来源类型为ScrollSource.FLING。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScrollSnapOptions](arkts-arkui-scrollsnapoptions-i.md) | 是 |

## zoomScale

```TypeScript
zoomScale(scale: number)
```

设置Scroll组件内容的缩放比例。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number | 是 |
