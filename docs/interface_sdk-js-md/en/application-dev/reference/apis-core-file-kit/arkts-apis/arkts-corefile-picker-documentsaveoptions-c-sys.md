# DocumentSaveOptions

Defines the options for saving documents.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-picker-class DocumentSaveOptions--><!--Device-picker-class DocumentSaveOptions-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from '@kit.CoreFileKit';
```

## themeColor

```TypeScript
themeColor?: CustomColors
```

Theme color parameter. By default, it is left empty and follows the color settings of the **FilePicker**. When it is set to specific theme color properties, such as  
[brand, fontPrimary, compBackgroundEmphasize, and iconFourth](../../apis-arkui/arkts-apis/arkts-arkui-arkui-theme-colors-i.md#Colors), the launched  
**FilePicker** will adapt to the theme color accordingly.This API can be called on smartphones but has no effect on other devices.

**Type:** [CustomColors](../../apis-arkui/arkts-apis/arkts-arkui-customcolors-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DocumentSaveOptions-themeColor?: CustomColors--><!--Device-DocumentSaveOptions-themeColor?: CustomColors-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

