# stringify

## Modules to Import

```TypeScript
import { JSON } from '@kit.ArkTS';
```

## stringify

```TypeScript
function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string
```

Converts an ArkTS object or array into a JSON string. In the case of a container, linear containers are supported, but non-linear containers are not.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string--><!--Device-json-function stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Object | Yes |
| replacer | (number \| string)[] \| null | No |
| space | string \| number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |


## stringify

```TypeScript
function stringify(value: Object, replacer?: Transformer, space?: string | number): string
```

Converts an ArkTS object or array into a JSON string. In the case of a container, linear containers are supported, but non-linear containers are not.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function stringify(value: Object, replacer?: Transformer, space?: string | number): string--><!--Device-json-function stringify(value: Object, replacer?: Transformer, space?: string | number): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Object | Yes |
| replacer | [Transformer](arkts-arkts-ason-transformer-t.md) | No |
| space | string \| number | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |
