# TypeCode

```TypeScript
enum TypeCode
```

Since API version 12, [writeArrayBuffer](arkts-ipc-rpc-messagesequence-c.md#writearraybuffer) and [readArrayBuffer](arkts-ipc-rpc-messagesequence-c.md#readarraybuffer) are added to pass ArrayBuffer data. The specific TypedArray type is determined by the **TypeCode** defined as follows.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## INT8_ARRAY

```TypeScript
INT8_ARRAY = 0
```

The TypedArray type is INT8_ARRAY. Data is read and written in 8-bit signed integer format, with each element occupying 1 byte.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## UINT8_ARRAY

```TypeScript
UINT8_ARRAY = 1
```

The TypedArray type is UINT8_ARRAY. Data is read and written in 8-bit unsigned integer format, with each element occupying 1 byte.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## INT16_ARRAY

```TypeScript
INT16_ARRAY = 2
```

The TypedArray type is INT16_ARRAY. Data is read and written in 16-bit signed integer format, with each element occupying 2 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## UINT16_ARRAY

```TypeScript
UINT16_ARRAY = 3
```

The TypedArray type is UINT16_ARRAY. Data is read and written in 16-bit unsigned integer format, with each element occupying 2 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## INT32_ARRAY

```TypeScript
INT32_ARRAY = 4
```

The TypedArray type is INT32_ARRAY. Data is read and written in 32-bit signed integer format, with each element occupying 4 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## UINT32_ARRAY

```TypeScript
UINT32_ARRAY = 5
```

The TypedArray type is UINT32_ARRAY. Data is read and written in 32-bit unsigned integer format, with each element occupying 4 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## FLOAT32_ARRAY

```TypeScript
FLOAT32_ARRAY = 6
```

The TypedArray type is FLOAT32_ARRAY. Data is read and written in 32-bit single-precision floating-point format, with each element occupying 4 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## FLOAT64_ARRAY

```TypeScript
FLOAT64_ARRAY = 7
```

The TypedArray type is FLOAT64_ARRAY. Data is read and written in 64-bit double-precision floating-point format, with each element occupying 8 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## BIGINT64_ARRAY

```TypeScript
BIGINT64_ARRAY = 8
```

The TypedArray type is BIGINT64_ARRAY. Data is read and written in 64-bit big integer format, with each element occupying 8 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core

## BIGUINT64_ARRAY

```TypeScript
BIGUINT64_ARRAY = 9
```

The TypedArray type is BIGUINT64_ARRAY. Data is read and written in 64-bit unsigned big integer format, with each element occupying 8 bytes.

**Since:** 12

**System capability:** SystemCapability.Communication.IPC.Core
