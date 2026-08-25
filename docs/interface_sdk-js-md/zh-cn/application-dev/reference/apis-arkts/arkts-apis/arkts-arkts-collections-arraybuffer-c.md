# ArrayBuffer

ArkTS TypedArray（[Int8Array](arkts-arkts-collections-int8array-c.md)、 [Uint8Array](arkts-arkts-collections-uint8array-c.md)、 [Int16Array](arkts-arkts-collections-int16array-c.md)、 [Uint16Array](arkts-arkts-collections-uint16array-c.md)、 [Int32Array](arkts-arkts-collections-int32array-c.md)、 [Uint32Array](arkts-arkts-collections-uint32array-c.md)、 [Uint8ClampedArray](arkts-arkts-collections-uint8clampedarray-c.md)、 [Float32Array](arkts-arkts-collections-float32array-c.md)）的底层数据结构。

> **说明：**&gt;
> - 此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。
> **装饰器类型**：\@Sendable

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { collections } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(byteLength: number)
```

构造函数，用于创建一个指定长度的ArkTS ArrayBuffer对象。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [byteLength](#bytelength) | number | 是 |

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

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

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

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang
