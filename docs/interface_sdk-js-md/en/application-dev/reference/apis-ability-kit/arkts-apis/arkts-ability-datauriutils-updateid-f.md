# updateId

## Modules to Import

```TypeScript
import { dataUriUtils } from 'dataUriUtils';
```

## updateId

```TypeScript
function updateId(uri: string, id: double): string
```

Updates the ID in a given URI.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-dataUriUtils-function updateId(uri: string, id: double): string--><!--Device-dataUriUtils-function updateId(uri: string, id: double): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Target URI object. |
| id | double | Yes | New ID. |

**Return value:**

| Type | Description |
| --- | --- |
| string | URI object with the new ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let id = 1122;
  let uri = dataUriUtils.updateId(
    'com.example.dataUriUtils/1221',
    id
  );
} catch (err) {
  console.error(`update id err, code: ${JSON.stringify((err as BusinessError).code)}, msg: ${JSON.stringify((err as BusinessError).message)}`);
}
```

