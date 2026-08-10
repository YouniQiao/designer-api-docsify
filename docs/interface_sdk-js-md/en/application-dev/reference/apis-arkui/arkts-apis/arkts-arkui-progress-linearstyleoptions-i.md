# LinearStyleOptions

线性样式选项。

继承自[ScanEffectOptions](../arkts-components/arkts-arkui-scaneffectoptions-i.md/arkts-arkui-scaneffectoptions-i.md)和[CommonProgressStyleOptions](../arkts-components/arkts-arkui-commonprogressstyleoptions-i.md/arkts-arkui-commonprogressstyleoptions-i.md)。

**Inheritance/Implementation:** LinearStyleOptions extends [ScanEffectOptions](../arkts-components/arkts-arkui-scaneffectoptions-i.md/arkts-arkui-scaneffectoptions-i.md), [CommonProgressStyleOptions](../arkts-components/arkts-arkui-commonprogressstyleoptions-i.md/arkts-arkui-commonprogressstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface LinearStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions--><!--Device-unnamed-export declare interface LinearStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeRadius

```TypeScript
strokeRadius?: PX | VP | LPX | Resource
```

设置线性进度条的圆角半径。取值范围[0, strokeWidth / 2]。默认值：strokeWidth / 2。

**Type:** [PX](arkts-arkui-px-t.md) \| VP \| LPX \| Resource

**Default:** strokeWidth / 2

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LinearStyleOptions-strokeRadius?: PX | VP | LPX | Resource--><!--Device-LinearStyleOptions-strokeRadius?: PX | VP | LPX | Resource-End-->

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

<!--Device-LinearStyleOptions-strokeWidth?: Length--><!--Device-LinearStyleOptions-strokeWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

