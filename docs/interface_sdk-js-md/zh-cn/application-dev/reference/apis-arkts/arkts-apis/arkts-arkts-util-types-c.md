# types

提供检查不同内置对象类型的 API，例如 ArrayBuffer、Map 和 Set，以避免类型错误导致的异常。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor()
```

用于创建 **Types** 对象的构造函数。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## isAnyArrayBuffer

```TypeScript
isAnyArrayBuffer(value: Object): boolean
```

判断入参是否为 ArrayBuffer 或 SharedArrayBuffer 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isArgumentsObject

```TypeScript
isArgumentsObject(value: Object): boolean
```

判断入参是否为 **arguments** 对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isArrayBuffer

```TypeScript
isArrayBuffer(value: Object): boolean
```

判断入参是否为 ArrayBuffer 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isArrayBufferView

```TypeScript
isArrayBufferView(value: Object): boolean
```

判断入参是否为 ArrayBufferView 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isAsyncFunction

```TypeScript
isAsyncFunction(value: Object): boolean
```

判断入参是否为异步函数。

> **说明：**&gt;
> 该接口无法对AsyncGenerator Function进行有效判断，建议通过获取函数的constructor.name属性与'AsyncGeneratorFunction'做判等的方式替代。&gt;
> 该接口无法对Sendable class中的async成员函数进行有效判断，无替代方案。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isBigInt64Array

```TypeScript
isBigInt64Array(value: Object): boolean
```

判断入参是否为 BigInt64Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isBigUint64Array

```TypeScript
isBigUint64Array(value: Object): boolean
```

判断入参是否为 BigUint64Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isBooleanObject

```TypeScript
isBooleanObject(value: Object): boolean
```

判断入参是否为 Boolean 类型。

> **NOTE：**&gt;
> 本接口从 API version 8 起支持，从 API version 14 起废弃。无替代接口。

**起始版本：** 8

**废弃版本：** 14

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isBoxedPrimitive

```TypeScript
isBoxedPrimitive(value: Object): boolean
```

判断入参是否为 Boolean、Number、String 或 Symbol 类型。

> **NOTE：**&gt;
> 本接口从 API version 8 起支持，从 API version 14 起废弃。无替代接口。

**起始版本：** 8

**废弃版本：** 14

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isDataView

```TypeScript
isDataView(value: Object): boolean
```

判断入参是否为 DataView 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isDate

```TypeScript
isDate(value: Object): boolean
```

判断入参是否为 Date 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isExternal

```TypeScript
isExternal(value: Object): boolean
```

判断入参是否为 native external 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isFloat32Array

```TypeScript
isFloat32Array(value: Object): boolean
```

判断入参是否为 Float32Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isFloat64Array

```TypeScript
isFloat64Array(value: Object): boolean
```

判断入参是否为 Float64Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isGeneratorFunction

```TypeScript
isGeneratorFunction(value: Object): boolean
```

判断入参是否为 generator 函数。

> **说明：**&gt;
> 该接口无法对AsyncGenerator Function进行有效判断，建议通过获取函数的constructor.name属性与'AsyncGeneratorFunction'做判等的方式替代。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isGeneratorObject

```TypeScript
isGeneratorObject(value: Object): boolean
```

判断入参是否为 generator 对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInt16Array

```TypeScript
isInt16Array(value: Object): boolean
```

判断入参是否为 Int16Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInt32Array

```TypeScript
isInt32Array(value: Object): boolean
```

判断入参是否为 Int32Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isInt8Array

```TypeScript
isInt8Array(value: Object): boolean
```

判断入参是否为 Int8Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isMap

```TypeScript
isMap(value: Object): boolean
```

判断入参是否为 Map 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isMapIterator

```TypeScript
isMapIterator(value: Object): boolean
```

判断入参是否为 MapIterator 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isModuleNamespaceObject

```TypeScript
isModuleNamespaceObject(value: Object): boolean
```

判断入参是否为模块命名空间对象。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isNativeError

```TypeScript
isNativeError(value: Object): boolean
```

判断入参是否为 Error 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isNumberObject

```TypeScript
isNumberObject(value: Object): boolean
```

判断入参是否为 Number 类型。

> **NOTE：**&gt;
> 本接口从 API version 8 起支持，从 API version 14 起废弃。无替代接口。

**起始版本：** 8

**废弃版本：** 14

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isPromise

```TypeScript
isPromise(value: Object): boolean
```

判断入参是否为 promise。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isProxy

```TypeScript
isProxy(value: Object): boolean
```

判断入参是否为 proxy。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isRegExp

```TypeScript
isRegExp(value: Object): boolean
```

判断入参是否为 RegExp 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isSet

```TypeScript
isSet(value: Object): boolean
```

判断入参是否为 Set 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isSetIterator

```TypeScript
isSetIterator(value: Object): boolean
```

判断入参是否为 SetIterator 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isSharedArrayBuffer

```TypeScript
isSharedArrayBuffer(value: Object): boolean
```

判断入参是否为 SharedArrayBuffer 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isStringObject

```TypeScript
isStringObject(value: Object): boolean
```

判断入参是否为字符串对象。

> **NOTE：**&gt;
> 本接口从 API version 8 起支持，从 API version 14 起废弃。无替代接口。

**起始版本：** 8

**废弃版本：** 14

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isSymbolObject

```TypeScript
isSymbolObject(value: Object): boolean
```

判断入参是否为 symbol 对象。

> **NOTE：**&gt;
> 本接口从 API version 8 起支持，从 API version 14 起废弃。无替代接口。

**起始版本：** 8

**废弃版本：** 14

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isTypedArray

```TypeScript
isTypedArray(value: Object): boolean
```

判断入参是否为 TypedArray 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUint16Array

```TypeScript
isUint16Array(value: Object): boolean
```

判断入参是否为 Uint16Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUint32Array

```TypeScript
isUint32Array(value: Object): boolean
```

判断入参是否为 Uint32Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUint8Array

```TypeScript
isUint8Array(value: Object): boolean
```

判断入参是否为 Uint8Array 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isUint8ClampedArray

```TypeScript
isUint8ClampedArray(value: Object): boolean
```

判断入参是否为 Uint8ClampedArray 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isWeakMap

```TypeScript
isWeakMap(value: Object): boolean
```

判断入参是否为 WeakMap 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isWeakSet

```TypeScript
isWeakSet(value: Object): boolean
```

判断入参是否为 WeakSet 类型。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
