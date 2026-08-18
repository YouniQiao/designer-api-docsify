# WriteStream

Defines a writeable stream. You need to use [fileIo.createWriteStream](arkts-corefile-file-fs-createwritestream-f.md#createwritestream) to create a **WriteStream** instance, which is inherited from [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md#writable) .

**Inheritance/Implementation:** WriteStream extends [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md#writable)

**Since:** 12

<!--Device-unnamed-declare class WriteStream--><!--Device-unnamed-declare class WriteStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
```

## close

```TypeScript
close(): void
```

Closes this writeable stream.

**Since:** 12

<!--Device-WriteStream-close(): void--><!--Device-WriteStream-close(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID |
| --- |
| 13900004 |
| 13900005 |
| 13900008 |
| 13900025 |
| 13900041 |
| 13900042 |

**Examples**

```TypeScript
const filePath = pathDir + "/test.txt";
const ws = fileIo.createWriteStream(filePath);
ws.close();
```

## constructor

```TypeScript
constructor()
```

The WriteStream constructor.

**Since:** 12

<!--Device-WriteStream-constructor()--><!--Device-WriteStream-constructor()-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: number, whence?: WhenceType): number
```

Adjusts the position of the writeable stream offset pointer.

**Since:** 12

<!--Device-WriteStream-seek(offset: number, whence?: WhenceType): number--><!--Device-WriteStream-seek(offset: number, whence?: WhenceType): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| whence | [WhenceType](arkts-corefile-file-fs-whencetype-e.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900026 |
| 13900042 |

**Examples**

```TypeScript
const filePath = pathDir + "/test.txt";
const ws = fileIo.createWriteStream(filePath);
const curOff = ws.seek(5, fileIo.WhenceType.SEEK_SET);
console.info(`Succeeded in seeking, current offset is ${curOff}`);
ws.close();
```

## bytesWritten

```TypeScript
readonly bytesWritten: number
```

Number of bytes written to the writable stream.

**Type:** number

**Since:** 12

<!--Device-WriteStream-readonly bytesWritten: number--><!--Device-WriteStream-readonly bytesWritten: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file corresponding to the writeable stream.

**Type:** string

**Since:** 12

<!--Device-WriteStream-readonly path: string--><!--Device-WriteStream-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO
