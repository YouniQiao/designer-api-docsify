# AutoDeviceSwitchStatus

自动切换镜头状态信息。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-camera-interface AutoDeviceSwitchStatus--><!--Device-camera-interface AutoDeviceSwitchStatus-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## isDeviceCapabilityChanged

```TypeScript
readonly isDeviceCapabilityChanged: boolean
```

自动切换镜头成功后，其镜头能力值是否发生改变。true表示发生变化，false表示未发生变化。

**Type:** boolean

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoDeviceSwitchStatus-readonly isDeviceCapabilityChanged: boolean--><!--Device-AutoDeviceSwitchStatus-readonly isDeviceCapabilityChanged: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isDeviceSwitched

```TypeScript
readonly isDeviceSwitched: boolean
```

自动切换镜头是否成功。true表示成功，false表示失败。

**Type:** boolean

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoDeviceSwitchStatus-readonly isDeviceSwitched: boolean--><!--Device-AutoDeviceSwitchStatus-readonly isDeviceSwitched: boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

