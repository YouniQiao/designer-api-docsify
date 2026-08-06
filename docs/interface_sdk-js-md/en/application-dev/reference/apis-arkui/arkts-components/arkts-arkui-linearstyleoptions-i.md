# LinearStyleOptions

Linear style options.

Inherits from [ScanEffectOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ and  
[CommonProgressStyleOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Inheritance/Implementation:** LinearStyleOptions extends [ScanEffectOptions](../arkts-apis/arkts-arkui-component/progress-scaneffectoptions-i.md), [CommonProgressStyleOptions](../arkts-apis/arkts-arkui-component/progress-commonprogressstyleoptions-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface LinearStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions--><!--Device-unnamed-declare interface LinearStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeRadius

```TypeScript
strokeRadius?: PX | VP | LPX | Resource
```

Border radius of the linear progress indicator.

Value range: [0, strokeWidth/2] Default value: **strokeWidth/2

**Type:** PX \| VP \| LPX \| Resource

**Default:** strokeWidth / 2

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LinearStyleOptions-strokeRadius?: PX | VP | LPX | Resource--><!--Device-LinearStyleOptions-strokeRadius?: PX | VP | LPX | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Length
```

Stroke width of the progress indicator. Percentage values are not supported.

Default value: **4.0vp

**Type:** Length

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LinearStyleOptions-strokeWidth?: Length--><!--Device-LinearStyleOptions-strokeWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

