# createHfpHfProfile

## Modules to Import

```TypeScript
import { hfp } from 'kits/@kit.ConnectivityKit';
```

## createHfpHfProfile

```TypeScript
function createHfpHfProfile(): HandsFreeHfProfile
```

create the instance of HF(Hands-Free Unit) for HFP(Hands-Free Profile).

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-hfp-function createHfpHfProfile(): HandsFreeHfProfile--><!--Device-hfp-function createHfpHfProfile(): HandsFreeHfProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| [HandsFreeHfProfile](arkts-connectivity-hfp-handsfreehfprofile-i-sys.md) | Returns the instance of profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |

