# @ohos.arkui.colorPickerController

The **colorPickerController** module provides global color picking capability. After an application calls [pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md) to start the color picking process, a color ring appears on the screen at the specified initial position. The ring follows the user's finger or stylus movement. When the user lifts the finger or stylus, the color of the last pointing position is returned.

This API supports both SDR and HDR color formats. The returned [brightness](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md#brightness) is available when the picked pixel is HDR content.

> **NOTE:** 
> - Only touchscreen/stylus devices are supported.

## Modules to Import

```TypeScript
import { colorPickerController, PickedColorInfo } from '@kit.ArkUI';
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [colorPickerController](arkts-arkui-colorpickercontroller-n.md) | The **colorPickerController** module provides global color picking capability. After an application calls [pickForResult](arkts-arkui-colorpickercontroller-pickforresult-f.md) to start the color picking process, a color ring appears on the screen at the specified initial position. The ring follows the user's finger or stylus movement. When the user lifts the finger or stylus, the color of the last pointing position is returned. |

### Interfaces

| Name | Description |
| --- | --- |
| [PickedColorInfo](arkts-arkui-arkui-colorpickercontroller-pickedcolorinfo-i.md) | Global color picking result object, containing the basic information of the picked color. |
