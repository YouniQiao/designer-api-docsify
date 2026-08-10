# RingStyleOptions

环形无刻度样式选项。

继承自[ScanEffectOptions](../arkts-components/arkts-arkui-scaneffectoptions-i.md/arkts-arkui-scaneffectoptions-i.md)和[CommonProgressStyleOptions](../arkts-components/arkts-arkui-commonprogressstyleoptions-i.md/arkts-arkui-commonprogressstyleoptions-i.md)。

**Inheritance/Implementation:** RingStyleOptions extends [ScanEffectOptions](../arkts-components/arkts-arkui-scaneffectoptions-i.md/arkts-arkui-scaneffectoptions-i.md), [CommonProgressStyleOptions](../arkts-components/arkts-arkui-commonprogressstyleoptions-i.md/arkts-arkui-commonprogressstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RingStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions--><!--Device-unnamed-export declare interface RingStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: boolean
```

进度条阴影开关。true：表示打开进度条阴影；false：表示关闭进度条阴影。默认值：false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RingStyleOptions-shadow?: boolean--><!--Device-RingStyleOptions-shadow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status?: ProgressStatus
```

设置进度条状态。当设置为ProgressStatus.LOADING时会开启检查更新动效，此时设置进度值不生效。当从ProgressStatus.LOADING设置为ProgressStatus.PROGRESSING时，检查更新动效会执行到终点再停止。默认值：ProgressStatus.PROGRESSING。

**Type:** [ProgressStatus](../arkts-components/arkts-arkui-progressstatus-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RingStyleOptions-status?: ProgressStatus--><!--Device-RingStyleOptions-status?: ProgressStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Length
```

设置进度条宽度（不支持百分比设置）。默认值：4vp。

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RingStyleOptions-strokeWidth?: Length--><!--Device-RingStyleOptions-strokeWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

