# parse

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'kits/@kit.ArkTS';
```

## parse

```TypeScript
function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null
```

用于解析JSON字符串生成ISendable数据或null。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ASON-function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null--><!--Device-ASON-function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 有效的JSON字符串。 |
| reviver | [Transformer](arkts-arkts-ason-transformer-t.md) | No | 转换函数，传入该参数，可以用来修改解析生成的原始值。默认值是undefined。该参数目前仅支持传入undefined值，其他值会被忽略或视为无效。 |
| options | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | No | 解析的配置，传入该参数，可以用来控制解析生成的结果类型。默认值是undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ISendable](../../apis-image-kit/arkts-apis/arkts-image-sendableimage-isendable-t.md) | 返回ISendable数据或null。入参为null时，返回null。 |

