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

## autoCreateEmptyFile

```TypeScript
autoCreateEmptyFile?: boolean
```

保存文件时，由应用决定是否预置空文件。默认为true，Picker会预置空文件并且返回文件的URI数组。false不预置空文件，只会返回文件的URI数组。

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSaveOptions-autoCreateEmptyFile?: boolean--><!--Device-DocumentSaveOptions-autoCreateEmptyFile?: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService.FolderSelection

## defaultFilePathUri

```TypeScript
defaultFilePathUri?: string
```

指定选择的文件或者目录的URI。默认为空（效果为拉起最近打开页）。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DocumentSaveOptions-defaultFilePathUri?: string--><!--Device-DocumentSaveOptions-defaultFilePathUri?: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## fileSuffixChoices

```TypeScript
fileSuffixChoices?: Array<string>
```

保存文件的后缀类型。传入字符串数组，每一项代表一个后缀选项，每一项内部用"|"分为两部分，第一部分为描述，第二部分为要保存的后缀。没有"|"则没有描述，该项整体是一个保存的后缀。默认没有后缀类型。

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DocumentSaveOptions-fileSuffixChoices?: Array<string>--><!--Device-DocumentSaveOptions-fileSuffixChoices?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## newFileNames

```TypeScript
newFileNames?: Array<string>
```

拉起documentPicker进行保存的文件名。若无此参数，则默认需要用户自行输入。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DocumentSaveOptions-newFileNames?: Array<string>--><!--Device-DocumentSaveOptions-newFileNames?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## pickerMode

```TypeScript
pickerMode?: DocumentPickerMode
```

拉起picker的类型, 默认为DEFAULT。当pickerMode设置为DOWNLOAD时，用户配置的参数newFileNames、defaultFilePathUri和fileSuffixChoices将不会生效。

**Type:** [DocumentPickerMode](arkts-corefile-picker-documentpickermode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DocumentSaveOptions-pickerMode?: DocumentPickerMode--><!--Device-DocumentSaveOptions-pickerMode?: DocumentPickerMode-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

