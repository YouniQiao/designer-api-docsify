# getTimezoneSync

## Modules to Import

```TypeScript
import { systemDateTime } from '@kit.BasicServicesKit';
```

## getTimezoneSync

```TypeScript
function getTimezoneSync(): string
```

Obtains the system time zone in synchronous mode.

**Since:** 23

**Deprecated since:** -1

<!--Device-systemDateTime-function getTimezoneSync(): string--><!--Device-systemDateTime-function getTimezoneSync(): string-End-->

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timezone: string = systemDateTime.getTimezoneSync();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
}
```
