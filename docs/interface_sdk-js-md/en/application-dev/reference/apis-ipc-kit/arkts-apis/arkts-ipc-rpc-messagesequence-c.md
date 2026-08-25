# MessageSequence

Provides APIs for reading and writing data in specific format. During RPC or IPC, the sender can use the **write()** method provided by **MessageSequence** to write data in specific format to a **MessageSequence** object. The receiver can use the **read()** method provided by **MessageSequence** to read data in specific format from a **MessageSequence** object. The data formats include basic data types and arrays, IPC objects, interface tokens, and custom sequenceable objects.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## closeFileDescriptor

```TypeScript
static closeFileDescriptor(fd: number): void
```

Closes a file descriptor. This API is a static method.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## containFileDescriptors

```TypeScript
containFileDescriptors(): boolean
```

Checks whether this **MessageSequence** object contains file descriptors.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## create

```TypeScript
static create(): MessageSequence
```

Creates a **MessageSequence** object. This API is a static method.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MessageSequence](arkts-ipc-rpc-messagesequence-c.md) |

## dupFileDescriptor

```TypeScript
static dupFileDescriptor(fd: number): number
```

Duplicates a file descriptor. This API is a static method.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900013](../errorcode-rpc.md#1900013-failed-to-invoke-dup) |

## getCapacity

```TypeScript
getCapacity(): number
```

Obtains the capacity of this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getRawDataCapacity

```TypeScript
getRawDataCapacity(): number
```

Obtains the maximum amount of raw data that can be held by this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReadableBytes

```TypeScript
getReadableBytes(): number
```

Obtains the readable capacity of this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReadPosition

```TypeScript
getReadPosition(): number
```

Obtains the read position of this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

Obtains the data size of this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWritableBytes

```TypeScript
getWritableBytes(): number
```

Obtains the writable capacity (in bytes) of this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWritePosition

```TypeScript
getWritePosition(): number
```

Obtains the write position of this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readArrayBuffer

```TypeScript
readArrayBuffer(typeCode: TypeCode): ArrayBuffer
```

Reads data of the ArrayBuffer type from this **MessageSequence**.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| typeCode | [TypeCode](arkts-ipc-rpc-typecode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readAshmem

```TypeScript
readAshmem(): Ashmem
```

Reads the anonymous shared object from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readBoolean

```TypeScript
readBoolean(): boolean
```

Reads the Boolean value from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readBooleanArray

```TypeScript
readBooleanArray(dataIn: boolean[]): void
```

Reads the Boolean array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | boolean[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readBooleanArray

```TypeScript
readBooleanArray(): boolean[]
```

Reads the Boolean array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readByte

```TypeScript
readByte(): number
```

Reads the byte value from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readByteArray

```TypeScript
readByteArray(dataIn: number[]): void
```

Reads the byte array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readByteArray

```TypeScript
readByteArray(): number[]
```

Reads the byte array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readChar

```TypeScript
readChar(): number
```

Reads the character from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readCharArray

```TypeScript
readCharArray(dataIn: number[]): void
```

Reads the character array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readCharArray

```TypeScript
readCharArray(): number[]
```

Reads the character array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readDouble

```TypeScript
readDouble(): number
```

Reads the number value from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readDoubleArray

```TypeScript
readDoubleArray(dataIn: number[]): void
```

Reads the number array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readDoubleArray

```TypeScript
readDoubleArray(): number[]
```

Reads the number array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readException

```TypeScript
readException(): void
```

Reads the exception information from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readFileDescriptor

```TypeScript
readFileDescriptor(): number
```

Reads the file descriptor from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readFloat

```TypeScript
readFloat(): number
```

Reads the number value from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readFloatArray

```TypeScript
readFloatArray(dataIn: number[]): void
```

Reads the number array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readFloatArray

```TypeScript
readFloatArray(): number[]
```

Reads the number array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readInt

```TypeScript
readInt(): number
```

Reads the integer from this **MessageSequence** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readIntArray

```TypeScript
readIntArray(dataIn: number[]): void
```

Reads the integer array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readIntArray

```TypeScript
readIntArray(): number[]
```

Reads the integer array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readInterfaceToken

```TypeScript
readInterfaceToken(): string
```

Reads the interface token from this **MessageSequence** object. The interface token is read in the sequence in which it is written to the **MessageSequence** object. The local object can use it to verify the communication.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readLong

```TypeScript
readLong(): number
```

Reads the number integer from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readLongArray

```TypeScript
readLongArray(dataIn: number[]): void
```

Reads the number array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readLongArray

```TypeScript
readLongArray(): number[]
```

Reads the number integer array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readParcelable

```TypeScript
readParcelable(dataIn: Parcelable): void
```

Reads the **Parcelable** object from this **MessageSequence** object to the specified object (**dataIn**).

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | [Parcelable](arkts-ipc-rpc-parcelable-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |
| [1900012](../errorcode-rpc.md#1900012-js-callback-execution-failed) |

## readParcelableArray

```TypeScript
readParcelableArray(parcelableArray: Parcelable[]): void
```

Reads the **Parcelable** array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parcelableArray | [Parcelable](arkts-ipc-rpc-parcelable-i.md)[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |
| [1900012](../errorcode-rpc.md#1900012-js-callback-execution-failed) |

## readRawData

```TypeScript
readRawData(size: number): number[]
```

Reads raw data from this **MessageSequence** object.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [readRawDataBuffer](#readrawdatabuffer)(size: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readRawDataBuffer

```TypeScript
readRawDataBuffer(size: number): ArrayBuffer
```

Reads raw data from this **MessageSequence** object.

**Since:** 11

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readRemoteObject

```TypeScript
readRemoteObject(): IRemoteObject
```

Reads the remote object from **MessageSequence**. You can use this API to deserialize the **MessageSequence** object to generate an **IRemoteObject**. The remote object is read in the order in which it is written to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1900008](../errorcode-rpc.md#1900008-invalid-ipc-object) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(objects: IRemoteObject[]): void
```

Reads the **IRemoteObject** array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| objects | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(): IRemoteObject[]
```

Reads the **IRemoteObject** array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readShort

```TypeScript
readShort(): number
```

Reads the short integer from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readShortArray

```TypeScript
readShortArray(dataIn: number[]): void
```

Reads the short array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readShortArray

```TypeScript
readShortArray(): number[]
```

Reads the short array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readString

```TypeScript
readString(): string
```

Reads the string from this **MessageSequence** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readStringArray

```TypeScript
readStringArray(dataIn: string[]): void
```

Reads the string array from this **MessageSequence** object and writes it to the created empty array.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | string[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## readStringArray

```TypeScript
readStringArray(): string[]
```

Reads the string array from this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Error codes:**

| Error Code ID |
| --- |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## reclaim

```TypeScript
reclaim(): void
```

Reclaims the **MessageSequence** object that is no longer used.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

## rewindRead

```TypeScript
rewindRead(pos: number): void
```

Moves the read pointer to the specified position.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900010](../errorcode-rpc.md#1900010-failed-to-read-data-from-messagesequence) |

## rewindWrite

```TypeScript
rewindWrite(pos: number): void
```

Moves the write pointer to the specified position.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## setCapacity

```TypeScript
setCapacity(size: number): void
```

Sets the storage capacity of this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |
| [1900011](../errorcode-rpc.md#1900011-memory-allocation-failed) |

## setSize

```TypeScript
setSize(size: number): void
```

Sets the size of the data contained in this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeArrayBuffer

```TypeScript
writeArrayBuffer(buf: ArrayBuffer, typeCode: TypeCode): void
```

Writes data of the ArrayBuffer type to this **MessageSequence** object.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buf | ArrayBuffer | Yes |
| typeCode | [TypeCode](arkts-ipc-rpc-typecode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeAshmem

```TypeScript
writeAshmem(ashmem: Ashmem): void
```

Writes an anonymous shared object to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeBoolean

```TypeScript
writeBoolean(val: boolean): void
```

Writes a Boolean value to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeBooleanArray

```TypeScript
writeBooleanArray(booleanArray: boolean[]): void
```

Writes a Boolean array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| booleanArray | boolean[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeByte

```TypeScript
writeByte(val: number): void
```

Writes a byte value to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeByteArray

```TypeScript
writeByteArray(byteArray: number[]): void
```

Writes a byte array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| byteArray | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeChar

```TypeScript
writeChar(val: number): void
```

Writes a character to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeCharArray

```TypeScript
writeCharArray(charArray: number[]): void
```

Writes a character array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| charArray | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeDouble

```TypeScript
writeDouble(val: number): void
```

Writes a number value to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeDoubleArray

```TypeScript
writeDoubleArray(doubleArray: number[]): void
```

Writes a number array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| doubleArray | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeFileDescriptor

```TypeScript
writeFileDescriptor(fd: number): void
```

Writes a file descriptor to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeFloat

```TypeScript
writeFloat(val: number): void
```

Writes a number value to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeFloatArray

```TypeScript
writeFloatArray(floatArray: number[]): void
```

Writes a number array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| floatArray | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeInt

```TypeScript
writeInt(val: number): void
```

Writes an integer to this **MessageSequence** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeIntArray

```TypeScript
writeIntArray(intArray: number[]): void
```

Writes an integer array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| intArray | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeInterfaceToken

```TypeScript
writeInterfaceToken(token: string): void
```

Writes an interface token to this **MessageSequence** object. The remote object can use this interface token to verify the communication.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeLong

```TypeScript
writeLong(val: number): void
```

Writes a number integer to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeLongArray

```TypeScript
writeLongArray(longArray: number[]): void
```

Writes a number array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| longArray | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeNoException

```TypeScript
writeNoException(): void
```

Writes information to this **MessageSequence** object indicating that no exception occurred.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Error codes:**

| Error Code ID |
| --- |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeParcelable

```TypeScript
writeParcelable(val: Parcelable): void
```

Writes a **Parcelable** object to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | [Parcelable](arkts-ipc-rpc-parcelable-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeParcelableArray

```TypeScript
writeParcelableArray(parcelableArray: Parcelable[]): void
```

Writes the **Parcelable** array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| parcelableArray | [Parcelable](arkts-ipc-rpc-parcelable-i.md)[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeRawData

```TypeScript
writeRawData(rawData: number[], size: number): void
```

Writes raw data to this **MessageSequence** object.

> **NOTE：**&gt;
> - This API cannot be called for multiple times in one parcel communication.&gt;
> - When the data volume is large (greater than 32 KB), the shared memory is used to transmit data. In this case,
> pay attention to the SELinux configuration.

**Since:** 9

**Deprecated since:** 11

**Substitutes:** [writeRawDataBuffer](#writerawdatabuffer)(rawData: ArrayBuffer, size: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rawData | number[] | Yes |
| size | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeRawDataBuffer

```TypeScript
writeRawDataBuffer(rawData: ArrayBuffer, size: number): void
```

Writes raw data to this **MessageSequence** object.

> **NOTE：**&gt;
> - This API cannot be called for multiple times in one parcel communication.&gt;
> - When the data volume is large (greater than 32 KB), the shared memory is used to transmit data. In this case,
> pay attention to the SELinux configuration.

**Since:** 11

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rawData | ArrayBuffer | Yes |
| size | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeRemoteObject

```TypeScript
writeRemoteObject(obj: IRemoteObject): void
```

Serializes the remote object and writes it to the [MessageSequence](#messagesequence) object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900008](../errorcode-rpc.md#1900008-invalid-ipc-object) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeRemoteObjectArray

```TypeScript
writeRemoteObjectArray(objectArray: IRemoteObject[]): void
```

Writes an **IRemoteObject** array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| objectArray | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeShort

```TypeScript
writeShort(val: number): void
```

Writes a short integer to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeShortArray

```TypeScript
writeShortArray(shortArray: number[]): void
```

Writes a short array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shortArray | number[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeString

```TypeScript
writeString(val: string): void
```

Writes a string to this **MessageSequence** object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |

## writeStringArray

```TypeScript
writeStringArray(stringArray: string[]): void
```

Writes a string array to this **MessageSequence** object.

**Since:** 9

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| stringArray | string[] | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1900009](../errorcode-rpc.md#1900009-failed-to-write-data-to-messagesequence) |
