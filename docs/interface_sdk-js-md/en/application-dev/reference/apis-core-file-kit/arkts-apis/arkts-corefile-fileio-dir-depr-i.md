# Dir

Manages directories. Before calling a method of the **Dir** class, use the **opendir()** method synchronously or asynchronously to create a **Dir** instance.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): Promise<void>
```

Closes a directory. This API uses a promise to return the result. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## close

```TypeScript
close(callback: AsyncCallback<void>): void
```

Closes a directory. This API uses an asynchronous callback to return the result. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## closeSync

```TypeScript
closeSync(): void
```

Closes a directory. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

## read

```TypeScript
read(): Promise<Dirent>
```

Reads the next directory entry. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Dirent](arkts-corefile-fileio-dirent-depr-i.md)&gt; |

## read

```TypeScript
read(callback: AsyncCallback<Dirent>): void
```

Reads the next directory entry. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Dirent](arkts-corefile-fileio-dirent-depr-i.md)&gt; | Yes |

## readSync

```TypeScript
readSync(): Dirent
```

Reads the next directory entry. This API returns the result synchronously.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [listFile](arkts-corefile-file-fs-listfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Dirent](arkts-corefile-fileio-dirent-depr-i.md) |
