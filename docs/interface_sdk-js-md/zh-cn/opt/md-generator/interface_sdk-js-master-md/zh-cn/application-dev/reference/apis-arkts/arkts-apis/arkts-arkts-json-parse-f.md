# parse

## parse

```TypeScript
function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null
```

解析JSON字符串生成ArkTS对象或null。解析过程中，每个键值对按从最内层到最外层的顺序依次经过reviver函数处理，返回值替换原始值； 当传入ParseOptions指定BigIntMode时，符合条件的整数将被解析为BigInt；当入参字符串为'null'时返回null。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null--><!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| reviver | [Transformer](arkts-arkts-ason-transformer-t.md) | 否 |
| options | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Object |
