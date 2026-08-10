# BreakPoints

设置栅格容器组件的断点。更多断点的说明参考[栅格容器断点](../../../ui/arkts-layout-development-grid-layout.md#栅格容器断点)。

&lt;!--code_no_check--&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare interface BreakPoints--><!--Device-unnamed-declare interface BreakPoints-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reference

```TypeScript
reference?: BreakpointsReference
```

断点切换参照物。支持WindowSize（以窗口为参照）和ComponentSize（以容器为参照）。

默认值：BreakpointsReference.WindowSize 

非法值：按默认值处理。

**Type:** [BreakpointsReference](../arkts-apis/arkts-arkui-gridrow-breakpointsreference-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BreakPoints-reference?: BreakpointsReference--><!--Device-BreakPoints-reference?: BreakpointsReference-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: Array<string>
```

设置断点位置的单调递增数组，字符串格式为"数字+vp"，例如"320vp"、"600vp"等。

默认值：["320vp", "600vp", "840vp"] 

非法值：按默认值处理。

单位：vp

默认断点适用于大多数场景，可根据特殊屏幕尺寸或特定布局需求自定义。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BreakPoints-value?: Array<string>--><!--Device-BreakPoints-value?: Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

