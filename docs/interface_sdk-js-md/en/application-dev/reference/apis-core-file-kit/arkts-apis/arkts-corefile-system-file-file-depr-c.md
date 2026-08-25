# File

File

**Since:** 3

**Deprecated since:** 10

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

**Substitutes:** [access](arkts-corefile-file-fs-access-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileAccessOption](arkts-corefile-system-file-fileaccessoption-depr-i.md) | Yes |

## copy

```TypeScript
static copy(options: FileCopyOption): void
```

Copies a file to the given URI.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileCopyOption](arkts-corefile-system-file-filecopyoption-depr-i.md) | Yes |

## delete

```TypeScript
static delete(options: FileDeleteOption): void
```

Deletes a local file.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [unlink](arkts-corefile-file-fs-unlink-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileDeleteOption](arkts-corefile-system-file-filedeleteoption-depr-i.md) | Yes |

## get

```TypeScript
static get(options: FileGetOption): void
```

Obtains information about a local file.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [stat](arkts-corefile-file-fs-stat-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileGetOption](arkts-corefile-system-file-filegetoption-depr-i.md) | Yes |

## list

```TypeScript
static list(options: FileListOption): void
```

Obtains all files in the specified directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileListOption](arkts-corefile-system-file-filelistoption-depr-i.md) | Yes |

## mkdir

```TypeScript
static mkdir(options: FileMkdirOption): void
```

Creates a directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileMkdirOption](arkts-corefile-system-file-filemkdiroption-depr-i.md) | Yes |

## move

```TypeScript
static move(options: FileMoveOption): void
```

Moves a specified file to a given location.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [moveFile](arkts-corefile-file-fs-movefile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileMoveOption](arkts-corefile-system-file-filemoveoption-depr-i.md) | Yes |

## readArrayBuffer

```TypeScript
static readArrayBuffer(options: FileReadArrayBufferOption): void
```

Reads buffer data from a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [read](arkts-corefile-file-fs-read-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileReadArrayBufferOption](arkts-corefile-system-file-filereadarraybufferoption-depr-i.md) | Yes |

## readText

```TypeScript
static readText(options: FileReadTextOption): void
```

Reads text from a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [readText](arkts-corefile-file-fs-readtext-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileReadTextOption](arkts-corefile-system-file-filereadtextoption-depr-i.md) | Yes |

## rmdir

```TypeScript
static rmdir(options: FileRmdirOption): void
```

Deletes a directory.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [rmdir](arkts-corefile-file-fs-rmdir-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileRmdirOption](arkts-corefile-system-file-filermdiroption-depr-i.md) | Yes |

## writeArrayBuffer

```TypeScript
static writeArrayBuffer(options: FileWriteArrayBufferOption): void
```

Writes buffer data into a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileWriteArrayBufferOption](arkts-corefile-system-file-filewritearraybufferoption-depr-i.md) | Yes |

## writeText

```TypeScript
static writeText(options: FileWriteTextOption): void
```

Writes text into a file. Only text files can be read and written.

**Since:** 3

**Deprecated since:** 10

**Substitutes:** [write](arkts-corefile-file-fs-write-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [FileWriteTextOption](arkts-corefile-system-file-filewritetextoption-depr-i.md) | Yes |
