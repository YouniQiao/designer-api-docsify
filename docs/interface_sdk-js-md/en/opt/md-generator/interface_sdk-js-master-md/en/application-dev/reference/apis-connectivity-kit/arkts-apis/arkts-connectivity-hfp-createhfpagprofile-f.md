# createHfpAgProfile

## Modules to Import

```TypeScript
import { hfp } from 'kits/@kit.ConnectivityKit';
```

## createHfpAgProfile

```TypeScript
function createHfpAgProfile(): HandsFreeAudioGatewayProfile
```

create the instance of hfp profile.

**Since:** 10

<!--Device-hfp-function createHfpAgProfile(): HandsFreeAudioGatewayProfile--><!--Device-hfp-function createHfpAgProfile(): HandsFreeAudioGatewayProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HandsFreeAudioGatewayProfile](arkts-connectivity-bluetoothmanager-handsfreeaudiogatewayprofile-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let hfpAgProfile = hfp.createHfpAgProfile();
    console.info('hfpAg success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
