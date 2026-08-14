# parse

## Modules to Import

```TypeScript
import { ArkTSUtils } from 'ArkTSUtils';
```

## parse

```TypeScript
function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null
```

Converts a JavaScript Object Notation (JSON) string into an ArkTS Value.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ASON-function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null--><!--Device-ASON-function parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | A valid JSON string. |
| reviver | Transformer | No | A function that transforms the results. |
| options | ParseOptions | No | The config of parse. |

**Return value:**

| Type | Description |
| --- | --- |
| ISendable | Return an ArkTS Value. |

