# FileMapping

File mapping object. Before invoking the FileMapping method, you need to use the mmap() method (synchronous or asynchronous) to construct a FileMapping instance.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-fileIo-interface FileMapping--><!--Device-fileIo-interface FileMapping-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## capacity

```TypeScript
capacity(): int
```

Obtains the capacity of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-capacity(): int--><!--Device-FileMapping-capacity(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | Size of the file mapping area, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |

## flip

```TypeScript
flip(): void
```

Mode reversal. That is, the limit attribute is set to the current position, and then the current position is set to 0.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-flip(): void--><!--Device-FileMapping-flip(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |

## getLimit

```TypeScript
getLimit(): int
```

Obtains the upper bound of the readable and writable area of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |

## getPosition

```TypeScript
getPosition(): int
```

Gets the current location of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-getPosition(): int--><!--Device-FileMapping-getPosition(): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| int | Current location of the file mapping area, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |

## msync

```TypeScript
msync(): Promise<void>
```

Synchronizes the dirty page data in the entire file mapping area to the disk file and uses the promise asynchronous callback function. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msync(): Promise<void>--><!--Device-FileMapping-msync(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise object. No return value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900011 | Out of memory |
| 13900014 | Device or resource busy |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |

## msync

```TypeScript
msync(position: int, length: int): Promise<void>
```

Synchronizes the dirty page data in the specified range of the file mapping area to the disk file and uses the promise asynchronous callback function. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msync(position: int, length: int): Promise<void>--><!--Device-FileMapping-msync(position: int, length: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position to synchronize from, in bytes. |
| length | int | Yes | Length of the data to be synchronized, in bytes. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise object. No return value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900011 | Out of memory |
| 13900014 | Device or resource busy |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |

## msyncSync

```TypeScript
msyncSync(): void
```

Synchronizes the dirty page data of the entire file mapping area to the disk file by using the synchronization method. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msyncSync(): void--><!--Device-FileMapping-msyncSync(): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900011 | Out of memory |
| 13900014 | Device or resource busy |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |

## msyncSync

```TypeScript
msyncSync(position: int, length: int): void
```

Synchronize the dirty page data in the specified range of the file mapping area to the disk file by using the synchronization method. Note: If the file is not stored on the local device, calling this API does not ensure that all changes are stored persistently.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-msyncSync(position: int, length: int): void--><!--Device-FileMapping-msyncSync(position: int, length: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position to synchronize from, in bytes. |
| length | int | Yes | Length of the data to be synchronized, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900011 | Out of memory |
| 13900014 | Device or resource busy |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |
| 13900055 | Mmap operation not supported |

## read

```TypeScript
read(buffer: ArrayBuffer, length?: int): int
```

Reads data from the current position and moves the position backward by the number of bytes actually read.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-read(buffer: ArrayBuffer, length?: int): int--><!--Device-FileMapping-read(buffer: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes | Buffer for storing the read file data. |
| length | int | No | Length of the data to be read, in bytes. This parameter is optional.The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - Length of the actually read data, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |
| 13900052 | Mmap buffer released |
| 13900054 | Mmap buffer is inaccessible |

## read

```TypeScript
read(position: int, buffer: ArrayBuffer, length?: int): int
```

Reads data from the specified location without affecting the current location.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-read(position: int, buffer: ArrayBuffer, length?: int): int--><!--Device-FileMapping-read(position: int, buffer: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position to read from. |
| buffer | ArrayBuffer | Yes | Buffer for storing the read file data. |
| length | int | No | Length of the data to be read, in bytes. This parameter is optional.The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - Length of the actually read data, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |
| 13900052 | Mmap buffer released |
| 13900054 | Mmap buffer is inaccessible |

## remaining

```TypeScript
remaining(): int
```

Obtains the number of remaining bytes between the current position (position) and the upper bound (limit) of the readable and writable area.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |

## setLimit

```TypeScript
setLimit(limit: int): void
```

Sets the upper bound of the readable and writable area of the file mapping area. The upper bound does not exceed the total capacity of the mapping area (0 <= limit <= capacity).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-setLimit(limit: int): void--><!--Device-FileMapping-setLimit(limit: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| limit | int | Yes | Upper bound of the readable and writable area to be set, in bytes. If the current position is greater than the new upper bound, the value is automatically adjusted to limit. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |

## setPosition

```TypeScript
setPosition(position: int): void
```

Sets the current location of the file mapping area.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-setPosition(position: int): void--><!--Device-FileMapping-setPosition(position: int): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Target location, in bytes. The value must be a non-negative number and cannot be greater than the current upper bound (limit). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900052 | Mmap buffer released |

## unmap

```TypeScript
unmap(): Promise<void>
```

Releases the file mapping area and use the promise asynchronous callback function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-unmap(): Promise<void>--><!--Device-FileMapping-unmap(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | - Promise object. No return value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |

## unmapSync

```TypeScript
unmapSync(): void
```

Releases the file mapping area by using the synchronization method.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

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

Writes data from the current location and moves the location backward by the number of bytes actually written.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-write(data: ArrayBuffer, length?: int): int--><!--Device-FileMapping-write(data: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArrayBuffer | Yes | Buffer data to be written to the file. |
| length | int | No | Length of the data to be written, in bytes. This parameter is optional.The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - Length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |
| 13900052 | Mmap buffer released |
| 13900053 | Read-only mmap buffer |
| 13900054 | Mmap buffer is inaccessible |

## write

```TypeScript
write(position: int, data: ArrayBuffer, length?: int): int
```

Writes data from the specified location without affecting the current location.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FileMapping-write(position: int, data: ArrayBuffer, length?: int): int--><!--Device-FileMapping-write(position: int, data: ArrayBuffer, length?: int): int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | int | Yes | Start position of the expected write. |
| data | ArrayBuffer | Yes | Buffer data to be written to the file. |
| length | int | No | Length of the data to be written, in bytes. This parameter is optional.The default value is the buffer length. |

**Return value:**

| Type | Description |
| --- | --- |
| int | - Length of the data written, in bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900050 | Internal resource error |
| 13900051 | Buffer read/write out of bounds |
| 13900052 | Mmap buffer released |
| 13900053 | Read-only mmap buffer |
| 13900054 | Mmap buffer is inaccessible |

