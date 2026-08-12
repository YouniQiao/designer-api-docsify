# attachId

## attachId

```TypeScript
function attachId(uri: string, id: number): string
```

Attaches the given ID to the end of the path component of the given uri.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [attachId](ohos.app.ability.dataUriUtils/dataUriUtils#attachId)

<!--Device-dataUriUtils-function attachId(uri: string, id: number): string--><!--Device-dataUriUtils-function attachId(uri: string, id: number): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = 1122;
let uri = dataUriUtils.attachId(
    'com.example.dataUriUtils',
	id,
);
```
