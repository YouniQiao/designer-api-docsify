# DocumentSaveOptions

文档保存选项。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-picker-class DocumentSaveOptions--><!--Device-picker-class DocumentSaveOptions-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## themeColor

```TypeScript
themeColor?: CustomColors
```

主题色参数, 默认为空，跟随FilePicker应用颜色。当themeColor设置为特定的主题色属性（[brand, fontPrimary, compBackgroundEmphasize, iconFourth](../../apis-arkui/arkts-apis/arkts-arkui-arkui-theme-colors-i.md/arkts-arkui-arkui-theme-colors-i.md)）时，被拉起的FilePicker应用将适配传入的主题色参数的效果。

该接口在Phone设备中可正常调用，在其他设备中无效果。

**Type:** [CustomColors](../../apis-arkui/arkts-apis/arkts-arkui-customcolors-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-DocumentSaveOptions-themeColor?: CustomColors--><!--Device-DocumentSaveOptions-themeColor?: CustomColors-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

**System API:** This is a system API.

