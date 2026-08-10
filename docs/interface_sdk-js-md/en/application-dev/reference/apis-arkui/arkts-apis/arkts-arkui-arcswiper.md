# @ohos.arkui.ArcSwiper

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from 'kits/@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ArcDotIndicator](arkts-arkui-arkui-arcswiper-arcdotindicator-c.md) | 提供弧形圆点指示器属性及功能。 |
| [ArcSwiperController](arkts-arkui-arkui-arcswiper-arcswipercontroller-c.md) | ArcSwiper容器组件的控制器，可以将此对象绑定至ArcSwiper组件，实现控制ArcSwiper翻页等功能。 |

### Interfaces

| Name | Description |
| --- | --- |
| [ArcSwiperAttribute](arkts-arkui-arkui-arcswiper-arcswiperattribute-i.md) | 除支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)外，还支持以下属性，不支持[Menu控制](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)。 |
| [ArcSwiperContentAnimatedTransition](arkts-arkui-arkui-arcswiper-arcswipercontentanimatedtransition-i.md) | ArcSwiper自定义切换动画相关信息。 |
| [ArcSwiperContentTransitionProxy](arkts-arkui-arkui-arcswiper-arcswipercontenttransitionproxy-i.md) | ArcSwiper自定义切换动画执行过程中，返回给开发者的proxy对象。开发者可通过该对象获取自定义动画视窗内的页面信息，同时，也可以通过调用该对象的finishTransition接口通知ArcSwiper组件页面自定义动画已结束。 |

### Enums

| Name | Description |
| --- | --- |
| [ArcDirection](arkts-arkui-arkui-arcswiper-arcdirection-e.md) | 弧形方向。 |

### Types

| Name | Description |
| --- | --- |
| [AnimationEndHandler](arkts-arkui-animationendhandler-t.md) | 切换动画结束时的回调。 |
| [AnimationStartHandler](arkts-arkui-animationstarthandler-t.md) | 切换动画开始时的回调。 |
| [FinishAnimationHandler](arkts-arkui-finishanimationhandler-t.md) | 停止播放动画时，告知应用。 |
| [GestureSwipeHandler](arkts-arkui-gestureswipehandler-t.md) | 在页面跟手滑动过程中，逐帧触发的回调。 |
| [IndexChangedHandler](arkts-arkui-indexchangedhandler-t.md) | 当前显示元素的索引变化时，告知应用。 |

