# ValueType

```TypeScript
type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint
```

表示支持的值类型。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-preferences-type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint--><!--Device-preferences-type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

| Type | Description |
| --- | --- |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符串。 |
| boolean | 表示值类型为布尔值。 |
| Array&lt;number&gt; | 表示值类型为数字类型的数组。 |
| Array&lt;string&gt; | 表示值类型为字符串类型的数组。 |
| Array&lt;boolean&gt; | 表示值类型为布尔类型的数组。 |
| Uint8Array | 表示值类型为8位无符号整型的数组。 [since 11] |
| object | 表示值类型为对象。 [since 12] |
| bigint | 表示值类型为任意精度格式的整数。 [since 12] |

