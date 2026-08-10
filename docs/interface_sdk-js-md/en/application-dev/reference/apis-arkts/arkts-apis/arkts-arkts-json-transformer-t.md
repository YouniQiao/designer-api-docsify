# Transformer

```TypeScript
type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null
```

用于转换结果的函数类型。作为[JSON.parse](arkts-arkts-json-parse-f.md#parse)函数的参数时，解析结果中的每个键值对按深度优先顺序（从最内层节点开始，逐层向外）依次调用此函数，this指向当前键值对所属的对象，返回值替换原始值，若返回undefined则该属性将被删除。作为[JSON.stringify](arkts-arkts-json-stringify-f.md#stringify)函数的参数时，序列化引擎会按从外到内的顺序对每个属性调用该函数处理，this指向当前属性所属的对象，返回值作为序列化结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null--><!--Device-json-type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| this | Object | Yes | 正在解析或序列化的键值对所属的对象。 |
| key | string | Yes | 当前正在处理的对象成员的属性名，用于在转换函数中识别所解析或序列化的键。 |
| value | Object | Yes | 正在解析或序列化的键值对的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object \| undefined \| null | 返回转换处理后的属性值；返回undefined时，该属性在结果中被移除；返回null时，该属性值设为null。 |

