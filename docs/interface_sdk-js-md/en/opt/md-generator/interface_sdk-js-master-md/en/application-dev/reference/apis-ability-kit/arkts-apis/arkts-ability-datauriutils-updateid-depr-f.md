# updateId

## updateId

```TypeScript
function updateId(uri: string, id: number): string
```

Updates the ID in the specified uri

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [updateId](arkts-ability-datauriutils-updateid-f.md#updateId)

<!--Device-dataUriUtils-function updateId(uri: string, id: number): string--><!--Device-dataUriUtils-function updateId(uri: string, id: number): string-End-->

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
let uri = dataUriUtils.updateId(
    'com.example.dataUriUtils/1221',
	id
);
```
