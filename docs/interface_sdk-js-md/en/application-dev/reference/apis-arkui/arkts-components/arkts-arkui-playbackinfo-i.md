# PlaybackInfo

用于描述当前视频播放的进度。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface PlaybackInfo--><!--Device-unnamed-interface PlaybackInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## time

```TypeScript
time: number
```

当前视频播放的进度。

单位：s

取值范围：[0,+∞)

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PlaybackInfo-time: number--><!--Device-PlaybackInfo-time: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

