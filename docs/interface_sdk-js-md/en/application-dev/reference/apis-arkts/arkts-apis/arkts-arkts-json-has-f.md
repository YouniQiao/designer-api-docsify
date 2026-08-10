# has

## Modules to Import

```TypeScript
import { JSON } from 'kits/@kit.ArkTS';
```

## has

```TypeScript
function has(obj: object, property: string): boolean
```

检查ArkTS对象是否包含某种属性，可用于[JSON.parse](arkts-arkts-json-parse-f.md#parse)解析JSON字符串之后。has接口仅支持最外层为字典形式（即大括号而非中括号包围）的合法JSON串，传入非字典形式的对象时无法正确判断属性是否存在。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function has(obj: object, property: string): boolean--><!--Device-json-function has(obj: object, property: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | object | Yes | ArkTS对象，仅支持最外层为字典形式（即大括号而非中括号包围）的合法JSON串解析后的对象。 |
| property | string | Yes | 要检查的属性名称，用于指定需在ArkTS对象中查找是否存在的属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回ArkTS对象是否包含指定属性的结果。true表示对象包含指定属性；false表示对象不包含指定属性。 |

