# getTime

## Modules to Import

```TypeScript
import { systemDateTime } from '@kit.BasicServicesKit';
```

## getTime

```TypeScript
function getTime(isNanoseconds?: boolean): number
```

Obtains the time elapsed since the Unix epoch. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-systemDateTime-function getTime(isNanoseconds?: boolean): long--><!--Device-systemDateTime-function getTime(isNanoseconds?: boolean): long-End-->

**System capability:** SystemCapability.MiscServices.Time

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isNanoseconds | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

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
