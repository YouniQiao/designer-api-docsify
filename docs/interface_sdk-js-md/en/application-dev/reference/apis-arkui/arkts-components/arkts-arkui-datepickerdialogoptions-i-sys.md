# DatePickerDialogOptions

日期选择器弹窗选项。

继承自[DatePickerOptions](arkts-arkui-datepickeroptions-i.md)。

**Inheritance/Implementation:** DatePickerDialogOptions extends [DatePickerOptions](arkts-arkui-datepickeroptions-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface DatePickerDialogOptions extends DatePickerOptions--><!--Device-unnamed-declare interface DatePickerDialogOptions extends DatePickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## distortionMode

```TypeScript
distortionMode?: DistortionMode
```

设置系统材质下弹窗的非线性动画模式。当需要自定义弹窗的非线性动画效果时传入此参数。

> **默认值：** DistortionMode.DISTORTION_AUTO

> **系统接口：** 此接口为系统接口。

> **说明：** 当取值为 DISTORTION_AUTO 时，需设置[ImmersiveMaterial](ImmersiveMaterial) 类型材质方可生效，
> 并依据设备算力档位自动生效非线性效果（高中档算力设备生效，低档算力设备不生效）。非线性动画会增加渲染开销，建议在低端设备上谨慎使用。
> 各枚举取值含义请参见[DistortionMode](../arkts-apis/arkts-arkui-common-distortionmode-e-sys.md/arkts-arkui-common-distortionmode-e-sys.md)。

**Type:** [DistortionMode](arkts-arkui-distortionmode-e-sys.md)

**Default:** DistortionMode.DISTORTION_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-distortionMode?: DistortionMode--><!--Device-DatePickerDialogOptions-distortionMode?: DistortionMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

设置系统材质下弹窗的流光动画模式。当需要自定义弹窗的流光动画效果时传入此参数。

> **默认值：** EdgeLightMode.EDGELIGHT_AUTO

> **系统接口：** 此接口为系统接口。

> **说明：** 当取值为 EDGELIGHT_AUTO 时，需设置[ImmersiveMaterial](ImmersiveMaterial) 类型材质方可生效，
> 并依据设备算力档位自动生效流光效果（高档算力设备生效，中低档算力设备不生效）。流光动画会增加渲染开销，建议在低端设备上谨慎使用。
> 各枚举取值含义请参见[EdgeLightMode](../arkts-apis/arkts-arkui-common-edgelightmode-e-sys.md/arkts-arkui-common-edgelightmode-e-sys.md)。

**Type:** [EdgeLightMode](arkts-arkui-edgelightmode-e-sys.md)

**Default:** EdgeLightMode.EDGELIGHT_AUTO

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerDialogOptions-edgeLightMode?: EdgeLightMode--><!--Device-DatePickerDialogOptions-edgeLightMode?: EdgeLightMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

