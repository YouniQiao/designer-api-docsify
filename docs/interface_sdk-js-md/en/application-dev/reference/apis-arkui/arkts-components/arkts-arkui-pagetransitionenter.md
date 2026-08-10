# PageTransitionEnter

Defines PageTransitionEnter Component.

## PageTransitionEnter

```TypeScript
PageTransitionEnter(value: PageTransitionOptions)
```

设置当前页面的自定义入场动效。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PageTransitionEnterInterface-(value: PageTransitionOptions): PageTransitionEnterInterface--><!--Device-PageTransitionEnterInterface-(value: PageTransitionOptions): PageTransitionEnterInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PageTransitionOptions](../arkts-apis/arkts-arkui-pagetransition-pagetransitionoptions-i.md) | Yes | 配置入场动效的参数。 |

## PageTransitionEnter

```TypeScript
PageTransitionEnter(event: PageTransitionCallback)
```

逐帧回调，直到入场动画结束，progress从0变化到1。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PageTransitionEnterInterface-onEnter(event: PageTransitionCallback): PageTransitionEnterInterface--><!--Device-PageTransitionEnterInterface-onEnter(event: PageTransitionCallback): PageTransitionEnterInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PageTransitionCallback](../arkts-apis/arkts-arkui-pagetransitioncallback-t.md) | Yes | 入场动画的逐帧回调直到入场动画结束，progress从0变化到1。 |

## Summary

- [PageTransitionExitInterface](arkts-arkui-pagetransitionenter-pagetransitionexitinterface-i.md)
- [PageTransitionOptions](arkts-arkui-pagetransitionenter-pagetransitionoptions-i.md)
- [PageTransitionCallback](arkts-arkui-pagetransitionenter-pagetransitioncallback-t.md)
- [RouteType](arkts-arkui-pagetransitionenter-routetype-e.md)
- [SlideEffect](arkts-arkui-pagetransitionenter-slideeffect-e.md)
