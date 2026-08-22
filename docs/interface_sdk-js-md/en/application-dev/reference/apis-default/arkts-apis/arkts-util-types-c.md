# types

Check the type of parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-util-class types--><!--Device-util-class types-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

The types constructor

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-constructor()--><!--Device-types-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## isAnyArrayBuffer

```TypeScript
isAnyArrayBuffer(value: Object): boolean
```

Check whether the entered value is of arraybuffer or sharedarraybuffer type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isAnyArrayBuffer(value: Object): boolean--><!--Device-types-isAnyArrayBuffer(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A ArrayBuffer or SharedArrayBuffer value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in ArrayBuffer or SharedArrayBuffer instance. |

## isArrayBuffer

```TypeScript
isArrayBuffer(value: Object): boolean
```

Check whether the entered value is of arraybuffer type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isArrayBuffer(value: Object): boolean--><!--Device-types-isArrayBuffer(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A arraybuffer value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in ArrayBuffer instance. This does not include SharedArrayBuffer instances. Usually, it is desirable to test for both; See isAnyArrayBuffer() for that. |

## isArrayBufferView

```TypeScript
isArrayBufferView(value: Object): boolean
```

Check whether the type is included in the isAnyArrayBuffer.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isArrayBufferView(value: Object): boolean--><!--Device-types-isArrayBufferView(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A included in the isAnyArrayBuffer value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is an instance of one of the ArrayBuffer views, such as typed array objects or DataView. |

## isAsyncFunction

```TypeScript
isAsyncFunction(value: Object): boolean
```

Check whether the value entered is an asynchronous function type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isAsyncFunction(value: Object): boolean--><!--Device-types-isAsyncFunction(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A async function value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is an async function. This only reports back what the JavaScript engine is seeing; in particular, the return value may not match the original source code if a transpilation tool was used. |

## isBigInt64Array

```TypeScript
isBigInt64Array(value: Object): boolean
```

Check whether the entered value is of bigint64array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isBigInt64Array(value: Object): boolean--><!--Device-types-isBigInt64Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A BigInt64Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a BigInt64Array instance. |

## isBigUint64Array

```TypeScript
isBigUint64Array(value: Object): boolean
```

Check whether the entered value is of biguint64array array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isBigUint64Array(value: Object): boolean--><!--Device-types-isBigUint64Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A BigUint64Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a BigUint64Array instance. |

## isDataView

```TypeScript
isDataView(value: Object): boolean
```

Check whether the entered value is of DataView type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isDataView(value: Object): boolean--><!--Device-types-isDataView(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A DataView value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in DataView instance. |

## isDate

```TypeScript
isDate(value: Object): boolean
```

Check whether the entered value is of type date.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isDate(value: Object): boolean--><!--Device-types-isDate(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Date value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Date instance. |

## isFloat32Array

```TypeScript
isFloat32Array(value: Object): boolean
```

Check whether the entered value is of float32array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isFloat32Array(value: Object): boolean--><!--Device-types-isFloat32Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Float32Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Float32Array instance. |

## isFloat64Array

```TypeScript
isFloat64Array(value: Object): boolean
```

Check whether the entered value is of float64array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isFloat64Array(value: Object): boolean--><!--Device-types-isFloat64Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Float64Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Float64Array instance. |

## isInt16Array

```TypeScript
isInt16Array(value: Object): boolean
```

Check whether the entered value is the int16array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isInt16Array(value: Object): boolean--><!--Device-types-isInt16Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Int16Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Int16Array instance. |

## isInt32Array

```TypeScript
isInt32Array(value: Object): boolean
```

Check whether the entered value is the int32array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isInt32Array(value: Object): boolean--><!--Device-types-isInt32Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Int32Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Int32Array instance. |

## isInt8Array

```TypeScript
isInt8Array(value: Object): boolean
```

Check whether the entered value is of int8array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isInt8Array(value: Object): boolean--><!--Device-types-isInt8Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Int8Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Int8Array instance. |

## isMap

```TypeScript
isMap(value: Object): boolean
```

Check whether the entered value is of map type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isMap(value: Object): boolean--><!--Device-types-isMap(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Map value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Map instance. |

## isMapIterator

```TypeScript
isMapIterator(value: Object): boolean
```

Check whether the entered value is the iterator type of map.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isMapIterator(value: Object): boolean--><!--Device-types-isMapIterator(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Map iterator value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is an iterator returned for a built-in Map instance. |

## isNativeError

```TypeScript
isNativeError(value: Object): boolean
```

Check whether the value entered is of type error.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isNativeError(value: Object): boolean--><!--Device-types-isNativeError(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Error value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is an instance of a built-in Error type. |

## isPromise

```TypeScript
isPromise(value: Object): boolean
```

Check whether the entered value is of promise type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isPromise(value: Object): boolean--><!--Device-types-isPromise(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Promise value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Promise. |

## isRegExp

```TypeScript
isRegExp(value: Object): boolean
```

Check whether the entered value is of type regexp.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isRegExp(value: Object): boolean--><!--Device-types-isRegExp(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A regular expression object value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a regular expression object. |

## isSet

```TypeScript
isSet(value: Object): boolean
```

Check whether the entered value is of type set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isSet(value: Object): boolean--><!--Device-types-isSet(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Set instance value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Set instance. |

## isSetIterator

```TypeScript
isSetIterator(value: Object): boolean
```

Check whether the entered value is the iterator type of set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isSetIterator(value: Object): boolean--><!--Device-types-isSetIterator(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Set iterator value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is an iterator returned for a built-in Set instance. |

## isTypedArray

```TypeScript
isTypedArray(value: Object): boolean
```

Check whether the entered value is a type contained in typedarray.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isTypedArray(value: Object): boolean--><!--Device-types-isTypedArray(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A TypedArray instance value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in TypedArray instance. |

## isUint16Array

```TypeScript
isUint16Array(value: Object): boolean
```

Check whether the entered value is the uint16array array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isUint16Array(value: Object): boolean--><!--Device-types-isUint16Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Uint16Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Uint16Array instance. |

## isUint32Array

```TypeScript
isUint32Array(value: Object): boolean
```

Check whether the entered value is the uint32array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isUint32Array(value: Object): boolean--><!--Device-types-isUint32Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Uint32Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Uint32Array instance. |

## isUint8Array

```TypeScript
isUint8Array(value: Object): boolean
```

Check whether the entered value is the uint8array array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isUint8Array(value: Object): boolean--><!--Device-types-isUint8Array(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Uint8Array value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Uint8Array instance. |

## isUint8ClampedArray

```TypeScript
isUint8ClampedArray(value: Object): boolean
```

Check whether the entered value is the uint8clapedarray array type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isUint8ClampedArray(value: Object): boolean--><!--Device-types-isUint8ClampedArray(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A Uint8ClampedArray value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in Uint8ClampedArray instance. |

## isWeakMap

```TypeScript
isWeakMap(value: Object): boolean
```

Check whether the entered value is of type weakmap.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isWeakMap(value: Object): boolean--><!--Device-types-isWeakMap(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A WeakMap value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in WeakMap instance. |

## isWeakSet

```TypeScript
isWeakSet(value: Object): boolean
```

Check whether the entered value is of type weakset.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-types-isWeakSet(value: Object): boolean--><!--Device-types-isWeakSet(value: Object): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Object | Yes | A WeakSet value |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the value is a built-in WeakSet instance. |

