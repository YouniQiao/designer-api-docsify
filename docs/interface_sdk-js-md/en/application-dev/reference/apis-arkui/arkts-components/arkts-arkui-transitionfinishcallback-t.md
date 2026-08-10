# TransitionFinishCallback

```TypeScript
declare type TransitionFinishCallback = (transitionIn: boolean) => void
```

组件转场动画的结束回调类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-unnamed-declare type TransitionFinishCallback = (transitionIn: boolean) => void--><!--Device-unnamed-declare type TransitionFinishCallback = (transitionIn: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transitionIn | boolean | Yes | 该入参表示转场动画的结束回调类型。<br/>该参数为true表示该转场回调是出现动画的结束回调，该参数为false表示该转场回调是消失动画的结束回调。 |

