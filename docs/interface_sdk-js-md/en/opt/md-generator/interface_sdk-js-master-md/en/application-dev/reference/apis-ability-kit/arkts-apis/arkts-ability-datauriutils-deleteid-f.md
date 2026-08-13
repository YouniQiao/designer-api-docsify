# deleteId

## Modules to Import

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';
```

## deleteId

```TypeScript
function deleteId(uri: string): string
```

Deletes the ID from the end of a given URI.

**Since:** 23

**Deprecated since:** -1

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

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let uri = dataUriUtils.deleteId('com.example.dataUriUtils/1221');
  console.info(`delete id with the uri is: ${uri}`);
} catch(err) {
  console.error(`delete id err, code: ${JSON.stringify((err as BusinessError).code)}, msg: ${JSON.stringify((err as BusinessError).message)}`);
}
```
