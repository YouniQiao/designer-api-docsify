# @ohos.file.picker

选择器(Picker)是一个封装DocumentViewPicker、AudioViewPicker、PhotoViewPicker的API模块，具有选择与保存的能力。 应用可以选择使用以下API来实现文件的选择和保存的功能。该类接口，需要应用在界面UIAbility中调用，否则无法拉起FilePicker应用、 AudioPicker应用或PhotoPicker应用。调用本模块接口返回的URI数组， URI中的中文及非数字字母的特殊字符会被编码为对应的ASCII码并拼接到URI中。 > **说明：** > > 该模块接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace picker--><!--Device-unnamed-declare namespace picker-End-->

**系统能力：** SystemCapability.FileManagement.UserFileService

## 汇总

### 类

| 名称 |
| --- |
| [AudioSaveOptions](arkts-corefile-picker-audiosaveoptions-c.md) |
| [AudioSelectOptions](arkts-corefile-picker-audioselectoptions-c.md) |
| [AudioViewPicker](arkts-corefile-picker-audioviewpicker-c.md) |
| [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c.md) |
| [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c.md) |
| [DocumentViewPicker](arkts-corefile-picker-documentviewpicker-c.md) |
| [PhotoSaveOptions](arkts-corefile-picker-photosaveoptions-c.md) |
| [PhotoSelectOptions](arkts-corefile-picker-photoselectoptions-c.md) |
| [PhotoSelectResult](arkts-corefile-picker-photoselectresult-c.md) |
| [PhotoViewPicker](arkts-corefile-picker-photoviewpicker-c.md) |

<!--Del-->
### 类（系统接口）

| 名称 |
| --- |
| [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c-sys.md) |
| [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [AudioSaveOptions](arkts-corefile-picker-audiosaveoptions-i.md) |
| [AudioSelectOptions](arkts-corefile-picker-audioselectoptions-i.md) |
| [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-i.md) |
| [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [DocumentPickerMode](arkts-corefile-picker-documentpickermode-e.md) |
| [DocumentSelectMode](arkts-corefile-picker-documentselectmode-e.md) |
| [MergeTypeMode](arkts-corefile-picker-mergetypemode-e.md) |
| [PhotoViewMIMETypes](arkts-corefile-picker-photoviewmimetypes-e.md) |
