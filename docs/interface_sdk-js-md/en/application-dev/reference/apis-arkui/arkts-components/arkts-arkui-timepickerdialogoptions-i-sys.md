# TimePickerDialogOptions

时间选择器弹窗选项。

继承自[TimePickerOptions](arkts-arkui-timepickeroptions-i.md)。

**Inheritance/Implementation:** TimePickerDialogOptions extends [TimePickerOptions](arkts-arkui-timepickeroptions-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface TimePickerDialogOptions extends TimePickerOptions--><!--Device-unnamed-declare interface TimePickerDialogOptions extends TimePickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distortionMode

```TypeScript
distortionMode?: DistortionMode
```

设置系统材质下弹窗的非线性动画模式。

> **默认值：** DistortionMode.DISTORTION_AUTO

> **系统接口：** 此接口为系统接口。

> **说明：** 当取值为 DISTORTION_AUTO 时，需设置
> [ImmersiveMaterial](ImmersiveMaterial) 类型材质方可生效，并依据设备算力档位自动生效非线性效果（高中档算力设备生效，
> 低档算力设备不生效）。非线性动画会增加渲染开销，建议在低端设备上谨慎使用。
> 各枚举取值含义请参见[DistortionMode](../arkts-apis/arkts-arkui-common-distortionmode-e-sys.md/arkts-arkui-common-distortionmode-e-sys.md)。

**Type:** [DistortionMode](arkts-arkui-distortionmode-e-sys.md)

**Default:** DistortionMode.DISTORTION_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-distortionMode?: DistortionMode--><!--Device-TimePickerDialogOptions-distortionMode?: DistortionMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

设置系统材质下弹窗的流光动画模式。

> **默认值：** EdgeLightMode.EDGELIGHT_AUTO

> **系统接口：** 此接口为系统接口。

> **说明：** 当取值为 EDGELIGHT_AUTO 时，需设置
> [ImmersiveMaterial](ImmersiveMaterial) 类型材质方可生效，并依据设备算力档位自动生效流光效果（高档算力设备生效，
> 中低档算力设备不生效）。流光动画会增加渲染开销，建议在低端设备上谨慎使用。各枚举取值含义请参见[EdgeLightMode](../arkts-apis/arkts-arkui-common-edgelightmode-e-sys.md/arkts-arkui-common-edgelightmode-e-sys.md)。

**Type:** [EdgeLightMode](arkts-arkui-edgelightmode-e-sys.md)

**Default:** EdgeLightMode.EDGELIGHT_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerDialogOptions-edgeLightMode?: EdgeLightMode--><!--Device-TimePickerDialogOptions-edgeLightMode?: EdgeLightMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

