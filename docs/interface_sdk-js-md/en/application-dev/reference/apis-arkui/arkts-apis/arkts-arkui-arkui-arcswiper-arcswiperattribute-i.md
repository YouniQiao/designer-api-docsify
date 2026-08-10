# ArcSwiperAttribute

除支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)外，还支持以下属性，不支持[Menu控制](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)。

**Inheritance/Implementation:** ArcSwiperAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcSwiperAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ArcSwiperAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from 'kits/@kit.ArkUI';
```

## customContentTransition

```TypeScript
default customContentTransition(transition: ArcSwiperContentAnimatedTransition | undefined): this
```

自定义ArcSwiper页面切换动画。在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发回调，开发者可在回调中设置透明度、缩放比例、位移等属性。

在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发  
[SwiperContentTransitionProxy](../../../reference/apis-arkui/arkui-ts/ts-container-arcswiper copy.md#swipercontenttransitionproxy)回调。例如，当视窗内有下标为0、1的两个页面时，会每帧触发两次index值分别为0和1的回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default customContentTransition(transition: ArcSwiperContentAnimatedTransition | undefined): this--><!--Device-ArcSwiperAttribute-default customContentTransition(transition: ArcSwiperContentAnimatedTransition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transition | [ArcSwiperContentAnimatedTransition](arkts-arkui-arkui-arcswiper-arcswipercontentanimatedtransition-i.md) \| undefined | Yes | ArcSwiper自定义切换动画相关信息。&lt;br/&gt;取值为undefined时，无回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

设置旋转表冠的灵敏度。未通过该接口设置时，旋转表冠的灵敏度默认为CrownSensitivity.MEDIUM。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this--><!--Device-ArcSwiperAttribute-default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | Yes | 旋转表冠的灵敏度。设置不同灵敏度级别可调整表冠滚动的响应速度。&lt;br/&gt;取值为undefined时，旋转表冠的灵敏度为CrownSensitivity.MEDIUM。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## disableSwipe

```TypeScript
default disableSwipe(disabled: boolean | undefined): this
```

设置是否禁用组件滑动切换功能。未通过该接口设置时，默认不禁用组件滑动切换功能。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default disableSwipe(disabled: boolean | undefined): this--><!--Device-ArcSwiperAttribute-default disableSwipe(disabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disabled | boolean \| undefined | Yes | 是否禁用组件滑动切换功能。设置为true禁用，false不禁用。&lt;br/&gt;取值为undefined时，不禁用组件滑动切换功能。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## disableTransitionAnimation

```TypeScript
default disableTransitionAnimation(disabled: boolean | undefined): this
```

是否关闭特殊动效效果。未通过该接口设置时，默认不关闭特殊动效效果。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default disableTransitionAnimation(disabled: boolean | undefined): this--><!--Device-ArcSwiperAttribute-default disableTransitionAnimation(disabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| disabled | boolean \| undefined | Yes | 是否关闭特殊动效效果。&lt;br/&gt;传入参数非法时，按false处理。&lt;br/&gt;取值为undefined时，不关闭特殊动效效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## duration

```TypeScript
default duration(duration: int | undefined): this
```

设置子组件切换的动画时长。未通过该接口设置时，默认子组件切换的动画时长为400ms。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default duration(duration: int | undefined): this--><!--Device-ArcSwiperAttribute-default duration(duration: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | int \| undefined | Yes | 子组件切换的动画时长。&lt;br/&gt;取值为undefined时，子组件切换的动画时长为400。&lt;br/&gt;单位：毫秒 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## effectMode

```TypeScript
default effectMode(edgeEffect: EdgeEffect | undefined): this
```

设置边缘滑动效果。未通过该接口设置时，边缘滑动效果默认为EdgeEffect.Spring。通过[ArcSwiperController](arkts-arkui-arkui-arcswiper-arcswipercontroller-c.md)的showNext、showPrevious、finishAnimation接口控制翻页时，回弹效果不生效。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default effectMode(edgeEffect: EdgeEffect | undefined): this--><!--Device-ArcSwiperAttribute-default effectMode(edgeEffect: EdgeEffect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| edgeEffect | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | Yes | 边缘滑动效果。通过ArcSwiperController接口控制翻页时，回弹效果不生效。&lt;br/&gt;取值为undefined时，边缘滑动效果为EdgeEffect.Spring。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## index

```TypeScript
default index(index: int | undefined): this
```

设置当前在容器中显示的子组件的索引值。设置小于0或大于等于子组件数量时，按照默认值0处理。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default index(index: int | undefined): this--><!--Device-ArcSwiperAttribute-default index(index: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int \| undefined | Yes | 当前在容器中显示的子组件的索引值。&lt;br/&gt;取值为undefined时，当前在容器中显示的子组件的索引值为0。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## indicator

```TypeScript
default indicator(style: ArcDotIndicator | boolean | undefined): this
```

设置弧形圆点指示器样式。未通过该接口设置时，默认启用弧形圆点指示器样式。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default indicator(style: ArcDotIndicator | boolean | undefined): this--><!--Device-ArcSwiperAttribute-default indicator(style: ArcDotIndicator | boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) \| boolean \| undefined | Yes | ArcDotIndicator：弧形圆点指示器属性及功能。&lt;br/&gt;- boolean：是否启用弧形圆点指示器。 设置为true启用，false不启用。&lt;br/&gt;取值为undefined时，启用弧形圆点指示器样式。&lt;br/&gt;默认类型：ArcDotIndicator |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAnimationEnd

```TypeScript
default onAnimationEnd(handler: AnimationEndHandler | undefined): this
```

切换动画结束时触发该回调。默认无回调。

当ArcSwiper切换动效结束时触发，包括动画过程中手势中断，通过[SwiperController](arkts-arkui-swiper-swipercontroller-c.md)调用finishAnimation。参数为动画结束后的index值，多列ArcSwiper时，index为最左侧组件的索引。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onAnimationEnd(handler: AnimationEndHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onAnimationEnd(handler: AnimationEndHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [AnimationEndHandler](arkts-arkui-animationendhandler-t.md) \| undefined | Yes | 切换动画结束时触发该回调。&lt;br/&gt;取值为undefined时，无回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAnimationStart

```TypeScript
default onAnimationStart(handler: AnimationStartHandler | undefined): this
```

切换动画开始时触发该回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onAnimationStart(handler: AnimationStartHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onAnimationStart(handler: AnimationStartHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [AnimationStartHandler](arkts-arkui-animationstarthandler-t.md) \| undefined | Yes | 切换动画开始时的回调。&lt;br/&gt;取值为undefined时，无回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(handler: IndexChangedHandler | undefined): this
```

当前显示子组件的索引变化时触发该事件，返回值为当前显示子组件的索引值。

ArcSwiper组件结合[LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)使用时，不能在onChange事件里触发子页面UI的刷新。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onChange(handler: IndexChangedHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onChange(handler: IndexChangedHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [IndexChangedHandler](arkts-arkui-indexchangedhandler-t.md) \| undefined | Yes | 当前显示的子组件索引变化时触发该事件。&lt;br/&gt;取值为undefined时，无回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onGestureSwipe

```TypeScript
default onGestureSwipe(handler: GestureSwipeHandler | undefined): this
```

在页面跟手滑动过程中，逐帧触发该回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default onGestureSwipe(handler: GestureSwipeHandler | undefined): this--><!--Device-ArcSwiperAttribute-default onGestureSwipe(handler: GestureSwipeHandler | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [GestureSwipeHandler](arkts-arkui-gestureswipehandler-t.md) \| undefined | Yes | 在页面跟手滑动过程中，逐帧触发该回调。&lt;br/&gt;取值为undefined时，无回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setArcSwiperOptions

```TypeScript
default setArcSwiperOptions(controller?: ArcSwiperController): this
```

设置arcSwiper选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default setArcSwiperOptions(controller?: ArcSwiperController): this--><!--Device-ArcSwiperAttribute-default setArcSwiperOptions(controller?: ArcSwiperController): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [ArcSwiperController](arkts-arkui-arkui-arcswiper-arcswipercontroller-c.md) | No | ArcSwiper构造函数选项 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回ArcSwiperAttribute的实例。 |

## vertical

```TypeScript
default vertical(isVertical: boolean | undefined): this
```

设置是否为纵向滑动。未通过该接口设置时，默认为横向滑动。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcSwiperAttribute-default vertical(isVertical: boolean | undefined): this--><!--Device-ArcSwiperAttribute-default vertical(isVertical: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isVertical | boolean \| undefined | Yes | 是否为纵向滑动。&lt;br/&gt;true表示纵向滑动；false表示横向滑动。&lt;br/&gt;取值为undefined时，进行横向滑动。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

