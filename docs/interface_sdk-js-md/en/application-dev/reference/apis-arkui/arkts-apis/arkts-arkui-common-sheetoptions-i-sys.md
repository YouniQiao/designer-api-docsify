# SheetOptions

Component sheet options@extends BindOptions

**Inheritance/Implementation:** SheetOptions extends [BindOptions](arkts-arkui-common-bindoptions-i.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurSnapshot

```TypeScript
blurSnapshot?: BlurSnapshotOptions
```

Options for blur snapshot optimization of the sheet. When this property is set, blur optimization is enabled and the sheet background will be rendered using a blur snapshot. This property cannot be dynamically switched after the sheet is presented.

**Type:** [BlurSnapshotOptions](arkts-arkui-common-blursnapshotoptions-i-sys.md)

**Default:** undefined

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

Sets the edgeLight animation Mode of the bindSheet.

**Type:** [EdgeLightMode](arkts-arkui-common-edgelightmode-e-sys.md)

**Default:** EdgeLightMode.EDGELIGHT_DISABLED

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## offset

```TypeScript
offset?: Position
```

Sets the position offset of the bindSheet.

**Type:** [Position](arkts-arkui-position-i.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.
