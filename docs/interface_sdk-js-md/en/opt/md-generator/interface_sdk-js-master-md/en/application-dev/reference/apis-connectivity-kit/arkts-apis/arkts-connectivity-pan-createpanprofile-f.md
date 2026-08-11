# createPanProfile

## Modules to Import

```TypeScript
import { pan } from 'kits/@kit.ConnectivityKit';
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

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PanProfile](arkts-connectivity-pan-panprofile-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

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
