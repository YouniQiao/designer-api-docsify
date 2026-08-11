# PanProfile

Manager pan host profile.

**Inheritance/Implementation:** PanProfile extends [BaseProfile](arkts-connectivity-pan-baseprofile-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

<!--Device-pan-interface PanProfile extends BaseProfile--><!--Device-pan-interface PanProfile extends BaseProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { pan } from 'kits/@kit.ConnectivityKit';
```

## isPanSupported

```TypeScript
isPanSupported(): boolean
```

Determine whether the local device supports PAN.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanProfile-isPanSupported(): boolean--><!--Device-PanProfile-isPanSupported(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the local device supports PAN; returns false otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2900099 | Operation failed. |

## isTetheringOn

```TypeScript
isTetheringOn(): boolean
```

Obtains the tethering enable or disable.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanProfile-isTetheringOn(): boolean--><!--Device-PanProfile-isTetheringOn(): boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns the value { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Only can be called on phone, tablet, and 2in1 devices. Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs.<br>**Applicable version:** 10 - 24 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let panProfile: pan.PanProfile = pan.createPanProfile();
    panProfile.isTetheringOn();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

