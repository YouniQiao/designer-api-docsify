# SwiperContentWillScrollResult

The result of swiper ContentWillScrollCallback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SwiperContentWillScrollResult--><!--Device-unnamed-export declare interface SwiperContentWillScrollResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## comingIndex

```TypeScript
comingIndex: int
```

the index value of the child page that will display. The value range is all integers.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperContentWillScrollResult-comingIndex: int--><!--Device-SwiperContentWillScrollResult-comingIndex: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## currentIndex

```TypeScript
currentIndex: int
```

the index value of the current child page. The value range is all integers.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperContentWillScrollResult-currentIndex: int--><!--Device-SwiperContentWillScrollResult-currentIndex: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset: double
```

the sliding offset of each frame. Positive numbers indicating slide backward(e.g. from index=1 to index=0), negative numbers indicating slide forward(e.g. from index=0 to index=1).

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperContentWillScrollResult-offset: double--><!--Device-SwiperContentWillScrollResult-offset: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

