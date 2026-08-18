# Transformer

```TypeScript
type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null
```

用于转换结果的函数类型。 作为[JSON.parse](arkts-arkts-json-parse-f.md#parse)函数的参数时，解析结果中的每个键值对按深度优先顺序（从最内层节点开始，逐层向外）依次调用此函数， this指向当前键值对所属的对象，返回值替换原始值，若返回undefined则该属性将被删除。 作为[JSON.stringify](arkts-arkts-json-stringify-f.md#stringify)函数的参数时， 序列化引擎会按从外到内的顺序对每个属性调用该函数处理，this指向当前属性所属的对象，返回值作为序列化结果。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-json-type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null--><!--Device-json-type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| this | Object | 是 |
| key | string | 是 |
| value | Object | 是 |

**返回值：**

| 类型 |
| --- |
| Object \| undefined \| null |
