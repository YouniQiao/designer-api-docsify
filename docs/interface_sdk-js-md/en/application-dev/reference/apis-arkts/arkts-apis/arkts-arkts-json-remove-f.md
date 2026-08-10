# remove

## Modules to Import

```TypeScript
import { JSON } from 'kits/@kit.ArkTS';
```

## remove

```TypeScript
function remove(obj: object, property: string): void
```

从ArkTS对象中删除某种属性，可用于[JSON.parse](arkts-arkts-json-parse-f.md#parse)解析JSON字符串之后，如清理敏感字段、移除冗余数据等场景。JSON.remove接口仅支持最外层为字典形式（即大括号而非中括号包围）的合法JSON串。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function remove(obj: object, property: string): void--><!--Device-json-function remove(obj: object, property: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | object | Yes | ArkTS对象，仅支持最外层为字典形式（即大括号而非中括号包围）的合法JSON串解析后的对象。 |
| property | string | Yes | 要删除的属性名称，用于指定需从ArkTS对象中移除的属性。 |

