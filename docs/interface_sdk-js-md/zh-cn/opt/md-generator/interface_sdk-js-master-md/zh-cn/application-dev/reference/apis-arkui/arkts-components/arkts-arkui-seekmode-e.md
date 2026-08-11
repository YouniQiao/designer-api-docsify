# SeekMode

视频跳转模式选项。

| 名称 |值| 说明 |
| ---------------- |--| ---------------------------- |
| [PreviousKeyframe](#previouskeyframe) |0| 跳转到当前播放位置之前最近的关键帧。 |
| [NextKeyframe](#nextkeyframe) |1| 跳转到当前播放位置之后最近的关键帧。 |
| [ClosestKeyframe](#closestkeyframe) |2| 跳转到距离当前播放位置最近的关键帧。 |
| [Accurate](#accurate) |3|

**起始版本：** 8

<!--Device-unnamed-declare enum SeekMode--><!--Device-unnamed-declare enum SeekMode-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## PreviousKeyframe

```TypeScript
PreviousKeyframe
```

Seek to the nearest previous keyframe.

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SeekMode-PreviousKeyframe--><!--Device-SeekMode-PreviousKeyframe-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## NextKeyframe

```TypeScript
NextKeyframe
```

Seek to the nearest next keyframe.

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SeekMode-NextKeyframe--><!--Device-SeekMode-NextKeyframe-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## ClosestKeyframe

```TypeScript
ClosestKeyframe
```

Seek to the nearest keyframe.

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SeekMode-ClosestKeyframe--><!--Device-SeekMode-ClosestKeyframe-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## Accurate

```TypeScript
Accurate
```

Seek to a specific frame, regardless of whether the frame is a keyframe.

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SeekMode-Accurate--><!--Device-SeekMode-Accurate-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
