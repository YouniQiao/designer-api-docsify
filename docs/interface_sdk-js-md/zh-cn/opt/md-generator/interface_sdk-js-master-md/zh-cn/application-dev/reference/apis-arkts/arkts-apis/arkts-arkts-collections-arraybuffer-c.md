# ArrayBuffer

ArkTS TypedArray（[Int8Array](arkts-collections.md#@arkts.collections)、 [Uint8Array](arkts-collections.md#@arkts.collections)、 [Int16Array](arkts-collections.md#@arkts.collections)、 [Uint16Array](arkts-collections.md#@arkts.collections)、 [Int32Array](arkts-collections.md#@arkts.collections)、 [Uint32Array](arkts-collections.md#@arkts.collections)、 [Uint8ClampedArray](arkts-collections.md#@arkts.collections)、 [Float32Array](arkts-collections.md#@arkts.collections)）的底层数据结构。 > **说明：**> > - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。 > **装饰器类型**：\@Sendable

**起始版本：** 12

**废弃版本：** -1

<!--Device-collections-class ArrayBuffer--><!--Device-collections-class ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(byteLength: number)
```

构造函数，用于创建一个指定长度的ArkTS ArrayBuffer对象。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ArrayBuffer-constructor(byteLength: number)--><!--Device-ArrayBuffer-constructor(byteLength: number)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteLength](#byteLength) | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-构造函数调用异常) |

## slice

```TypeScript
slice(begin: number, end?: number): ArrayBuffer
```

返回一个新的ArkTS ArrayBuffer对象，其包含原ArkTS ArrayBuffer指定范围的内容。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer--><!--Device-ArrayBuffer-slice(begin: number, end?: number): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 否 |

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

**错误码：**

| 错误码ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-传入的thisobject不是容器类的实例) |
| [10200201](../errorcode-utils.md#10200201-concurrent修改错误) |

## byteLength

```TypeScript
readonly byteLength: number
```

buffer所占的字节数。

**类型：** number

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ArrayBuffer-readonly byteLength: number--><!--Device-ArrayBuffer-readonly byteLength: number-End-->

**系统能力：** SystemCapability.Utils.Lang
