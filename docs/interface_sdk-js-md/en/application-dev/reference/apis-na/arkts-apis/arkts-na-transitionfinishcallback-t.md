# TransitionFinishCallback

```TypeScript
export type TransitionFinishCallback = (transitionIn: boolean) => void
```

Defines the finish callback type used in transition.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TransitionFinishCallback = (transitionIn: boolean) => void--><!--Device-unnamed-export type TransitionFinishCallback = (transitionIn: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transitionIn | boolean | Yes | a boolean value indicates whether it is the callback of transitionIn or transitionOut.  |

