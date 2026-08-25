# MessageParcel

Provides APIs for reading and writing data in specific format. During RPC, the sender can use the **write()** method provided by **MessageParcel** to write data in specific format to a **MessageParcel** object. The receiver can use the **read()** method provided by **MessageParcel** to read data in specific format from a **MessageParcel** object. The data formats include basic data types and arrays, IPC objects, interface tokens, and custom sequenceable objects.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [MessageSequence](arkts-ipc-rpc-messagesequence-c.md)

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [closeFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#closefiledescriptor)(fd: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

## containFileDescriptors

```TypeScript
containFileDescriptors(): boolean
```

Checks whether this **MessageParcel** object contains file descriptors.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [containFileDescriptors](arkts-ipc-rpc-messagesequence-c.md#containfiledescriptors)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## create

```TypeScript
static create(): MessageParcel
```

Creates a **MessageParcel** object. This method is a static method.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [create](arkts-ipc-rpc-messagesequence-c.md#create)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MessageParcel](arkts-ipc-rpc-messageparcel-c.md) |

## dupFileDescriptor

```TypeScript
static dupFileDescriptor(fd: number): number
```

Duplicates a file descriptor. This API is a static method.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [dupFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#dupfiledescriptor)(fd: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCapacity

```TypeScript
getCapacity(): number
```

Obtains the capacity of this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getCapacity](arkts-ipc-rpc-messagesequence-c.md#getcapacity)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getRawDataCapacity

```TypeScript
getRawDataCapacity(): number
```

Obtains the maximum amount of raw data that can be held by this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRawDataCapacity](arkts-ipc-rpc-messagesequence-c.md#getrawdatacapacity)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReadableBytes

```TypeScript
getReadableBytes(): number
```

Obtains the readable capacity of this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getReadableBytes](arkts-ipc-rpc-messagesequence-c.md#getreadablebytes)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getReadPosition

```TypeScript
getReadPosition(): number
```

Obtains the read position of this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getReadPosition](arkts-ipc-rpc-messagesequence-c.md#getreadposition)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getSize

```TypeScript
getSize(): number
```

Obtains the data size of this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getSize](arkts-ipc-rpc-messagesequence-c.md#getsize)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWritableBytes

```TypeScript
getWritableBytes(): number
```

Obtains the writable capacity of this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getWritableBytes](arkts-ipc-rpc-messagesequence-c.md#getwritablebytes)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWritePosition

```TypeScript
getWritePosition(): number
```

Obtains the write position of this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getWritePosition](arkts-ipc-rpc-messagesequence-c.md#getwriteposition)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readAshmem

```TypeScript
readAshmem(): Ashmem
```

Reads the anonymous shared object from this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readAshmem](arkts-ipc-rpc-messagesequence-c.md#readashmem)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Ashmem](arkts-ipc-rpc-ashmem-c.md) |

## readBoolean

```TypeScript
readBoolean(): boolean
```

Reads the Boolean value from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readBoolean](arkts-ipc-rpc-messagesequence-c.md#readboolean)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## readBooleanArray

```TypeScript
readBooleanArray(dataIn: boolean[]): void
```

Reads the Boolean array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readBooleanArray](arkts-ipc-rpc-messagesequence-c.md#readbooleanarray)(dataIn: boolean[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | boolean[] | Yes |

## readBooleanArray

```TypeScript
readBooleanArray(): boolean[]
```

Reads the Boolean array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readBooleanArray](arkts-ipc-rpc-messagesequence-c.md#readbooleanarray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean[] |

## readByte

```TypeScript
readByte(): number
```

Reads the byte value from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readByte](arkts-ipc-rpc-messagesequence-c.md#readbyte)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readByteArray

```TypeScript
readByteArray(dataIn: number[]): void
```

Reads the byte array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readByteArray](arkts-ipc-rpc-messagesequence-c.md#readbytearray)(dataIn: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

## readByteArray

```TypeScript
readByteArray(): number[]
```

Reads the byte array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readByteArray](arkts-ipc-rpc-messagesequence-c.md#readbytearray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readChar

```TypeScript
readChar(): number
```

Reads the single character value from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readChar](arkts-ipc-rpc-messagesequence-c.md#readchar)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readCharArray

```TypeScript
readCharArray(dataIn: number[]): void
```

Reads the character array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readCharArray](arkts-ipc-rpc-messagesequence-c.md#readchararray)(dataIn: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

## readCharArray

```TypeScript
readCharArray(): number[]
```

Reads the single character array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readCharArray](arkts-ipc-rpc-messagesequence-c.md#readchararray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readDouble

```TypeScript
readDouble(): number
```

Reads the number value from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readDouble](arkts-ipc-rpc-messagesequence-c.md#readdouble)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readDoubleArray

```TypeScript
readDoubleArray(dataIn: number[]): void
```

Reads the number array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readDoubleArray](arkts-ipc-rpc-messagesequence-c.md#readdoublearray)(dataIn: double[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

## readDoubleArray

```TypeScript
readDoubleArray(): number[]
```

Reads the number array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readDoubleArray](arkts-ipc-rpc-messagesequence-c.md#readdoublearray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readException

```TypeScript
readException(): void
```

Reads the exception information from this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readException](arkts-ipc-rpc-messagesequence-c.md#readexception)()

**System capability:** SystemCapability.Communication.IPC.Core

## readFileDescriptor

```TypeScript
readFileDescriptor(): number
```

Reads the file descriptor from this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#readfiledescriptor)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readFloat

```TypeScript
readFloat(): number
```

Reads the number value from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readFloat](arkts-ipc-rpc-messagesequence-c.md#readfloat)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readFloatArray

```TypeScript
readFloatArray(dataIn: number[]): void
```

Reads the number array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readFloatArray](arkts-ipc-rpc-messagesequence-c.md#readfloatarray)(dataIn: double[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

## readFloatArray

```TypeScript
readFloatArray(): number[]
```

Reads the number array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readFloatArray](arkts-ipc-rpc-messagesequence-c.md#readfloatarray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readInt

```TypeScript
readInt(): number
```

Reads the integer from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readInt](arkts-ipc-rpc-messagesequence-c.md#readint)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readIntArray

```TypeScript
readIntArray(dataIn: number[]): void
```

Reads the integer array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readIntArray](arkts-ipc-rpc-messagesequence-c.md#readintarray)(dataIn: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

## readIntArray

```TypeScript
readIntArray(): number[]
```

Reads the integer array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readIntArray](arkts-ipc-rpc-messagesequence-c.md#readintarray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readInterfaceToken

```TypeScript
readInterfaceToken(): string
```

Reads the interface token from this **MessageParcel** object. The interface token is read in the sequence in which it is written to the **MessageParcel** object. The local object can use it to verify the communication.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readInterfaceToken](arkts-ipc-rpc-messagesequence-c.md#readinterfacetoken)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## readLong

```TypeScript
readLong(): number
```

Reads the number number value from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readLong](arkts-ipc-rpc-messagesequence-c.md#readlong)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readLongArray

```TypeScript
readLongArray(dataIn: number[]): void
```

Reads the number array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readLongArray](arkts-ipc-rpc-messagesequence-c.md#readlongarray)(dataIn: long[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

## readLongArray

```TypeScript
readLongArray(): number[]
```

Reads the number array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readLongArray](arkts-ipc-rpc-messagesequence-c.md#readlongarray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readRawData

```TypeScript
readRawData(size: number): number[]
```

Reads raw data from this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readRawDataBuffer](arkts-ipc-rpc-messagesequence-c.md#readrawdatabuffer)(size: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readRemoteObject

```TypeScript
readRemoteObject(): IRemoteObject
```

Reads the remote object from this **MessageParcel** object. You can use this method to deserialize the **MessageParcel** object to generate an **IRemoteObject**. The remote objects are read in the order in which they are written to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readRemoteObject](arkts-ipc-rpc-messagesequence-c.md#readremoteobject)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(objects: IRemoteObject[]): void
```

Reads the **IRemoteObject** array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#readremoteobjectarray)(objects: IRemoteObject[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| objects | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | Yes |

## readRemoteObjectArray

```TypeScript
readRemoteObjectArray(): IRemoteObject[]
```

Reads the **IRemoteObject** array from this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#readremoteobjectarray)(objects: IRemoteObject[])

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] |

## readSequenceable

```TypeScript
readSequenceable(dataIn: Sequenceable): boolean
```

Reads member variables from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readParcelable](arkts-ipc-rpc-messagesequence-c.md#readparcelable)(dataIn: Parcelable)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## readSequenceableArray

```TypeScript
readSequenceableArray(sequenceableArray: Sequenceable[]): void
```

Reads the **Sequenceable** array from this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [readParcelableArray](arkts-ipc-rpc-messagesequence-c.md#readparcelablearray)(parcelableArray: Parcelable[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sequenceableArray | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md)[] | Yes |

## readShort

```TypeScript
readShort(): number
```

Reads the short integer from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readShort](arkts-ipc-rpc-messagesequence-c.md#readshort)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## readShortArray

```TypeScript
readShortArray(dataIn: number[]): void
```

Reads the short array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readShortArray](arkts-ipc-rpc-messagesequence-c.md#readshortarray)(dataIn: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | number[] | Yes |

## readShortArray

```TypeScript
readShortArray(): number[]
```

Reads the short array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readShortArray](arkts-ipc-rpc-messagesequence-c.md#readshortarray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number[] |

## readString

```TypeScript
readString(): string
```

Reads the string from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readString](arkts-ipc-rpc-messagesequence-c.md#readstring)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## readStringArray

```TypeScript
readStringArray(dataIn: string[]): void
```

Reads the string array from this **MessageParcel** object and writes it to the created empty array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readStringArray](arkts-ipc-rpc-messagesequence-c.md#readstringarray)(dataIn: string[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataIn | string[] | Yes |

## readStringArray

```TypeScript
readStringArray(): string[]
```

Reads the string array from this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [readStringArray](arkts-ipc-rpc-messagesequence-c.md#readstringarray)()

**System capability:** SystemCapability.Communication.IPC.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## reclaim

```TypeScript
reclaim(): void
```

Reclaims the **MessageParcel** object that is no longer used.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [reclaim](arkts-ipc-rpc-messagesequence-c.md#reclaim)()

**System capability:** SystemCapability.Communication.IPC.Core

## rewindRead

```TypeScript
rewindRead(pos: number): boolean
```

Moves the read pointer to the specified position.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [rewindRead](arkts-ipc-rpc-messagesequence-c.md#rewindread)(pos: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## rewindWrite

```TypeScript
rewindWrite(pos: number): boolean
```

Moves the write pointer to the specified position.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [rewindWrite](arkts-ipc-rpc-messagesequence-c.md#rewindwrite)(pos: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setCapacity

```TypeScript
setCapacity(size: number): boolean
```

Sets the storage capacity of this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setCapacity](arkts-ipc-rpc-messagesequence-c.md#setcapacity)(size: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setSize

```TypeScript
setSize(size: number): boolean
```

Sets the size of data contained in this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [setSize](arkts-ipc-rpc-messagesequence-c.md#setsize)(size: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeAshmem

```TypeScript
writeAshmem(ashmem: Ashmem): boolean
```

Writes an anonymous shared object to this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [writeAshmem](arkts-ipc-rpc-messagesequence-c.md#writeashmem)(ashmem: Ashmem)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ashmem | [Ashmem](arkts-ipc-rpc-ashmem-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeBoolean

```TypeScript
writeBoolean(val: boolean): boolean
```

Writes a Boolean value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeBoolean](arkts-ipc-rpc-messagesequence-c.md#writeboolean)(val: boolean)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeBooleanArray

```TypeScript
writeBooleanArray(booleanArray: boolean[]): boolean
```

Writes a Boolean array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeBooleanArray](arkts-ipc-rpc-messagesequence-c.md#writebooleanarray)(booleanArray: boolean[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| booleanArray | boolean[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeByte

```TypeScript
writeByte(val: number): boolean
```

Writes a Byte value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeByte](arkts-ipc-rpc-messagesequence-c.md#writebyte)(val: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeByteArray

```TypeScript
writeByteArray(byteArray: number[]): boolean
```

Writes a byte array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeByteArray](arkts-ipc-rpc-messagesequence-c.md#writebytearray)(byteArray: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| byteArray | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeChar

```TypeScript
writeChar(val: number): boolean
```

Writes a single character value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeChar](arkts-ipc-rpc-messagesequence-c.md#writechar)(val: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeCharArray

```TypeScript
writeCharArray(charArray: number[]): boolean
```

Writes a single character array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeCharArray](arkts-ipc-rpc-messagesequence-c.md#writechararray)(charArray: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| charArray | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeDouble

```TypeScript
writeDouble(val: number): boolean
```

Writes a number value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeDouble](arkts-ipc-rpc-messagesequence-c.md#writedouble)(val: double)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeDoubleArray

```TypeScript
writeDoubleArray(doubleArray: number[]): boolean
```

Writes a number array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeDoubleArray](arkts-ipc-rpc-messagesequence-c.md#writedoublearray)(doubleArray: double[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| doubleArray | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeFileDescriptor

```TypeScript
writeFileDescriptor(fd: number): boolean
```

Writes a file descriptor to this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [writeFileDescriptor](arkts-ipc-rpc-messagesequence-c.md#writefiledescriptor)(fd: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeFloat

```TypeScript
writeFloat(val: number): boolean
```

Writes a number value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeFloat](arkts-ipc-rpc-messagesequence-c.md#writefloat)(val: double)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeFloatArray

```TypeScript
writeFloatArray(floatArray: number[]): boolean
```

Writes a number array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeFloatArray](arkts-ipc-rpc-messagesequence-c.md#writefloatarray)(floatArray: double[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| floatArray | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeInt

```TypeScript
writeInt(val: number): boolean
```

Writes an number value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeInt](arkts-ipc-rpc-messagesequence-c.md#writeint)(val: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeIntArray

```TypeScript
writeIntArray(intArray: number[]): boolean
```

Writes an integer array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeIntArray](arkts-ipc-rpc-messagesequence-c.md#writeintarray)(intArray: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| intArray | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeInterfaceToken

```TypeScript
writeInterfaceToken(token: string): boolean
```

Writes an interface token to this **MessageParcel** object. The remote object can use this interface token to verify the communication.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeInterfaceToken](arkts-ipc-rpc-messagesequence-c.md#writeinterfacetoken)(token: string)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeLong

```TypeScript
writeLong(val: number): boolean
```

Writes a number number value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeLong](arkts-ipc-rpc-messagesequence-c.md#writelong)(val: long)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeLongArray

```TypeScript
writeLongArray(longArray: number[]): boolean
```

Writes a number array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeLongArray](arkts-ipc-rpc-messagesequence-c.md#writelongarray)(longArray: long[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| longArray | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeNoException

```TypeScript
writeNoException(): void
```

Writes information to this **MessageParcel** object indicating that no exception occurred.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [writeNoException](arkts-ipc-rpc-messagesequence-c.md#writenoexception)()

**System capability:** SystemCapability.Communication.IPC.Core

## writeRawData

```TypeScript
writeRawData(rawData: number[], size: number): boolean
```

Writes raw data to this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [writeRawDataBuffer](arkts-ipc-rpc-messagesequence-c.md#writerawdatabuffer)(rawData: ArrayBuffer, size: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rawData | number[] | Yes |
| size | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeRemoteObject

```TypeScript
writeRemoteObject(object: IRemoteObject): boolean
```

Serializes a remote object and writes it to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeRemoteObject](arkts-ipc-rpc-messagesequence-c.md#writeremoteobject)(obj: IRemoteObject)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| object | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeRemoteObjectArray

```TypeScript
writeRemoteObjectArray(objectArray: IRemoteObject[]): boolean
```

Writes an **IRemoteObject** array to this **MessageParcel** object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [writeRemoteObjectArray](arkts-ipc-rpc-messagesequence-c.md#writeremoteobjectarray)(objectArray: IRemoteObject[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| objectArray | [IRemoteObject](arkts-ipc-rpc-iremoteobject-c.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeSequenceable

```TypeScript
writeSequenceable(val: Sequenceable): boolean
```

Writes a **Sequenceable** object to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeParcelable](arkts-ipc-rpc-messagesequence-c.md#writeparcelable)(val: Parcelable)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeSequenceableArray

```TypeScript
writeSequenceableArray(sequenceableArray: Sequenceable[]): boolean
```

Writes a **Sequenceable** array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeParcelableArray](arkts-ipc-rpc-messagesequence-c.md#writeparcelablearray)(parcelableArray: Parcelable[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sequenceableArray | [Sequenceable](arkts-ipc-rpc-sequenceable-i.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeShort

```TypeScript
writeShort(val: number): boolean
```

Writes a short number value to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeShort](arkts-ipc-rpc-messagesequence-c.md#writeshort)(val: int)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeShortArray

```TypeScript
writeShortArray(shortArray: number[]): boolean
```

Writes a short array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeShortArray](arkts-ipc-rpc-messagesequence-c.md#writeshortarray)(shortArray: int[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shortArray | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeString

```TypeScript
writeString(val: string): boolean
```

Writes a string to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeString](arkts-ipc-rpc-messagesequence-c.md#writestring)(val: string)

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| val | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## writeStringArray

```TypeScript
writeStringArray(stringArray: string[]): boolean
```

Writes a string array to this **MessageParcel** object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [writeStringArray](arkts-ipc-rpc-messagesequence-c.md#writestringarray)(stringArray: string[])

**System capability:** SystemCapability.Communication.IPC.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| stringArray | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
