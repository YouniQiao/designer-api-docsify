# RingStyleOptions

Defines the ring style Options.

**Inheritance/Implementation:** RingStyleOptions extends [ScanEffectOptions](../arkts-components/arkts-arkui-scaneffectoptions-i.md/arkts-arkui-scaneffectoptions-i.md), [CommonProgressStyleOptions](../arkts-components/arkts-arkui-commonprogressstyleoptions-i.md/arkts-arkui-commonprogressstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RingStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions--><!--Device-unnamed-export declare interface RingStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: boolean
```

Enables progress shadow.Default value: false.

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

The status of progress, default is PROGRESSING. Set to LOADING status will trigger the loading animation.Default value: ProgressStatus.PROGRESSING.

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

Defines the strokeWidth property.Default value: 4vp.

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RingStyleOptions-strokeWidth?: Length--><!--Device-RingStyleOptions-strokeWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

