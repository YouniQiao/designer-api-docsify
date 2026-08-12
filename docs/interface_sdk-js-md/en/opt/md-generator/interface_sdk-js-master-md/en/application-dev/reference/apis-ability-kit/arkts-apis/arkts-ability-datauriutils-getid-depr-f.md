# getId

## getId

```TypeScript
function getId(uri: string): number
```

Obtains the ID attached to the end of the path component of the given uri.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getId](ohos.app.ability.dataUriUtils/dataUriUtils#getId)

<!--Device-dataUriUtils-function getId(uri: string): number--><!--Device-dataUriUtils-function getId(uri: string): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
import dataUriUtils from '@ohos.ability.dataUriUtils';

let id = dataUriUtils.getId('com.example.dataUriUtils/1221');
```
