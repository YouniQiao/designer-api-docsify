# SheetOptions

Component sheet options

**Inheritance/Implementation:** SheetOptions extends [BindOptions](common-bindoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SheetOptions extends BindOptions--><!--Device-unnamed-export declare interface SheetOptions extends BindOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## blurSnapshot

```TypeScript
blurSnapshot?: BlurSnapshotOptions
```

Options for blur snapshot optimization of the sheet.When this property is set, blur optimization is enabled and the sheet background will be rendered using a blur snapshot.This property cannot be dynamically switched after the sheet is presented.

**Type:** BlurSnapshotOptions

**Default:** undefined

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-blurSnapshot?: BlurSnapshotOptions--><!--Device-SheetOptions-blurSnapshot?: BlurSnapshotOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## edgeLightMode

```TypeScript
edgeLightMode?: EdgeLightMode
```

Sets the edgeLight animation Mode of the bindSheet.

**Type:** EdgeLightMode

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

Sets the position offset of the bindSheet.

**Type:** Position

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SheetOptions-offset?: Position--><!--Device-SheetOptions-offset?: Position-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

