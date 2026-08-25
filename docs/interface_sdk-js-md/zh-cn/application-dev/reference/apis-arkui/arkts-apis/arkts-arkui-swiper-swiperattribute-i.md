# SwiperAttribute

除支持通用属性外，还支持以下属性：

> **说明：**&gt;
> Swiper组件通用属性clip的默认值为
> true。

**继承/实现关系：** SwiperAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SwiperAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置Swiper组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## autoPlay

```TypeScript
default autoPlay(value: boolean | undefined): this
```

设置子组件是否自动播放。轮播方向为索引从小到大。  
[loop](#loop)为false时，自动轮播到最后一页时停止轮播。手势切换完成后，如果当前页面不是最后一页，自动轮播将继续播放。当Swiper不可见时会停止轮播。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## autoPlay

```TypeScript
default autoPlay(autoPlay: boolean | undefined, options: AutoPlayOptions | undefined): this
```

设置子组件是否自动播放。options入参控制手指或鼠标按下屏幕时子组件是否停止自动播放。当[loop](#loop)设置为false时，自动轮播将在到达最后一页时停止。在通过手势切换且未处于最后一页的情况下，轮播将继续进行。Swiper在不可见时，轮播也将停止。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [autoPlay](#autoplay) | boolean \| undefined | 是 |
| options | [AutoPlayOptions](arkts-arkui-swiper-autoplayoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## cachedCount

```TypeScript
default cachedCount(value: int | undefined): this
```

设置预加载子组件个数，以当前页面为基准，加载当前显示页面的前后个数。前面item删除，后面会向前补位。例如cachedCount=1时，会将当前显示页面在索引序号上相邻的前一页和后一页的子组件都预加载。如果设置为按组翻页，即 displayCount的swipeByGroup参数设为true，预加载时会以组为基本单位。例如cachedCount=1，swipeByGroup=true时，会将当前组的前面一组和后面一组的子组件都预加载。

> **说明：**&gt;
> - 在连续滑动场景中，一屏显示一个Swiper子组件时，通常将cachedCount值设置为1或2即可。最佳实践请参考
> [优化Swiper组件加载慢丢帧问题-缓存数据项](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-swiper_high_performance_development_guide#section143504547145)
> 。&gt;
> - 只在[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了virtualScroll开关的
> [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)中生效，生效后超出显示及缓存范围的子节点会被释放。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## cachedCount

```TypeScript
default cachedCount(count: int | undefined, isShown: boolean | undefined): this
```

设置预加载子组件个数。

> **说明：**&gt;
> - isShown值为true，且设置的count过大时，如果前后预加载范围内可加载的节点不足，循环场景下同一个可加载节点只会布局在一侧。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | int \| undefined | 是 |
| isShown | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## cachedCount

```TypeScript
default cachedCount(count: int | undefined, options: CachedCountOptions | undefined): this
```

设置预加载子组件个数和配置选项。

> **说明：**&gt;
> - 当options的independent设置为true时，预加载子组件个数按count个数计算，与
> displayCount的分组swipeByGroup
> 计算解耦。例如cachedCount的count为1时，会将当前显示子节点的前一个和后一个子组件预加载。&gt;
> - 当displayCount的swipeByGroup参数设为true，且options的independent为false（默认值）时，预加载子组件个数以组为基本单位。例如cachedCount的count为1，
> displayCount的value为2，displayCount的swipeByGroup为true时，会将当前显示组的前一组和后一组的各两个子组件预加载。&gt;
> - 只在[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)和开启了virtualScroll开关的
> [Repeat](../../../ui/rendering-control/arkts-new-rendering-control-repeat.md)中生效，生效后超出缓存范围的子节点会被释放。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | int \| undefined | 是 |
| options | [CachedCountOptions](arkts-arkui-swiper-cachedcountoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## curve

```TypeScript
default curve(value: Curve | string | ICurve | undefined): this
```

设置Swiper的动画曲线，默认为弹簧插值曲线，常用曲线参考[Curve](arkts-arkui-curve-e.md)，也可以通过 [插值计算](arkts-curves.md)模块提供的接口创建自定义的插值曲线对象。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Curve](arkts-arkui-curve-e.md) \| string \| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## customContentTransition

```TypeScript
default customContentTransition(transition: SwiperContentAnimatedTransition | undefined): this
```

自定义Swiper页面切换动画。在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发回调，开发者可以在回调中设置透明度、缩放比例、位移等属性来自定义切换动画。使用说明：1、循环场景下，设置prevMargin和nextMargin属性，使得Swiper视窗的前后两端区域显示同一页面时，该接口不生效。2、在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发[SwiperContentTransitionProxy](arkts-arkui-swiper-swipercontenttransitionproxy-i.md)回调。例如，当视窗内有下 标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。3、设置displayCount属性的swipeByGroup参数为true时，若同组中至少有一个页面在视窗内时，则会对同组中所有页面触发回调，若同组所有页面均不在视窗内时，则会一起下渲染树。4、在页面跟手滑动和离手后执行切换动画的过程中，默认动画（页面滑动）依然会发生，若希望页面不滑动，可以设置主轴方向上负的位移（translate属性）来抵消页面滑动。例如：当displayCount属性值为2，视窗内有下标为0、1 的两个页面时，页面水平滑动过程中，可以逐帧设置第0页的translate属性在x轴上的值为-position * mainAxisLength来抵消第0页的位移，设置第1页的translate属性在x轴上的值为-(position - 1) * mainAxisLength来抵消第1页的位移。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transition | [SwiperContentAnimatedTransition](arkts-arkui-swiper-swipercontentanimatedtransition-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## disableSwipe

```TypeScript
default disableSwipe(value: boolean | undefined): this
```

设置禁用组件滑动切换功能。适用于仅通过按钮或导航点控制翻页的场景，或需要限制用户滑动操作的场景。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## displayArrow

```TypeScript
default displayArrow(value: ArrowStyle | boolean | undefined, isHoverShow?: boolean | undefined): this
```

设置导航点箭头样式。

> **说明：**&gt;
> Swiper视窗内显示所有子节点时，只显示一屏，无法翻页，左右翻页箭头均不显示。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ArrowStyle](arkts-arkui-swiper-arrowstyle-i.md) \| boolean \| undefined | 是 |
| isHoverShow | boolean \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## displayCount

```TypeScript
default displayCount(value: int | string | SwiperAutoFill | ItemFillPolicy| undefined, swipeByGroup?: boolean | undefined): this
```

设置Swiper视窗内元素显示个数。使用number类型时，子元素主轴宽度会基于Swiper主轴宽度适应。子组件按照主轴均分Swiper宽度（减去displayCount-1个itemSpace）的方式进行主轴拉伸（收缩）布局，设置为小于等于0的值时，按默认值1显示 。使用string类型时，根据子元素的主轴宽度线性布局，不再适应Swiper主轴宽度。此时value值仅支持设置为'auto'，设置 [customContentTransition](#customcontenttransition)和 [onContentDidScroll](#oncontentdidscroll)事件不生效。使用SwiperAutoFill类型时，子元素主轴宽度会基于Swiper主轴宽度适应。通过设置一个子组件最小宽度值minSize，会根据Swiper当前宽度和minSize值自动计算并更改一页内元素显示个数。当minSize为空或 者小于等于0时，Swiper显示1列。

> **说明：**&gt;
> 1.按组进行翻页时，判定翻页的拖拽距离阈值将调整为Swiper宽度的50%（若按子元素翻页，该阈值为子元素宽度的50%）。若最后一组的子元素数量少于displayCount，将利用占位子元素进行填充，占位子元素仅用于布局定位，
> 不显示任何内容，其位置将直接显示Swiper的背景样式。&gt;
> 2.displayCount设置为'auto'，并且设置非循环时，选中导航点的位置与视窗内首个页面的位置保持一致。如果翻页完成后，视窗内首个页面仅部分显示在视窗内，选中导航点亦与页面的位置保持一致，位于两个未选中的导航点之间。
> 在此情况下，建议开发者隐藏导航点。&gt;
> 3.导航点样式设定为圆形导航点，视窗内显示子元素数量等于1时（单页场景）或者 displayCount设置为'auto'时，显示导航点数量等于子元素数量。&gt;
> 4.displayCount设置为'auto'时，若设置swipeByGroup为true，则单个子元素按组翻页，一次只能翻一页。在此情况下，建议开发者不设置swipeByGroup或者设置swipeByGroup为false
> 。
当导航点样式设定为圆形导航点，视窗内显示子元素数量大于1（多页场景），显示导航点数量情况如下表：  
| 子元素总数量是否大于视窗内显示的子元素数量 | 是否按组翻页 | 是否循环 | 圆形导航点显示数量 | 说明 | | ------------------------------------------ | ------------ | --------------- | ----------------------------------- ------------------------- | ---------------------------------------- | | 是 | 是 | loop设置为true | 圆形导航点的数量将与组数相等（组数计算方式为子元素总数量除以视窗内显示的子元素数 量，若除不尽，则向上取整） | 该效果在displayCount设置为'auto'时不生效 | | 是 | 是 | loop设置为false | 圆形导航点的数量将与组数相等（组数计算方式为子元素总数量除以视窗内显示的子元素数 量，若除不尽，则向上取整） | 该效果在displayCount设置为'auto'时不生效 | | 是 | 否 | loop设置为true | 圆形导航点的数量将与实际可翻页次数一致（显示导航点的数量等于子元素总数量） | —— | | 是 | 否 | loop设置为false | 圆形导航点的数量将与实际可翻页次数一致（计算方式是子元素的总 数量减去视窗内显示的子元素数量+1个） | 该效果在displayCount设置为'auto'时不生效 | | 否（同时子元素的总数量大于0） | —— | —— | 显示1个圆形导航点 | 该效果在 displayCount设置为'auto'时不生效 | | 否（同时子元素的总数量等于0） | —— | —— | 显示0个圆形导航点 |

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- API版本23+：SystemCapability.ArkUI.ArkUI.Full
- API版本23+：SystemCapability.ArkUI.ArkUI.Full
- API版本23+：SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full *

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| string \| [SwiperAutoFill](arkts-arkui-swiper-swiperautofill-i.md) \| [ItemFillPolicy](arkts-arkui-itemfillpolicy-i.md) \| undefined | 是 |
| swipeByGroup | boolean \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## displayMode

```TypeScript
default displayMode(value: SwiperDisplayMode | undefined): this
```

设置主轴方向上元素排列的模式，优先以displayCount 设置的个数显示，displayCount未设置时本属性生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SwiperDisplayMode](arkts-arkui-swiper-swiperdisplaymode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## duration

```TypeScript
default duration(value: int | undefined): this
```

设置子组件切换的动画时长。duration需要和[curve](#curve)一起使用。curve默认曲线为[interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md)，此时动画时长只受曲线自身参数影响，不再受duration 的控制。不受duration控制的曲线可以查阅[插值计算](arkts-curves.md)模块，比如， [springMotion](arkts-arkui-curves-springmotion-f.md)、 [responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md)和interpolatingSpring类型的曲线不受 duration控制。如果希望动画时长受到duration控制，需要给curve设置其他曲线。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## effectMode

```TypeScript
default effectMode(value: EdgeEffect | undefined): this
```

设置边缘滑动效果，[loop](#loop)为false或Swiper视窗内一屏显示所有子节点时生效。调用 SwiperController.changeIndex() 、[SwiperController.showNext()](arkts-arkui-swiper-swipercontroller-c.md#shownext)和 [SwiperController.showPrevious()](arkts-arkui-swiper-swipercontroller-c.md#showprevious)接口跳转至首尾页时不生效回弹。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## index

```TypeScript
default index(value: int | Bindable<int> | undefined): this
```

设置当前在容器中显示的子组件的索引值。设置小于0或大于等于子组件数量时，按照默认值0处理。从API version 10开始，该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;int&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## indicator

```TypeScript
default indicator(indicator: IndicatorComponentController | DotIndicator | DigitIndicator | boolean | undefined): this
```

设置可选导航点指示器样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [indicator](#indicator) | [IndicatorComponentController](../arkts-components/arkts-arkui-indicatorcomponentcontroller-c.md) \| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) \| [DigitIndicator](arkts-arkui-swiper-digitindicator-c.md) \| boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## indicatorInteractive

```TypeScript
default indicatorInteractive(value: boolean | undefined): this
```

设置导航点是否可交互。适用于需要通过其他方式（如按钮）控制翻页，或需要禁止用户通过导航点点击翻页的场景。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## interval

```TypeScript
default interval(value: int | undefined): this
```

设置使用自动播放时播放的时间间隔。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## itemSpace

```TypeScript
default itemSpace(value: double | string | undefined): this
```

设置子组件与子组件之间间隙。不支持设置百分比。类型为number或double时，默认单位vp。类型为string时，需要显式指定像素单位，如'10px'；未指定像素单位时，如'10'，单位为vp。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## loop

```TypeScript
default loop(value: boolean | undefined): this
```

设置是否开启循环。在LazyForEach懒循环加载模式下，加载的组件数量建议大于5个。预加载的组件数量不足时，可能会导致快速切换时出现空白或卡顿。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## maintainVisibleContentPosition

```TypeScript
default maintainVisibleContentPosition(enabled: boolean | undefined): this
```

设置显示区域上方或前方插入或删除数据时是否保持可见内容位置不变。适用于使用单一 [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)作为Swiper子节点的情况，通过LazyForEach的 [onDataAdd](../arkts-components/arkts-arkui-datachangelistener-i.md#ondataadd)、 [onDataDelete](../arkts-components/arkts-arkui-datachangelistener-i.md#ondatadelete)等接口修改数据源。其他场景下，显 示区域上方或前方插入或删除数据，可见内容位置会变化。在displayCount属性的swipeByGroup参数 设置为true，即按组翻页生效时，一次在显示区域上方或前方插入或删除数据，且插入或删除的是一组节点数量倍数的数据量时，才能保持可见内容位置不变，否则可见内容位置可能会随每组数据重新分组改变。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## nestedScroll

```TypeScript
default nestedScroll(value: SwiperNestedScrollMode | undefined): this
```

设置Swiper组件和父组件的嵌套滚动模式。当Swiper嵌套在滚动容器（如List、Scroll）中时，需要根据业务需求选择合适的嵌套滚动模式。[loop](#loop)为true时Swiper组件没有边缘，不会触发父组件嵌套滚动。

> **说明：**&gt;
> 由于Swiper的抛滑动画逻辑和其它滚动类组件不同（Swiper一次只能滑动一页，抛滑时做翻页动画），当Swiper内嵌套其它滚动组件时，如果Swiper的翻页动画已经启动，将无法接受子节点上传的滚动偏移量。这时Swiper的
> 翻页动画和子节点的边缘效果动画会同时执行。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SwiperNestedScrollMode](arkts-arkui-swiper-swipernestedscrollmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## nextMargin

```TypeScript
default nextMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this
```

当主轴方向为横向布局时，nextMargin或prevMargin中任意一个大于子组件测算的宽度，nextMargin和prevMargin均不显示。当主轴方向为纵向布局时，nextMargin或prevMargin中任意一个大于子组件测算的高度，nextMargin和prevMargin均不显示。使用nextMargin/prevMargin接口时，不要对子组件进行 [尺寸范围限制](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#constraintsize)，否则子节点主轴将不会被拉伸到预期长度 ，边距失去效果。

> **说明：**&gt;
> 该接口不支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |
| ignoreBlank | boolean \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onAnimationEnd

```TypeScript
default onAnimationEnd(event: OnSwiperAnimationEndCallback | undefined): this
```

切换动画结束时触发该回调。当Swiper切换动效结束时触发，包括动画过程中手势中断，通过SwiperController调用finishAnimation。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnSwiperAnimationEndCallback](arkts-arkui-onswiperanimationendcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onAnimationStart

```TypeScript
default onAnimationStart(event: OnSwiperAnimationStartCallback | undefined): this
```

切换动画开始时触发该回调。

> **说明：**&gt;
> - 调用此回调后，切换动画的逻辑将在渲染线程中执行，从而使处于空闲状态的主线程能够充分利用这段时间来加载子组件所需资源，减少后续在cachedCount范围内节点的预加载时间。最佳实践请参考
> [优化Swiper组件加载慢丢帧问题-提前加载数据](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-swiper_high_performance_development_guide#section8783121513246)
> 。&gt;
> - 当翻页动画时长为0时，只有以下场景会触发该回调：滑动翻页、自动轮播、调用SwiperController.showNext()和SwiperController.showPrevious()接口以及手指点击导航点翻页。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnSwiperAnimationStartCallback](arkts-arkui-onswiperanimationstartcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onChange

```TypeScript
default onChange(event: Callback<int> | undefined): this
```

当前显示元素索引变化时触发该事件，返回值为当前显示元素的索引值。Swiper组件结合LazyForEach使用时，不能在onChange事件里触发子页面UI的刷新。

> **说明：**&gt;
> 如果是动画引起的索引变化，回调在动画结束时触发。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onContentDidScroll

```TypeScript
default onContentDidScroll(handler: ContentDidScrollCallback | undefined): this
```

监听Swiper页面滑动事件。使用说明：1、循环场景下，设置prevMargin和nextMargin属性，使得Swiper视窗的前后两端区域显示同一页面时，该接口不生效。2、在页面滑动过程中，会对视窗内所有页面逐帧触发[ContentDidScrollCallback](arkts-arkui-contentdidscrollcallback-t.md)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次 index值分别为0和1的回调。3、设置displayCount属性的swipeByGroup参数为true时，若同组中至少有一个页面在视窗内时，则会对同组中所有页面触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [ContentDidScrollCallback](arkts-arkui-contentdidscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onContentWillScroll

```TypeScript
default onContentWillScroll(handler: ContentWillScrollCallback | undefined): this
```

Swiper滑动行为拦截事件，在滑动前触发。Swiper会依据该事件的返回值来决定是否允许此次滑动行为。若返回true，表示允许此次滑动行为，Swiper页面将跟随滑动。若返回false，表示不允许此次滑动，页面将保持静止。
1. 触发该事件的场景仅限于手势操作，具体包括手指滑动、滚动鼠标滚轮以及使用键盘方向键进行焦点移动。
2. 在手指滑动的过程中，每帧都将触发该事件，系统会依据事件的返回值判断是否对每帧的滑动做出响应。
3. 对于滚动鼠标滚轮和使用键盘方向键进行焦点移动的场景，每次翻页操作都会触发一次该事件，翻页是否被允许将根据事件的返回值来决定。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| handler | [ContentWillScrollCallback](arkts-arkui-contentwillscrollcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onGestureSwipe

```TypeScript
default onGestureSwipe(event: OnSwiperGestureSwipeCallback | undefined): this
```

在页面跟手滑动过程中，逐帧触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [OnSwiperGestureSwipeCallback](arkts-arkui-onswipergestureswipecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onScrollStateChanged

```TypeScript
default onScrollStateChanged(event: Callback<ScrollState> | undefined): this
```

Swiper滑动状态变化事件回调，在跟手滑动、离手动画、停止三种滑动状态变化时触发，返回值为当前滑动状态。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onSelected

```TypeScript
default onSelected(event: Callback<int> | undefined): this
```

当选中元素改变时触发该回调，返回值为当前选中的元素的索引值。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onUnselected

```TypeScript
default onUnselected(event: Callback<int> | undefined): this
```

当选中元素改变时触发该回调，返回值为将要隐藏的元素的索引值。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## pageFlipMode

```TypeScript
default pageFlipMode(mode: PageFlipMode | undefined): this
```

设置鼠标滚轮翻页模式。未通过该接口设置时，默认为连续翻页模式，取值为PageFlipMode.CONTINUOUS。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## prevMargin

```TypeScript
default prevMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this
```

设置前边距，用于露出前一项的一小部分，使用效果可以参考 示例1设置导航点交互及翻页动效。仅当Swiper子组件的 布局方式为拉伸时生效，主要包括两种场景：1、displayMode属性设置为SwiperDisplayMode.STRETCH；2、displayCount属性设置为number类型。当主轴方向为横向布局时，nextMargin/prevMargin中任意一个大于子组件测算的宽度，nextMargin和prevMargin均不显示。当主轴方向为纵向布局时，nextMargin/prevMargin中任意一个大于子组件测算的高度，nextMargin和prevMargin均不显示。使用nextMargin/prevMargin接口时，不要对子组件进行 [尺寸范围限制](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md#constraintsize)，否则子节点主轴将不会被拉伸到预期长度 ，边距失去效果。

> **说明：**&gt;
> 该接口不支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |
| ignoreBlank | boolean \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## setSwiperOptions

```TypeScript
default setSwiperOptions(controller?: SwiperController): this
```

设置滑动器选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | [SwiperController](arkts-arkui-swiper-swipercontroller-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## vertical

```TypeScript
default vertical(value: boolean | undefined): this
```

设置是否为纵向滑动。

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
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |
