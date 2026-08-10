# updateId

## Modules to Import

```TypeScript
import { dataUriUtils } from 'kits/@kit.AbilityKit';
```

## updateId

```TypeScript
function updateId(uri: string, id: double): string
```

更新指定uri中的ID。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-dataUriUtils-function updateId(uri: string, id: double): string--><!--Device-dataUriUtils-function updateId(uri: string, id: double): string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 表示uri对象 |
| id | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 表示要更新的ID |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回更新ID之后的uri对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

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

