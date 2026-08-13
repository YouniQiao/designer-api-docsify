# isStandby

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## isStandby

```TypeScript
function isStandby(): boolean
```

Checks whether the device is in standby mode.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-power-function isStandby(): boolean--><!--Device-power-function isStandby(): boolean-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The value **true** indicates that the device is in standby mode, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) | Failed to connect to the service. |

## Examples

```TypeScript
try {
    let isStandby = power.isStandby();
    console.info('device is in standby: ' + isStandby);
} catch(err) {
    console.error('check isStandby failed, err: ' + err);
}
```

