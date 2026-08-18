# DocumentSelectOptions

Defines the options for selecting documents.

**Since:** 9

<!--Device-picker-class DocumentSelectOptions--><!--Device-picker-class DocumentSelectOptions-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from '@kit.CoreFileKit';
```

## allowsMulFolderSelection

```TypeScript
allowsMulFolderSelection?: boolean
```

Whether to support for selecting folders, Only 2-in-1 devices are supported. The value false (default) means not support folder selection;

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-allowsMulFolderSelection?: boolean--><!--Device-DocumentSelectOptions-allowsMulFolderSelection?: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService.FolderSelection

## authMode

```TypeScript
authMode?: boolean
```

Whether to start Picker. Default value: false. If authMode is true, defaultFilePathUri is mandatory, which specifies the URI of the file allowed to access.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-authMode?: boolean--><!--Device-DocumentSelectOptions-authMode?: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService.FolderSelection

## defaultFilePathUri

```TypeScript
defaultFilePathUri?: string
```

Path of the document or directory to select. It is empty by default (the recently opened page is displayed).

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-defaultFilePathUri?: string--><!--Device-DocumentSelectOptions-defaultFilePathUri?: string-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## fileSuffixFilters

```TypeScript
fileSuffixFilters?: Array<string>
```

Document suffix of the document to select. The value is a string array. Each element specifies an option, which includes at most two parts with a vertical bar (|) in between. The first part is the description, and the second part is the document suffix. If there is no "|", the option does not have the description. Multiple document suffixes separated by a comma (,) are allowed in an option. The number of elements in a string array cannot exceed 100. This parameter is available only to the devices that have the required system capability. By default, no filtering is performed, that is, all documents are selected.

**Type:** Array&lt;string&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-fileSuffixFilters?: Array<string>--><!--Device-DocumentSelectOptions-fileSuffixFilters?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## isEncryptionSupported

```TypeScript
isEncryptionSupported?: boolean
```

Whether to support encryption (only files are supported). The default value is false. If this parameter is set to true, the picker will display a button that allows the user, files can be encrypted on the Picker page.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-isEncryptionSupported?: boolean--><!--Device-DocumentSelectOptions-isEncryptionSupported?: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## maxSelectNumber

```TypeScript
maxSelectNumber?: int
```

Maximum number of documents that can be selected. Value range: 1 to 500. Only the devices with the required system capability can select directories, and only one directory can be selected at a time. Default value: 1.

**Type:** int

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-maxSelectNumber?: int--><!--Device-DocumentSelectOptions-maxSelectNumber?: int-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## mergeMode

```TypeScript
mergeMode?: MergeTypeMode
```

Whether to enable the aggregation view mode for a file management application. The default value is DEFAULT, indicating that this parameter does not take effect and the aggregation view is disabled. If this parameter is set to a value other than DEFAULT, other parameters do not take effect. Only mobile phones are supported.

**Type:** [MergeTypeMode](arkts-corefile-picker-mergetypemode-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-mergeMode?: MergeTypeMode--><!--Device-DocumentSelectOptions-mergeMode?: MergeTypeMode-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## multiAuthMode

```TypeScript
multiAuthMode?: boolean
```

Whether to enable the batch authorization mode. The value false (default) means to disable the batch authorization mode; the value true means to enable the batch authorization mode. The multiUriArray parameter only takes effect when multAuthMode is set to true. Only mobile phones are supported.

**Type:** boolean

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-multiAuthMode?: boolean--><!--Device-DocumentSelectOptions-multiAuthMode?: boolean-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## multiUriArray

```TypeScript
multiUriArray?: Array<string>
```

Whether to pass the URIs for batch authorization (only files are supported). This parameter is used with multAuthMode, and does not take effect when multAuthMode is set to false. By default, this parameter is left empty.(The files displayed on the batch authorization page are empty.) Only mobile phones are supported.

**Type:** Array&lt;string&gt;

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-multiUriArray?: Array<string>--><!--Device-DocumentSelectOptions-multiUriArray?: Array<string>-End-->

**System capability:** SystemCapability.FileManagement.UserFileService

## selectMode

```TypeScript
selectMode?: DocumentSelectMode
```

Selection mode. Only 2-in-1 devices are supported. The default value is FILE.

**Type:** [DocumentSelectMode](arkts-corefile-picker-documentselectmode-e.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DocumentSelectOptions-selectMode?: DocumentSelectMode--><!--Device-DocumentSelectOptions-selectMode?: DocumentSelectMode-End-->

**System capability:** SystemCapability.FileManagement.UserFileService.FolderSelection

