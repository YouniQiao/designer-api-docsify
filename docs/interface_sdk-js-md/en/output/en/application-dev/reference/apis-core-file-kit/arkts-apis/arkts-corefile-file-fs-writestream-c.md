# WriteStream

Defines a writeable stream. You need to use \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to create a **WriteStream** instance, which is inherited from [stream.Writable]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ .

**Inheritance/Implementation:** WriteStream extends [stream.Writable](../../apis-arkts/arkts-apis/arkts-arkts-stream-writable-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class WriteStream extends stream.Writable--><!--Device-unnamed-declare class WriteStream extends stream.Writable-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## close

```TypeScript
close(): void
```

Closes this writeable stream.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WriteStream-close(): void--><!--Device-WriteStream-close(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900004 | Interrupted system call |
| 13900005 | I/O error |
| 13900008 | Bad file descriptor |
| 13900025 | No space left on device |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Example**

```TypeScript
const filePath = pathDir + "/test.txt";
const ws = fs.createWriteStream(filePath);
ws.close();
```

## constructor

```TypeScript
constructor()
```

The WriteStream constructor.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WriteStream-constructor()--><!--Device-WriteStream-constructor()-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## seek

```TypeScript
seek(offset: number, whence?: WhenceType): number
```

Adjusts the position of the writeable stream offset pointer.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WriteStream-seek(offset: number, whence?: WhenceType): number--><!--Device-WriteStream-seek(offset: number, whence?: WhenceType): number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | Relative offset, in bytes. |
| whence | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Where to start the offset. The default value is **SEEK\_\_\_ESCAPED\_UNDERSCORE\_\_\_SET**, which indicates the beginning of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Position of the current offset pointer (offset relative to the file header, in bytes). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error |
| 13900020 | Invalid argument |
| 13900026 | Illegal seek |
| 13900042 | Unknown error |

**Example**

```TypeScript
const filePath = pathDir + "/test.txt";
const ws = fs.createWriteStream(filePath);
const curOff = ws.seek(5, fs.WhenceType.SEEK_SET);
console.info(`current offset is ${curOff}`);
ws.close();
```

## bytesWritten

```TypeScript
readonly bytesWritten: number
```

Number of bytes written to the writable stream.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WriteStream-readonly bytesWritten: number--><!--Device-WriteStream-readonly bytesWritten: number-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## path

```TypeScript
readonly path: string
```

Path of the file corresponding to the writeable stream.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-WriteStream-readonly path: string--><!--Device-WriteStream-readonly path: string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

