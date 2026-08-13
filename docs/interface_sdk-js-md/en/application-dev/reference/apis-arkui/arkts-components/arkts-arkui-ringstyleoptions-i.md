# RingStyleOptions

Options of the ring style without scales. Inherits from [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md#ScanEffectOptions) and [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md#CommonProgressStyleOptions).

**Inheritance/Implementation:** RingStyleOptions extends [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md#ScanEffectOptions), [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md#CommonProgressStyleOptions)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare interface RingStyleOptions--><!--Device-unnamed-declare interface RingStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: boolean
```

Whether to enable the shadow effect. **true**: The shadow effect is enabled. **false**: The shadow effect is disabled. Default value: **false**

**Type:** boolean

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RingStyleOptions-shadow?: boolean--><!--Device-RingStyleOptions-shadow?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## status

```TypeScript
status?: ProgressStatus
```

Progress state. When this parameter is set to **ProgressStatus.LOADING**, the update check animation is enabled, and the progress value setting does not take effect. When the value changes from **ProgressStatus.LOADING** to **ProgressStatus.PROGRESSING**, the update check animation runs to completion and then stops. Default value: **ProgressStatus.PROGRESSING**

**Type:** [ProgressStatus](arkts-arkui-progressstatus-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RingStyleOptions-status?: ProgressStatus--><!--Device-RingStyleOptions-status?: ProgressStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Length
```

Stroke width of the progress indicator. Percentage values are not supported. Default value: **4.0vp**

**Type:** Length

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RingStyleOptions-strokeWidth?: Length--><!--Device-RingStyleOptions-strokeWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

