# DocumentSelectOptions

Defines the options for selecting documents.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

<!--Device-picker-class DocumentSelectOptions--><!--Device-picker-class DocumentSelectOptions-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from 'picker';
```

## themeColor

```TypeScript
themeColor?: CustomColors
```

Theme color parameter. By default, it is left empty and follows the color settings of the **FilePicker**. When it is set to specific theme color properties, such as [brand, fontPrimary, compBackgroundEmphasize, and iconFourth](../../apis-arkui/arkts-apis/arkts-arkui-arkui-theme-colors-i.md#Colors), the launched **FilePicker** will adapt to the theme color accordingly. This API can be called on smartphones but has no effect on other devices.

**Type:** [CustomColors](../../apis-arkui/arkts-apis/arkts-arkui-customcolors-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-themeColor?: CustomColors--><!--Device-DocumentSelectOptions-themeColor?: CustomColors-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

