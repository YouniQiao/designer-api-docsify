# @ohos.file.picker

The **Picker** module encapsulates APIs such as **DocumentViewPicker**, **AudioViewPicker**, and **PhotoViewPicker** to provide capabilities of selecting and saving files of different types. An application can select the API as required. The APIs of this module must be called in UIAbility. Otherwise, the **FilePicker**, **AudioPicker**, or **PhotoPicker** cannot be started. Chinese characters and non-digit characters in the URI are compiled into the corresponding ASCII code and concatenated to the URI returned by calling these APIs.

**Since:** 9

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Classes(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c-sys.md) |
| [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DocumentPickerMode](arkts-corefile-picker-documentpickermode-e.md) |
| [DocumentSelectMode](arkts-corefile-picker-documentselectmode-e.md) |
| [MergeTypeMode](arkts-corefile-picker-mergetypemode-e.md) |
| [PhotoViewMIMETypes](arkts-corefile-picker-photoviewmimetypes-e.md) |
