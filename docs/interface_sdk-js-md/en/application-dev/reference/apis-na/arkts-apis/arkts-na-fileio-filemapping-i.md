# FileMapping

Defines a file mapping object. Before calling the **FileMapping** method, construct a **FileMapping** instance using [mmap()](arkts-na-fileio-mmap-f.md#mmap) or [mmapSync()](arkts-na-fileio-mmapsync-f.md#mmapsync).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-fileIo-interface FileMapping--><!--Device-fileIo-interface FileMapping-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## capacity

```TypeScript
capacity(): int
```

Obtains the capacity of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-capacity(): int--><!--Device-FileMapping-capacity(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | Capacity of the file mapping area, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## flip

```TypeScript
flip(): void
```

Flips the file mapping area to switch from the write-ready state to the read-ready state. After this API is called, **limit** is set to the value of **position**, and **position** is reset to **0**. It is recommended that this API be called to prepare for subsequent [read()](arkts-na-fileio-stream-i.md#read) operations after the[write()](arkts-na-fileio-stream-i.md#write) operations are complete.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-flip(): void--><!--Device-FileMapping-flip(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## getLimit

```TypeScript
getLimit(): int
```

Obtains the upper bound of the readable and writable area of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-getLimit(): int--><!--Device-FileMapping-getLimit(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | Upper bound of the current readable and writable area, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## getPosition

```TypeScript
getPosition(): int
```

Gets the current location of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-getPosition(): int--><!--Device-FileMapping-getPosition(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | Current position of the file mapping area, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## msync

```TypeScript
msync(): Promise<void>
```

Synchronizes data of the entire file mapping area to the disk file synchronously. This API uses a promise to return the result. > **NOTE：**> > If the file is not stored on the local device, calling this API does not ensure that all changes are stored > persistently.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msync(): Promise<void>--><!--Device-FileMapping-msync(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## msync

```TypeScript
msync(position: int, length: int): Promise<void>
```

Synchronizes data in the specified range of the file mapping area to the disk file synchronously. This API uses a promise to return the result. > **NOTE：**> > If the file is not stored on the local device, calling this API does not ensure that all changes are stored > persistently.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msync(position: int, length: int): Promise<void>--><!--Device-FileMapping-msync(position: int, length: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position to synchronize, in bytes. |
| length | int | Yes | Length of the data to synchronize, in bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## msyncSync

```TypeScript
msyncSync(): void
```

Synchronizes data of the entire file mapping area to the disk file synchronously. > **NOTE：**> > If the file is not stored on the local device, calling this API does not ensure that all changes are stored > persistently.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msyncSync(): void--><!--Device-FileMapping-msyncSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## msyncSync

```TypeScript
msyncSync(position: int, length: int): void
```

Synchronizes data in the specified range of the file mapping area to the disk file synchronously. > **NOTE：**> > If the file is not stored on the local device, calling this API does not ensure that all changes are stored > persistently.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msyncSync(position: int, length: int): void--><!--Device-FileMapping-msyncSync(position: int, length: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position to synchronize, in bytes. |
| length | int | Yes | Length of the data to synchronize, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |
| 13900050 | Internal resource error |
| 13900014 | Device or resource busy |
| 13900011 | Out of memory |

## read

```TypeScript
read(buffer: ArrayBuffer, length?: int): int
```

Reads data from the current position and moves the position backward by the number of bytes actually read.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-read(buffer: ArrayBuffer, length?: int): int--><!--Device-FileMapping-read(buffer: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| length | int | No | Length of the data to read, in bytes. The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

## read

```TypeScript
read(position: int, buffer: ArrayBuffer, length?: int): int
```

Reads data from the specified position. The current position does not move.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-read(position: int, buffer: ArrayBuffer, length?: int): int--><!--Device-FileMapping-read(position: int, buffer: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position to read the data, in bytes. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| length | int | No | Length of the data to read, in bytes. The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | Length of the data read, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

## remaining

```TypeScript
remaining(): int
```

Obtains the number of remaining bytes between the current position (**position**) and the upper bound (**limit**) of the readable and writable area.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-remaining(): int--><!--Device-FileMapping-remaining(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | Number of remaining readable or writable bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## setLimit

```TypeScript
setLimit(limit: int): void
```

Sets the upper bound of the readable and writable area of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-setLimit(limit: int): void--><!--Device-FileMapping-setLimit(limit: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| limit | int | Yes | Upper bound of the readable and writable area to set, in bytes. <br>The value is greater than or equal to 0 and less than or equal to the value of [capacity](#capacity). If the value of **limit** is smaller than that of **position** in the file mapping area, the value of **position** is automatically adjusted to that of **limit**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## setPosition

```TypeScript
setPosition(position: int): void
```

Sets the current location of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-setPosition(position: int): void--><!--Device-FileMapping-setPosition(position: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Target position to set, in bytes. <br>The value must be a non-negative number and cannot be greater than the upper bound (**limit**) of the readable and writable area. You can obtain the value of **limit** by calling [getLimit()](#getlimit). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900050 | Internal resource error |

## unmap

```TypeScript
unmap(): Promise<void>
```

Releases the file mapping area. This API uses a promise to return the result. After this API is called, **position**, **limit**, and **capacity** are all reset to **0**, and no operation can be performed on the **FileMapping** object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-unmap(): Promise<void>--><!--Device-FileMapping-unmap(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |

## unmapSync

```TypeScript
unmapSync(): void
```

Releases the file mapping area synchronously. After this API is called, **position**, **limit**, and **capacity** are all reset to **0**, and no operation can be performed on the **FileMapping** object.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-unmapSync(): void--><!--Device-FileMapping-unmapSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |

## write

```TypeScript
write(data: ArrayBuffer, length?: int): int
```

Writes data from the current position and moves the position backward by the number of bytes actually written.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-write(data: ArrayBuffer, length?: int): int--><!--Device-FileMapping-write(data: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArrayBuffer | Yes | Buffer data to be written to the file. |
| length | int | No | Length of the data to write, in bytes. The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900053 | Read-only mmap buffer |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

## write

```TypeScript
write(position: int, data: ArrayBuffer, length?: int): int
```

Writes data to the specified position. The current position does not move.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-write(position: int, data: ArrayBuffer, length?: int): int--><!--Device-FileMapping-write(position: int, data: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position to write, in bytes. |
| data | ArrayBuffer | Yes | Buffer data to be written to the file. |
| length | int | No | Length of the data to write, in bytes. This parameter is optional. The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | return the length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900052 | Mmap buffer released |
| 13900053 | Read-only mmap buffer |
| 13900054 | Mmap buffer is inaccessible |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |

