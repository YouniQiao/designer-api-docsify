# parse

## Modules to Import

```TypeScript
import { JSON } from 'kits/@kit.ArkTS';
```

## parse

```TypeScript
function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null
```

解析JSON字符串生成ArkTS对象或null。解析过程中，每个键值对按从最内层到最外层的顺序依次经过reviver函数处理，返回值替换原始值；当传入ParseOptions指定BigIntMode时，符合条件的整数将被解析为BigInt；当入参字符串为'null'时返回null。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null--><!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 有效的JSON字符串，需符合JSON语法规范。 |
| reviver | [Transformer](arkts-arkts-ason-transformer-t.md) | No | 转换函数，用于修改解析生成的原始值；当需要对解析结果进行自定义转换时使用。默认值是undefined。 |
| options | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | No | 解析的配置选项，用于控制解析生成的类型。默认值是undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 当传入的字符串为'null'时，返回null。 |

