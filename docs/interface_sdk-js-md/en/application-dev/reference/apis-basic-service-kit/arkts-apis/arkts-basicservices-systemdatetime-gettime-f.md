# getTime

## Modules to Import

```TypeScript
import { systemDateTime } from 'kits/@kit.BasicServicesKit';
```

## getTime

```TypeScript
function getTime(isNanoseconds?: boolean): long
```

Obtains the time elapsed since the Unix epoch. This API returns the result synchronously.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-systemDateTime-function getTime(isNanoseconds?: boolean): long--><!--Device-systemDateTime-function getTime(isNanoseconds?: boolean): long-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isNanoseconds | boolean | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：long | Time elapsed since the Unix epoch. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getTime(true)
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get time. message: ${error.message}, code: ${error.code}`);
}
```

