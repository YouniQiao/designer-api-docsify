# colorPickerController

```TypeScript
declare namespace colorPickerController
```

The **colorPickerController** module provides global color picking capability. After an application calls [pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md) to start the color picking process, a color ring appears on the screen at the specified initial position. The ring follows the user's finger or stylus movement. When the user lifts the finger or stylus, the color of the last pointing position is returned.

This API supports both SDR and HDR color formats. The returned [brightness](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md#brightness) is available when the picked pixel is HDR content.

> **NOTE:** 
> - Only touchscreen/stylus devices are supported.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace colorPickerController--><!--Device-unnamed-declare namespace colorPickerController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md#pickforresult-1) | Picks color globally, supporting both SDR and HDR formats. A color ring appears on the screen at the specified initial position and follows the user's finger or stylus movement. When the user lifts the finger or stylus, the color of the last pointing position is returned. Uses Promise for asynchronous callback. |
