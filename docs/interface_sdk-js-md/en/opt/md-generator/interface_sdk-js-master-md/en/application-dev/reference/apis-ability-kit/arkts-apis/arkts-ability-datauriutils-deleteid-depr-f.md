# deleteId

## deleteId

```TypeScript
function deleteId(uri: string): string
```

Deletes the ID from the end of the path component of the given uri.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [deleteId](ohos.app.ability.dataUriUtils/dataUriUtils#deleteId)

<!--Device-dataUriUtils-function deleteId(uri: string): string--><!--Device-dataUriUtils-function deleteId(uri: string): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import dataUriUtils from '@ohos.ability.dataUriUtils';

let uri = dataUriUtils.deleteId('com.example.dataUriUtils/1221');
```
