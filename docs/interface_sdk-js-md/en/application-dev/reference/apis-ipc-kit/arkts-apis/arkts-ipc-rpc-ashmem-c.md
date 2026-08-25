# Ashmem

Provides methods related to anonymous shared memory objects, including creating, closing, mapping, and unmapping an **Ashmem** object, reading data from and writing data to an **Ashmem** object, obtaining the **Ashmem** size, and setting **Ashmem** protection. The shared memory applies only to cross-process communication within the local device.

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## closeAshmem

```TypeScript
closeAshmem(): void
```

Closes this **Ashmem** object.

> **NOTE：**&gt;
> Before closing the **Ashmem** object, you need to remove the address mapping.

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

## create

```TypeScript
static create(name: string, size: number): Ashmem
```

Creates an **Ashmem** object with the specified name and size. This API is a static method.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## create

```TypeScript
static create(ashmem: Ashmem): Ashmem
```

Creates an **Ashmem** object by copying the file descriptor of an existing **Ashmem** object. The two **Ashmem** objects point to the same shared memory region.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## createAshmem

```TypeScript
static createAshmem(name: string, size: number): Ashmem
```

Creates an **Ashmem** object with the specified name and size. This API is a static method.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** create()

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

## createAshmemFromExisting

```TypeScript
static createAshmemFromExisting(ashmem: Ashmem): Ashmem
```

Creates an **Ashmem** object by copying the file descriptor of an existing **Ashmem** object. The two **Ashmem** objects point to the same shared memory region.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** create()

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

## getAshmemSize

```TypeScript
getAshmemSize(): number
```

Obtains the memory size of this **Ashmem** object.

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## mapAshmem

```TypeScript
mapAshmem(mapType: number): boolean
```

Creates the shared file mapping on the virtual address space of this process. The size of the mapping region is specified by this **Ashmem** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [mapTypedAshmem](#maptypedashmem)(mapType: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mapType | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## mapReadAndWriteAshmem

```TypeScript
mapReadAndWriteAshmem(): boolean
```

Maps the shared file to the readable and writable virtual address space of the process.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [mapReadWriteAshmem](#mapreadwriteashmem)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## mapReadOnlyAshmem

```TypeScript
mapReadOnlyAshmem(): boolean
```

Maps the shared file to the read-only virtual address space of the process.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [mapReadonlyAshmem](#mapreadonlyashmem)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## mapReadonlyAshmem

```TypeScript
mapReadonlyAshmem(): void
```

Maps the shared file to the read-only virtual address space of the process.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Error codes:**

| Error Code ID |
| --- |
| [1900001](../errorcode-rpc.md#1900001-failed-to-call-mmap) |

## mapReadWriteAshmem

```TypeScript
mapReadWriteAshmem(): void
```

Maps the shared file to the readable and writable virtual address space of the process.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Error codes:**

| Error Code ID |
| --- |
| [1900001](../errorcode-rpc.md#1900001-failed-to-call-mmap) |

## mapTypedAshmem

```TypeScript
mapTypedAshmem(mapType: number): void
```

Creates the shared file mapping on the virtual address space of this process. The size of the mapping region is specified by this **Ashmem** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mapType | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900001](../errorcode-rpc.md#1900001-failed-to-call-mmap) |

## readAshmem

```TypeScript
readAshmem(size: number, offset: number): number[]
```

Reads data from the shared file associated with this **Ashmem** object.

> **NOTE：**&gt;
> - Before writing an **Ashmem** object, you need to call
> [mapReadWriteAshmem](#mapreadwriteashmem) for mapping.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [readDataFromAshmem](#readdatafromashmem)(size: int, offset: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900004](../errorcode-rpc.md#1900004-failed-to-read-data-from-the-shared-memory) |

## readDataFromAshmem

```TypeScript
readDataFromAshmem(size: number, offset: number): ArrayBuffer
```

Reads data from the shared file associated with this **Ashmem** object.

> **NOTE：**&gt;
> Before writing an **Ashmem** object, you need to call
> [mapReadWriteAshmem](#mapreadwriteashmem) for mapping.

**Since:** 11

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900004](../errorcode-rpc.md#1900004-failed-to-read-data-from-the-shared-memory) |

## readFromAshmem

```TypeScript
readFromAshmem(size: number, offset: number): number[]
```

Reads data from the shared file associated with this **Ashmem** object.

> **NOTE：**&gt;
> - Before writing an **Ashmem** object, you need to call
> [mapReadWriteAshmem](#mapreadwriteashmem) for mapping.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readDataFromAshmem](#readdatafromashmem)(size: int, offset: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## setProtection

```TypeScript
setProtection(protectionType: number): boolean
```

Sets the protection level of the memory region to which the shared file is mapped.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [setProtectionType](#setprotectiontype)(protectionType: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| protectionType | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setProtectionType

```TypeScript
setProtectionType(protectionType: number): void
```

Sets the protection level of the memory region to which the shared file is mapped.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| protectionType | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900002](../errorcode-rpc.md#1900002-failed-to-call-ioctl) |

## unmapAshmem

```TypeScript
unmapAshmem(): void
```

Deletes the mappings for the specified address range of this **Ashmem** object.

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

## writeAshmem

```TypeScript
writeAshmem(buf: number[], size: number, offset: number): void
```

Writes data to the shared file associated with this **Ashmem** object.

> **NOTE：**&gt;
> - Before writing an **Ashmem** object, you need to call
> [mapReadWriteAshmem](#mapreadwriteashmem) for mapping.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [writeDataToAshmem](#writedatatoashmem)(buf: ArrayBuffer, size: int, offset: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | number[] | Yes |
| size | number | Yes |
| offset | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900003](../errorcode-rpc.md#1900003-failed-to-write-data-to-the-shared-memory) |

## writeDataToAshmem

```TypeScript
writeDataToAshmem(buf: ArrayBuffer, size: number, offset: number): void
```

Writes data to the shared file associated with this **Ashmem** object.

> **NOTE：**&gt;
> Before writing an **Ashmem** object, you need to call
> [mapReadWriteAshmem](#mapreadwriteashmem) for mapping.

**Since:** 11

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| size | number | Yes |
| offset | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900003](../errorcode-rpc.md#1900003-failed-to-write-data-to-the-shared-memory) |

## writeToAshmem

```TypeScript
writeToAshmem(buf: number[], size: number, offset: number): boolean
```

Writes data to the shared file associated with this **Ashmem** object.

> **NOTE：**&gt;
> - Before writing an **Ashmem** object, you need to call
> [mapReadWriteAshmem](#mapreadwriteashmem) for mapping.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [writeDataToAshmem](#writedatatoashmem)(buf: ArrayBuffer, size: int, offset: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | number[] | Yes |
| size | number | Yes |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## PROT_EXEC

```TypeScript
static readonly PROT_EXEC: number
```

Mapped memory protection type, indicating that the mapped memory is executable.

**Type:** number

**Default:** 4

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

## PROT_NONE

```TypeScript
static readonly PROT_NONE: number
```

Mapped memory protection type, indicating that the mapped memory cannot be accessed.

**Type:** number

**Default:** 0

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

## PROT_READ

```TypeScript
static readonly PROT_READ: number
```

Mapped memory protection type, indicating that the mapped memory is readable.

**Type:** number

**Default:** 1

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core

## PROT_WRITE

```TypeScript
static readonly PROT_WRITE: number
```

Mapped memory protection type, indicating that the mapped memory is readable.

**Type:** number

**Default:** 2

**Since:** 8

**System capability:** SystemCapability.Communication.IPC.Core
