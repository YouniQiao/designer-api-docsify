# TransitionFinishCallback

```TypeScript
export type TransitionFinishCallback = (transitionIn: boolean) => void
```

组件转场动画的结束回调类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TransitionFinishCallback = (transitionIn: boolean) => void--><!--Device-unnamed-export type TransitionFinishCallback = (transitionIn: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transitionIn | boolean | Yes | 该入参表示转场动画的结束回调类型。<br/>该参数为true表示该转场回调是出现动画的结束回调，该参数为false表示该转场回调是消失动画的结束回调。 |

