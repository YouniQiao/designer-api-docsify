# File

File

**Since:** 3

**Deprecated since:** 10

<!--Device-unnamed-export default class File--><!--Device-unnamed-export default class File-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

## Modules to Import

```TypeScript
```

## access

```TypeScript
static access(options: FileAccessOption): void
```

Checks whether a file or directory exists.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [access](arkts-corefile-file-fs-access-f.md#access)

<!--Device-File-static access(options: FileAccessOption): void--><!--Device-File-static access(options: FileAccessOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileAccessOption](arkts-corefile-system-file-fileaccessoption-depr-i.md) | Yes | Options for checking whether a file or directory exists. |

## copy

```TypeScript
static copy(options: FileCopyOption): void
```

Copies a file to the given URI.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [copyFile](arkts-corefile-file-fs-copyfile-f.md#copyfile)

<!--Device-File-static copy(options: FileCopyOption): void--><!--Device-File-static copy(options: FileCopyOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileCopyOption](arkts-corefile-system-file-filecopyoption-depr-i.md) | Yes | Options for copying the files. |

## delete

```TypeScript
static delete(options: FileDeleteOption): void
```

Deletes a local file.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [unlink](arkts-corefile-file-fs-unlink-f.md#unlink)

<!--Device-File-static delete(options: FileDeleteOption): void--><!--Device-File-static delete(options: FileDeleteOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileDeleteOption](arkts-corefile-system-file-filedeleteoption-depr-i.md) | Yes | Options for deleting a local file. |

## get

```TypeScript
static get(options: FileGetOption): void
```

Obtains information about a local file.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [stat](arkts-corefile-file-fs-stat-f.md#stat)

<!--Device-File-static get(options: FileGetOption): void--><!--Device-File-static get(options: FileGetOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileGetOption](arkts-corefile-system-file-filegetoption-depr-i.md) | Yes | Options for obtaining information about a local file. |

## list

```TypeScript
static list(options: FileListOption): void
```

Obtains all files in the specified directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md#listfile)

<!--Device-File-static list(options: FileListOption): void--><!--Device-File-static list(options: FileListOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileListOption](arkts-corefile-system-file-filelistoption-depr-i.md) | Yes | Options for obtaining all files in the specified directory. |

## mkdir

```TypeScript
static mkdir(options: FileMkdirOption): void
```

Creates a directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md#mkdir)

<!--Device-File-static mkdir(options: FileMkdirOption): void--><!--Device-File-static mkdir(options: FileMkdirOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileMkdirOption](arkts-corefile-system-file-filemkdiroption-depr-i.md) | Yes | Options for creating a directory. |

## move

```TypeScript
static move(options: FileMoveOption): void
```

Moves a specified file to a given location.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [moveFile](arkts-corefile-file-fs-movefile-f.md#movefile)

<!--Device-File-static move(options: FileMoveOption): void--><!--Device-File-static move(options: FileMoveOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileMoveOption](arkts-corefile-system-file-filemoveoption-depr-i.md) | Yes | Options for moving the files. |

## readArrayBuffer

```TypeScript
static readArrayBuffer(options: FileReadArrayBufferOption): void
```

Reads buffer data from a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [read](arkts-corefile-file-fs-read-f.md#read)

<!--Device-File-static readArrayBuffer(options: FileReadArrayBufferOption): void--><!--Device-File-static readArrayBuffer(options: FileReadArrayBufferOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileReadArrayBufferOption](arkts-corefile-system-file-filereadarraybufferoption-depr-i.md) | Yes | Options for reading buffer data from a file. |

## readText

```TypeScript
static readText(options: FileReadTextOption): void
```

Reads text from a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [readText](arkts-corefile-file-fs-readtext-f.md#readtext)

<!--Device-File-static readText(options: FileReadTextOption): void--><!--Device-File-static readText(options: FileReadTextOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileReadTextOption](arkts-corefile-system-file-filereadtextoption-depr-i.md) | Yes | Options for reading text from a file. |

## rmdir

```TypeScript
static rmdir(options: FileRmdirOption): void
```

Deletes a directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [rmdir](arkts-corefile-file-fs-rmdir-f.md#rmdir)

<!--Device-File-static rmdir(options: FileRmdirOption): void--><!--Device-File-static rmdir(options: FileRmdirOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileRmdirOption](arkts-corefile-system-file-filermdiroption-depr-i.md) | Yes | Options for deleting a directory. |

## writeArrayBuffer

```TypeScript
static writeArrayBuffer(options: FileWriteArrayBufferOption): void
```

Writes buffer data into a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-File-static writeArrayBuffer(options: FileWriteArrayBufferOption): void--><!--Device-File-static writeArrayBuffer(options: FileWriteArrayBufferOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileWriteArrayBufferOption](arkts-corefile-system-file-filewritearraybufferoption-depr-i.md) | Yes | Options for writing buffer data into a file. |

## writeText

```TypeScript
static writeText(options: FileWriteTextOption): void
```

Writes text into a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md#write)

<!--Device-File-static writeText(options: FileWriteTextOption): void--><!--Device-File-static writeText(options: FileWriteTextOption): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [FileWriteTextOption](arkts-corefile-system-file-filewritetextoption-depr-i.md) | Yes | Options for writing text into a file. |

