# ListFileExtOptions

Defines the options used in **listFileExt**.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface ListFileExtOptions--><!--Device-unnamed-export interface ListFileExtOptions-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## fileFilter

```TypeScript
fileFilter?: FileFilter
```

File name filtering rule. The default value is empty, indicating that no filtering is performed.

**Type:** [FileFilter](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-filefilter-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFileExtOptions-fileFilter?: FileFilter--><!--Device-ListFileExtOptions-fileFilter?: FileFilter-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## listNum

```TypeScript
listNum?: long
```

Number of file names to be listed. The default value is **0**, indicating that all files are listed.

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFileExtOptions-listNum?: long--><!--Device-ListFileExtOptions-listNum?: long-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## recursion

```TypeScript
recursion?: boolean
```

Whether to list all files in subfolders recursively. The default value is **false**. **false**: The names of files and directories that meet the filtering requirements in the current directory are returned. **true**: Relative paths (starting with /) of all files that meet the filtering requirements in the directory are returned.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ListFileExtOptions-recursion?: boolean--><!--Device-ListFileExtOptions-recursion?: boolean-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

