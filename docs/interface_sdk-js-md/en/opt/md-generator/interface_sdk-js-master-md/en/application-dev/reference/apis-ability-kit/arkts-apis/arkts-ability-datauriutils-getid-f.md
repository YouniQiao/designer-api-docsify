# getId

## Modules to Import

```TypeScript
import { dataUriUtils } from 'kits/@kit.AbilityKit';
```

## getId

```TypeScript
function getId(uri: string): number
```

Obtains the ID attached to the end of a given URI.

**Since:** 9

<!--Device-dataUriUtils-function getId(uri: string): double--><!--Device-dataUriUtils-function getId(uri: string): double-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';

try {
  let id = dataUriUtils.getId('com.example.dataUriUtils/1221');
  console.info(`get id: ${id}`);
} catch(err) {
  console.error(`get id err ,check the uri ${err}`);
}
```
