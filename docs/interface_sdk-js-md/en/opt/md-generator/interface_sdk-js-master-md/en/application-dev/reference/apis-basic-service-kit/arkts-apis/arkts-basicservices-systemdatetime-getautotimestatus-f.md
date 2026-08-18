# getAutoTimeStatus

## Modules to Import

```TypeScript
```

## getAutoTimeStatus

```TypeScript
function getAutoTimeStatus(): boolean
```

Obtains the switch status of the automatic time setting. This API returns the result synchronously.

**Since:** 23

<!--Device-systemDateTime-function getAutoTimeStatus(): boolean--><!--Device-systemDateTime-function getAutoTimeStatus(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [13000001](../../apis-basic-services-kit/errorcode-time.md#13000001-network-or-os-error) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let status: boolean = systemDateTime.getAutoTimeStatus();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get autotime status. message: ${error.message}, code: ${error.code}`);
}
```
