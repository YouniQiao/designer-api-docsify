# createPanProfile

## Modules to Import

```TypeScript
import { pan } from 'pan';
```

## createPanProfile

```TypeScript
function createPanProfile(): PanProfile
```

create the instance of pan profile.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-pan-function createPanProfile(): PanProfile--><!--Device-pan-function createPanProfile(): PanProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| PanProfile | Returns the instance of pan profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let panProfile : pan.PanProfile= pan.createPanProfile();
    console.info('pan success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

