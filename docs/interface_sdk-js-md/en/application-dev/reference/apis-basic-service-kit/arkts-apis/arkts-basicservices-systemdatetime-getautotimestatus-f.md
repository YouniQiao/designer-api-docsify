# getAutoTimeStatus

## Modules to Import

```TypeScript
import { systemDateTime } from '@kit.BasicServicesKit';
```

## getAutoTimeStatus

```TypeScript
function getAutoTimeStatus(): boolean
```

Obtains the switch status of the automatic time setting. This API returns the result synchronously.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

<!--Device-systemDateTime-function getAutoTimeStatus(): boolean--><!--Device-systemDateTime-function getAutoTimeStatus(): boolean-End-->

**System capability:** SystemCapability.MiscServices.Time

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Switch status of the automatic time setting. &lt;br&gt;- **true**: The automatic time setting is on. &lt;br&gt;- **false**: The automatic time setting is off. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [13000001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-time.md#13000001-network-or-os-error) | Network connection error or OS error. Possible causes: 1.System memory is insufficient; 2.Calls the underlying system interface failed. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let status: boolean = systemDateTime.getAutoTimeStatus();
} catch(e) {
  let error = e as BusinessError;
  console.error(`Failed to get autotime status. message: ${error.message}, code: ${error.code}`);
}
```

