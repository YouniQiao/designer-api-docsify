# SeekMode

视频跳转模式选项。

| 名称 |值| 说明 |  
| ---------------- |--| ---------------------------- |  
| PreviousKeyframe |0| 跳转到当前播放位置之前最近的关键帧。 |  
| NextKeyframe |1| 跳转到当前播放位置之后最近的关键帧。 |  
| ClosestKeyframe |2| 跳转到距离当前播放位置最近的关键帧。 |  
| Accurate |3| 精准跳转到指定时间点，不论是否为关键帧。精度高但可能需要解码更多帧。 |

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare enum SeekMode--><!--Device-unnamed-declare enum SeekMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PreviousKeyframe

```TypeScript
PreviousKeyframe
```

Seek to the nearest previous keyframe.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SeekMode-PreviousKeyframe--><!--Device-SeekMode-PreviousKeyframe-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NextKeyframe

```TypeScript
NextKeyframe
```

Seek to the nearest next keyframe.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SeekMode-NextKeyframe--><!--Device-SeekMode-NextKeyframe-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ClosestKeyframe

```TypeScript
ClosestKeyframe
```

Seek to the nearest keyframe.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SeekMode-ClosestKeyframe--><!--Device-SeekMode-ClosestKeyframe-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Accurate

```TypeScript
Accurate
```

Seek to a specific frame, regardless of whether the frame is a keyframe.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SeekMode-Accurate--><!--Device-SeekMode-Accurate-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

