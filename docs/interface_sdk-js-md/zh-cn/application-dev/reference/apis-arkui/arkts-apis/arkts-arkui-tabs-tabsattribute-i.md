# TabsAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** TabsAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## animationCurve

```TypeScript
default animationCurve(curve: Curve | ICurve| undefined): this
```

设置Tabs翻页动画曲线。常用曲线参考[Curve](arkts-arkui-curve-e.md)，也可以通过 [插值计算](arkts-curves.md)模块提供的接口创建自定义的插值曲线对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) \| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## animationDuration

```TypeScript
default animationDuration(value: int | undefined): this
```

设置Tabs翻页动画时长。animationCurve不设置时，由于滑动TabContent翻页动画曲线interpolatingSpring(-1, 1, 228, 30)时长只受曲线自身参数影响，animationDuration只能控制点击 TabBar页签和调用TabsController的changeIndex接口切换TabContent的动画时长。不受animationDuration控制的曲线可以查阅[插值计算](arkts-curves.md)模块，比如 [springMotion](arkts-arkui-curves-springmotion-f.md)、 [responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md)和 [interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md)类型的曲线。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## animationMode

```TypeScript
default animationMode(mode: AnimationMode | undefined): this
```

设置点击[TabBar](../../../reference/apis-arkui/arkui-ts/ts-container-tabcontent.md#tabbar)页签或调用TabsController的 [changeIndex](arkts-arkui-tabs-tabscontroller-c.md#changeindex)接口时切换TabContent的动画形式。

> **说明：**&gt;
> 此属性不支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [AnimationMode](arkts-arkui-tabs-animationmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TabsAttribute> |
        AttributeModifier<CommonMethod> | undefined): this
```

动态设置Tabs组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundBlurStyle

```TypeScript
default barBackgroundBlurStyle(value: BlurStyle | undefined): this
```

设置TabBar的背景模糊材质。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundBlurStyle

```TypeScript
default barBackgroundBlurStyle(style: BlurStyle | undefined, options: BackgroundBlurStyleOptions | undefined): this
```

为TabBar提供一种在背景和内容之间的模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | 是 |
| options | [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundColor

```TypeScript
default barBackgroundColor(value: ResourceColor | undefined): this
```

设置TabBar的背景颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundEffect

```TypeScript
default barBackgroundEffect(options: BackgroundEffectOptions | undefined): this
```

设置TabBar背景属性，包含背景模糊半径，亮度，饱和度，颜色等参数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barGridAlign

```TypeScript
default barGridAlign(value: BarGridColumnOptions | undefined): this
```

以栅格化方式设置TabBar的可见区域。具体参见BarGridColumnOptions对象。仅水平模式下有效， [不适用于XS、XL和XXL设备](../../../ui/arkts-layout-development-grid-layout.md#栅格容器断点)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BarGridColumnOptions](arkts-arkui-tabs-bargridcolumnoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barHeight

```TypeScript
default barHeight(value: Length | undefined): this
```

设置TabBar的高度值。横向Tabs可以设置height为'auto'，让TabBar自适应子组件高度。height设置为小于0或大于Tabs高度值时，按默认值显示。API version 14之前的版本，若设置barHeight为固定值后，TabBar无法扩展底部安全区。从API version 14开始支持配合 safeAreaPadding属性，当 safeAreaPadding不设置bottom或者bottom设置为0时，可以实现扩展安全区。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barHeight

```TypeScript
default barHeight(value: Length | undefined, noMinHeightLimit: boolean| undefined): this
```

设置TabBar的高度值。横向Tabs可以设置height为'auto'，让TabBar自适应子组件高度，并通过设置noMinHeightLimit为true让自适应高度可以小于TabBar默认高度。height设置为小于0或 大于Tabs高度值时，按默认值显示。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |
| noMinHeightLimit | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barMode

```TypeScript
default barMode(value: BarMode | undefined, options?: ScrollableBarModeOptions | undefined): this
```

设置TabBar布局模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BarMode](arkts-arkui-tabs-barmode-e.md) \| undefined | 是 |
| options | [ScrollableBarModeOptions](arkts-arkui-tabs-scrollablebarmodeoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barOverlap

```TypeScript
default barOverlap(value: boolean | undefined): this
```

设置TabBar是否背后变模糊并叠加在TabContent之上。

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barPosition

```TypeScript
default barPosition(value: BarPosition | undefined): this
```

设置Tabs的页签位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [BarPosition](arkts-arkui-tabs-barposition-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barWidth

```TypeScript
default barWidth(value: Length | undefined): this
```

设置TabBar的宽度值。设置为小于0或大于Tabs宽度值时，按默认值显示。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## cachedMaxCount

```TypeScript
default cachedMaxCount(count: int | undefined, mode: TabsCacheMode | undefined): this
```

设置子组件的最大缓存个数及缓存模式。未设置该属性时默认缓存所有子组件且缓存后不会释放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | int \| undefined | 是 |
| mode | [TabsCacheMode](arkts-arkui-tabs-tabscachemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## customContentTransition

```TypeScript
default customContentTransition(delegate: TabsCustomContentTransitionCallback | undefined): this
```

自定义Tabs页面切换动画。使用说明：
1. 当使用自定义切换动画时，Tabs组件自带的默认切换动画会被禁用，同时，页面也无法跟手滑动。
2. 当设置为undefined时，表示不使用自定义切换动画，仍然使用组件自带的默认切换动画。
3. 当前自定义切换动画不支持打断。
4. 目前自定义切换动画只支持两种场景触发：点击页签和调用TabsController.changeIndex()接口。
5. 当使用自定义切换动画时，Tabs组件支持的事件中，除了[onGestureSwipe](#ongestureswipe)，其他事件均支持。
6. [onChange](#onchange)和[onAnimationEnd](#onanimationend)事件的触发时机需要特殊说明：如果在第一次自定义动画执行过程中，触发了第二次自定义动画，那么在开始第二次自定义动画时，就会触发第一次自定义动画的onChange和onAnimationEnd事件。
7. 当使用自定义动画时，参与动画的页面布局方式会改为Stack布局。如果开发者未主动设置相关页面的zIndex属性，那么所有页面的zIndex值是一样的，页面的渲染层级会按照在组件树上的顺序（即页面的index值顺序）确定。因此，开发者需要主动修改页面的zIndex属性，来控制页面的渲染层级。
8. 此属性不支持在attributeModifier中调用。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| delegate | [TabsCustomContentTransitionCallback](arkts-arkui-tabscustomcontenttransitioncallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## divider

```TypeScript
default divider(value: DividerStyle | null | undefined): this
```

设置区分TabBar和TabContent的分割线样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | DividerStyle \| null \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## edgeEffect

```TypeScript
default edgeEffect(edgeEffect: EdgeEffect | undefined): this
```

设置边缘滑动效果。

> **说明：**&gt;
> 从API version 17开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [edgeEffect](#edgeeffect) | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## fadingEdge

```TypeScript
default fadingEdge(value: boolean | undefined): this
```

设置页签超过容器宽度时是否渐隐消失。建议配合[barBackgroundColor](#barbackgroundcolor)属性一起使用，如果barBackgroundColor属性没有 定义，会默认显示页签末端为白色的渐隐效果。

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## nestedScroll

```TypeScript
default nestedScroll(value: TabsNestedScrollMode | undefined): this
```

设置Tabs组件与其父组件的嵌套滚动模式。未通过该接口设置时，默认嵌套滚动模式为[SELF_ONLY](arkts-arkui-tabs-tabsnestedscrollmode-e.md)。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TabsNestedScrollMode](arkts-arkui-tabs-tabsnestedscrollmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onAnimationEnd

```TypeScript
default onAnimationEnd(handler: OnTabsAnimationEndCallback | undefined): this
```

切换动画结束时触发该回调，包括动画过程中手势中断。当animationDuration为0时动画关闭，不触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnTabsAnimationEndCallback](arkts-arkui-ontabsanimationendcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onAnimationStart

```TypeScript
default onAnimationStart(handler: OnTabsAnimationStartCallback | undefined): this
```

切换动画开始时触发该回调。当[animationDuration](#animationduration)为0时动画关闭且 [scrollable](#scrollable)为false时，不触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnTabsAnimationStartCallback](arkts-arkui-ontabsanimationstartcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onChange

```TypeScript
default onChange(event: Callback<int> | undefined): this
```

Tab页签切换后触发的事件。满足以下任一条件，即可触发该事件：1、滑动页面进行页面切换时，组件滑动动画结束后触发。2、通过[控制器](arkts-arkui-tabs-tabscontroller-c.md)调用[changeIndex](arkts-arkui-tabs-tabscontroller-c.md#changeindex)接口，Tab页签切换后触发。3、动态修改[状态变量](../../../ui/state-management/arkts-state.md)构造的index属性值，Tab页签切换后触发。4、点击TabBar页签，Tab页签切换后触发。

> **说明：**&gt;
> 使用自定义页签时，在onChange事件中联动可能会导致滑动页面切换后才执行页签联动，引起自定义页签切换效果延迟。建议在
> [onAnimationStart](#onanimationstart)中监听并刷新当前索引，以确保动效能够及时触发。具体实现可参考
> 示例3。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onContentDidScroll

```TypeScript
default onContentDidScroll(handler: OnTabsContentDidScrollCallback | undefined): this
```

监听Tabs页面滑动事件。在页面滑动过程中，会对视窗内所有页面逐帧触发[OnTabsContentDidScrollCallback](arkts-arkui-ontabscontentdidscrollcallback-t.md)回调。例如，当视窗内有下标为0、1的两个页 面时，会每帧触发两次index值分别为0和1的回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnTabsContentDidScrollCallback](arkts-arkui-ontabscontentdidscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onContentWillChange

```TypeScript
default onContentWillChange(handler: OnTabsContentWillChangeCallback | undefined): this
```

自定义Tabs页面切换拦截事件能力，新页面即将显示时触发该回调。满足以下任一条件，即可触发该事件：1、滑动TabContent切换新页面时触发。2、通过TabsController.[changeIndex](arkts-arkui-tabs-tabscontroller-c.md#changeindex)接口切换新页面时触发。3、通过动态修改index属性值切换新页面时触发。4、通过点击TabBar页签切换新页面时触发。5、TabBar页签获焦后，通过键盘左右方向键等切换新页面时触发。

> **说明：**&gt;
> 从API version 20开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnTabsContentWillChangeCallback](arkts-arkui-ontabscontentwillchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onGestureSwipe

```TypeScript
default onGestureSwipe(handler: OnTabsGestureSwipeCallback | undefined): this
```

在页面跟手滑动过程中，逐帧触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [OnTabsGestureSwipeCallback](arkts-arkui-ontabsgestureswipecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onSelected

```TypeScript
default onSelected(event: Callback<int> | undefined): this
```

当选中元素改变时触发该回调，返回值为当前选中的元素的索引值。满足以下任一条件，即可触发该事件：
1. 滑动离手时满足翻页阈值，开始切换动画时触发。
2. 通过[TabsController控制器](arkts-arkui-tabs-tabscontroller-c.md)调用[changeIndex](arkts-arkui-tabs-tabscontroller-c.md#changeindex)接口，开始切换动画时触发。
3. 动态修改[状态变量](../../../ui/state-management/arkts-state.md)构造的index属性值后触发。
4. 通过页签处点击触发。

> **说明：**&gt;
> onSelected回调中不可通过[TabsOptions](arkts-arkui-tabs-tabsoptions-i.md)的index设置当前显示页的索引，不可调用TabsController.changeIndex()方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onTabBarClick

```TypeScript
default onTabBarClick(event: Callback<int> | undefined): this
```

Tab页签点击后触发的事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onUnselected

```TypeScript
default onUnselected(event: Callback<int> | undefined): this
```

当选中元素改变时触发该回调，返回值为将要隐藏的元素的索引值。满足以下任一条件，即可触发该事件：
1. 滑动离手时满足翻页阈值，开始切换动画时触发。
2. 通过[TabsController控制器](arkts-arkui-tabs-tabscontroller-c.md)调用[changeIndex](arkts-arkui-tabs-tabscontroller-c.md#changeindex)接口，开始切换动画时触发。
3. 动态修改[状态变量](../../../ui/state-management/arkts-state.md)构造的index属性值后触发。
4. 通过页签处点击触发。

> **说明：**&gt;
> onUnselected回调中不可通过[TabsOptions](arkts-arkui-tabs-tabsoptions-i.md)的index设置当前显示页的索引，不可调用TabsController.changeIndex()方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## pageFlipMode

```TypeScript
default pageFlipMode(mode: PageFlipMode | undefined): this
```

设置鼠标滚轮翻页模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [PageFlipMode](arkts-arkui-pageflipmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## scrollable

```TypeScript
default scrollable(value: boolean | undefined): this
```

设置是否可以通过滑动页面进行页面切换。

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## setTabsOptions

```TypeScript
default setTabsOptions(options?: TabsOptions): this
```

设置Tbas选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TabsOptions](arkts-arkui-tabs-tabsoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## vertical

```TypeScript
default vertical(value: boolean | undefined): this
```

设置是否为纵向Tabs。

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |
