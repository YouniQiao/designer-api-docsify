# attachId

## Modules to Import

```TypeScript
import { dataUriUtils } from 'kits/@kit.AbilityKit';
```

## attachId

```TypeScript
function attachId(uri: string, id: double): string
```

将ID附加到uri的路径末尾。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-dataUriUtils-function attachId(uri: string, id: double): string--><!--Device-dataUriUtils-function attachId(uri: string, id: double): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 表示uri对象。 |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示要附加的ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回附加ID之后的uri对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { dataUriUtils } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let id = 1122;
try {
  let uri = dataUriUtils.attachId(
    'com.example.dataUriUtils',
    id,
  );
  console.info(`attachId the uri is: ${uri}`);
} catch (err) {
  console.error(`get id err, code: ${JSON.stringify((err as BusinessError).code)}, msg: ${JSON.stringify((err as BusinessError).message)}`);
}
```

