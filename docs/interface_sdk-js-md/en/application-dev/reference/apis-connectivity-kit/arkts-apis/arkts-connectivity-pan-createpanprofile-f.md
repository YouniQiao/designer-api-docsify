# createPanProfile

## Modules to Import

```TypeScript
import { pan } from '@kit.ConnectivityKit';
```

## createPanProfile

```TypeScript
function createPanProfile(): PanProfile
```

create the instance of pan profile.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-pan-function createPanProfile(): PanProfile--><!--Device-pan-function createPanProfile(): PanProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| [PanProfile](arkts-connectivity-pan-panprofile-i.md) | Returns the instance of pan profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |

**Examples**

```TypeScript
try {
    let panProfile : pan.PanProfile= pan.createPanProfile();
    console.info('pan success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
