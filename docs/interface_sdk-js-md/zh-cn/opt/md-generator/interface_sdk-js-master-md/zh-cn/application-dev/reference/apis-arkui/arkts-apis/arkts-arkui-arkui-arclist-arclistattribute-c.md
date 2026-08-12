# ArcListAttribute

除支持[通用属性](./@internal/component/ets/common)外，还支持以下属性（不支持  
[滚动组件通用属性](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#属性)）：

**继承/实现关系：** ArcListAttribute extends [CommonMethod<ArcListAttribute>](CommonMethod<ArcListAttribute>)

**起始版本：** 18

<!--Device-unnamed-export declare class ArcListAttribute extends CommonMethod<ArcListAttribute>--><!--Device-unnamed-export declare class ArcListAttribute extends CommonMethod<ArcListAttribute>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## cachedCount

```TypeScript
cachedCount(count: Optional<number>): ArcListAttribute
```

设置列表中ArcListItem的预加载数量，懒加载场景只会预加载ArcList显示区域外上下各cachedCount行的ArcListItem，非懒加载场景会全部加载。懒加载、非懒加载都只布局ArcList显示区域+ArcList显示区域外上下各cachedCount行的ArcListItem。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-cachedCount(count: Optional<number>): ArcListAttribute--><!--Device-ArcListAttribute-cachedCount(count: Optional<number>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## chainAnimation

```TypeScript
chainAnimation(enable: Optional<boolean>): ArcListAttribute
```

设置当前ArcList是否启用链式联动动效，开启后列表滑动以及顶部和底部拖拽时会有链式联动的效果。

链式联动效果：ArcList内的ArcListItem间隔一定距离，在基本的滑动交互行为下，主动对象驱动从动对象进行联动，驱动效果遵循弹簧物理动效。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-chainAnimation(enable: Optional<boolean>): ArcListAttribute--><!--Device-ArcListAttribute-chainAnimation(enable: Optional<boolean>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## childrenMainSize

```TypeScript
childrenMainSize(size: Optional<ChildrenMainSize>): ArcListAttribute
```

设置ArcList组件的子组件在主轴方向的大小信息。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-childrenMainSize(size: Optional<ChildrenMainSize>): ArcListAttribute--><!--Device-ArcListAttribute-childrenMainSize(size: Optional<ChildrenMainSize>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ChildrenMainSize](../arkts-components/arkts-arkui-childrenmainsize-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcListAttribute
```

设置表冠响应灵敏度。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcListAttribute--><!--Device-ArcListAttribute-digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [sensitivity](../../apis-localization-kit/arkts-apis/arkts-localization-intl-collatoroptions-i.md) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[CrownSensitivity](arkts-arkui-crownsensitivity-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## enableScrollInteraction

```TypeScript
enableScrollInteraction(enable: Optional<boolean>): ArcListAttribute
```

设置是否支持滚动手势。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-enableScrollInteraction(enable: Optional<boolean>): ArcListAttribute--><!--Device-ArcListAttribute-enableScrollInteraction(enable: Optional<boolean>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## fadingEdge

```TypeScript
fadingEdge(enable: Optional<boolean>): ArcListAttribute
```

设置是否开启边缘渐隐效果。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-fadingEdge(enable: Optional<boolean>): ArcListAttribute--><!--Device-ArcListAttribute-fadingEdge(enable: Optional<boolean>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## flingSpeedLimit

```TypeScript
flingSpeedLimit(speed: Optional<number>): ArcListAttribute
```

限制跟手滑动结束后，惯性滚动动效开始时的最大初始速度。设置为小于等于0的值时，按默认值处理。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-flingSpeedLimit(speed: Optional<number>): ArcListAttribute--><!--Device-ArcListAttribute-flingSpeedLimit(speed: Optional<number>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## friction

```TypeScript
friction(friction: Optional<number>): ArcListAttribute
```

设置摩擦系数，手动滑动滚动区域时生效，仅影响惯性滚动过程。设置为小于等于0的值时，按默认值处理。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-friction(friction: Optional<number>): ArcListAttribute--><!--Device-ArcListAttribute-friction(friction: Optional<number>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [friction](#friction) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onDidScroll

```TypeScript
onDidScroll(handler: Optional<OnScrollCallback>): ArcListAttribute
```

列表滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-onDidScroll(handler: Optional<OnScrollCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onDidScroll(handler: Optional<OnScrollCallback>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[OnScrollCallback](../arkts-components/arkts-arkui-onscrollcallback-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onReachEnd

```TypeScript
onReachEnd(handler: Optional<VoidCallback>): ArcListAttribute
```

列表到达末尾位置时触发。

ArcList边缘效果为弹簧效果时，滑动经过末尾位置时触发一次该事件，回弹返回末尾位置时再触发一次该事件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-onReachEnd(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onReachEnd(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onReachStart

```TypeScript
onReachStart(handler: Optional<VoidCallback>): ArcListAttribute
```

列表到达起始位置时触发。

当ArcList进行初始化时，若[initialIndex](arkts-arkui-arkui-arclist-arklistoptions-i.md#ArkListOptions)设定为0，将触发一次事件。当ArcList滚动至起始位置，亦会触发一次事件。在ArcList的边缘效果设置为弹簧效果时，滑动经过起始位置时会触发一次事件，而在回弹返回起始位置时，将再次触发一次事件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-onReachStart(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onReachStart(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onScrollIndex

```TypeScript
onScrollIndex(handler: Optional<ArcScrollIndexHandler>): ArcListAttribute
```

当子组件划入或划出ArcList的显示区域时，将触发此事件。在ArcList初始化时，此事件会被触发一次。当ArcList显示区域内的首个或末个子组件的索引值发生变化，或是显示区域中心的子组件发生变动时，同样会触发此事件。

ArcList的边缘效果为弹簧效果时，在ArcList滑动到边缘后继续滑动以及松手回弹的过程中，不会触发onScrollIndex事件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-onScrollIndex(handler: Optional<ArcScrollIndexHandler>): ArcListAttribute--><!--Device-ArcListAttribute-onScrollIndex(handler: Optional<ArcScrollIndexHandler>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[ArcScrollIndexHandler](arkts-arkui-arcscrollindexhandler-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onScrollStart

```TypeScript
onScrollStart(handler: Optional<VoidCallback>): ArcListAttribute
```

列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](../arkts-components/arkts-arkui-scroller-c.md#Scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-onScrollStart(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onScrollStart(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onScrollStop

```TypeScript
onScrollStop(handler: Optional<VoidCallback>): ArcListAttribute
```

列表滑动停止时触发。手指拖动列表或列表的滚动条触发的滑动，手指离开屏幕后滑动停止时会触发该事件。使用[Scroller](../arkts-components/arkts-arkui-scroller-c.md#Scroller)滑动控制器触发的带动画的滑动，动画停止会触发该事件。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-onScrollStop(handler: Optional<VoidCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onScrollStop(handler: Optional<VoidCallback>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[VoidCallback](arkts-arkui-voidcallback-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## onWillScroll

```TypeScript
onWillScroll(handler: Optional<OnWillScrollCallback>): ArcListAttribute
```

列表滑动时每帧开始前触发，返回当前帧将要滑动的偏移量和当前滑动状态。返回的偏移量为计算得到的将要滑动的偏移量值，并非最终实际滑动偏移。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-onWillScroll(handler: Optional<OnWillScrollCallback>): ArcListAttribute--><!--Device-ArcListAttribute-onWillScroll(handler: Optional<OnWillScrollCallback>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[OnWillScrollCallback](../arkts-components/arkts-arkui-onwillscrollcallback-t.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## scrollBar

```TypeScript
scrollBar(status: Optional<BarState>): ArcListAttribute
```

设置滚动条状态。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-scrollBar(status: Optional<BarState>): ArcListAttribute--><!--Device-ArcListAttribute-scrollBar(status: Optional<BarState>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;[BarState](arkts-arkui-barstate-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## scrollBarColor

```TypeScript
scrollBarColor(color: Optional<ColorMetrics>): ArcListAttribute
```

设置滚动条的颜色。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-scrollBarColor(color: Optional<ColorMetrics>): ArcListAttribute--><!--Device-ArcListAttribute-scrollBarColor(color: Optional<ColorMetrics>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;ColorMetrics&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## scrollBarWidth

```TypeScript
scrollBarWidth(width: Optional<LengthMetrics>): ArcListAttribute
```

设置ArcList滚动条在按压态下的宽度。未设置时，按压态宽度为LengthMetrics.vp(24)。非按压态宽度固定为LengthMetrics.vp(4)，不受该属性影响。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-scrollBarWidth(width: Optional<LengthMetrics>): ArcListAttribute--><!--Device-ArcListAttribute-scrollBarWidth(width: Optional<LengthMetrics>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |

## space

```TypeScript
space(space: Optional<LengthMetrics>): ArcListAttribute
```

设置列表子项之间的间距。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ArcListAttribute-space(space: Optional<LengthMetrics>): ArcListAttribute--><!--Device-ArcListAttribute-space(space: Optional<LengthMetrics>): ArcListAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [space](#space) | [Optional](../arkts-components/arkts-arkui-optional-t.md)&lt;LengthMetrics&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [ArcListAttribute](arkts-arkui-arkui-arclist-arclistattribute-c.md) |
