# ArcSliderEnlargeHandler

```TypeScript
export declare type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void
```

弧形Slider放大或缩小时，告知应用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void--><!--Device-unnamed-export declare type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnlarged | boolean | Yes | ArcSlider当前是否放大。<br/>isEnlarged为false时，ArcSlider组件处于缩小状态。<br/>isEnlarged为true时， ArcSlider组件处于放大状态。 |

