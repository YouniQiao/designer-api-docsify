# SheetOptions

继承自[BindOptions](../arkts-components/arkts-arkui-bindoptions-i.md/arkts-arkui-bindoptions-i.md)。

半模态页面内容选项。

**Inheritance/Implementation:** SheetOptions extends [BindOptions](../arkts-components/arkts-arkui-bindoptions-i.md/arkts-arkui-bindoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SheetOptions extends BindOptions--><!--Device-unnamed-export declare interface SheetOptions extends BindOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

设置半模态弹窗边缘光效动画模式。

默认值：EdgeLightMode.EDGELIGHT_DISABLED

**系统接口：** 此接口为系统接口。

**Type:** [EdgeLightMode](../arkts-components/arkts-arkui-edgelightmode-e-sys.md)

**Default:** EdgeLightMode.EDGELIGHT_DISABLED

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-edgeLightMode?: EdgeLightMode--><!--Device-SheetOptions-edgeLightMode?: EdgeLightMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## offset

```TypeScript
offset?: Position
```

设置半模态弹窗偏移量。当半模态为底部弹窗时，支持设置底部间距。不支持设置半模态的[SheetOptions](../arkts-components/arkts-arkui-sheetoptions-i.md/arkts-arkui-sheetoptions-i.md)中的detents属性。y轴设置为负数的时候不生效。

默认值：x轴为0vp，y轴坐标为0vp。

**系统接口：** 此接口为系统接口。

**Type:** [Position](arkts-arkui-position-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-offset?: Position--><!--Device-SheetOptions-offset?: Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

