# AdvertisingStateChangeInfo

Advertising state change information.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ble-interface AdvertisingStateChangeInfo--><!--Device-ble-interface AdvertisingStateChangeInfo-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from 'kits/@kit.ConnectivityKit';
```

## advertisingId

```TypeScript
advertisingId: int
```

Indicates the ID of current advertising.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingStateChangeInfo-advertisingId: int--><!--Device-AdvertisingStateChangeInfo-advertisingId: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## state

```TypeScript
state: AdvertisingState
```

Indicates the advertising state.

**Type:** [AdvertisingState](arkts-connectivity-ble-advertisingstate-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AdvertisingStateChangeInfo-state: AdvertisingState--><!--Device-AdvertisingStateChangeInfo-state: AdvertisingState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

