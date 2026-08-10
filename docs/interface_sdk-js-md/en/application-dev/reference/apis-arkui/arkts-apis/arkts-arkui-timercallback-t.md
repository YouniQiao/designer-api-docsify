# TimerCallback

```TypeScript
export type TimerCallback = (utc: long, elapsedTime: long) => void
```

时间文本发生变化时触发该事件。锁屏状态和应用后台状态下不会触发该事件。设置高精度的format（SSS、SS）时，回调间隔可能会出现波动。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TimerCallback = (utc: long, elapsedTime: long) => void--><!--Device-unnamed-export type TimerCallback = (utc: long, elapsedTime: long) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| utc | long | Yes |  |
| elapsedTime | long | Yes |  |

