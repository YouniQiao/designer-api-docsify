# DocumentSaveOptions

Defines the options for saving documents.

**Since:** 9

<!--Device-picker-class DocumentSaveOptions--><!--Device-picker-class DocumentSaveOptions-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
```

## autoCreateEmptyFile

```TypeScript
autoCreateEmptyFile?: boolean
```

Whether to create empty files, The default value is true, indicating that empty files will be created.

**Type:** boolean

**Default:** true

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSaveOptions-autoCreateEmptyFile?: boolean--><!--Device-DocumentSaveOptions-autoCreateEmptyFile?: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService.FolderSelection

## defaultFilePathUri

```TypeScript
defaultFilePathUri?: string
```

Path of the document or directory to save.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSaveOptions-defaultFilePathUri?: string--><!--Device-DocumentSaveOptions-defaultFilePathUri?: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## fileSuffixChoices

```TypeScript
fileSuffixChoices?: Array<string>
```

Document suffix of the document to save. The value is a string array. Each element specifies an option, which includes at most two parts with a vertical bar (|) in between. The first part is the description, and the second part is the document suffix. If there is no "|", the option does not have the description. By default, all documents are saved.

**Type:** Array&lt;string&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSaveOptions-fileSuffixChoices?: Array<string>--><!--Device-DocumentSaveOptions-fileSuffixChoices?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## newFileNames

```TypeScript
newFileNames?: Array<string>
```

Name of the document to save. If this parameter is not specified, the user needs to enter the the document name.

**Type:** Array&lt;string&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSaveOptions-newFileNames?: Array<string>--><!--Device-DocumentSaveOptions-newFileNames?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## pickerMode

```TypeScript
pickerMode?: DocumentPickerMode
```

Mode for starting Picker. Default value: DEFAULT. If pickerMode is DOWNLOAD, the settings of newFileNames, defaultFilePathUri, and fileSuffixChoices do not take effect.

**Type:** [DocumentPickerMode](arkts-corefile-picker-documentpickermode-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSaveOptions-pickerMode?: DocumentPickerMode--><!--Device-DocumentSaveOptions-pickerMode?: DocumentPickerMode-End-->

**System capability:** SystemCapability.FileManagement.UserFileService
