# AdvertiseSetting

Describes the settings for BLE advertising.

**Since:** 10

<!--Device-ble-interface AdvertiseSetting--><!--Device-ble-interface AdvertiseSetting-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## connectable

```TypeScript
connectable?: boolean
```

Indicates whether the BLE is connectable, default is {@code true}

**Type:** boolean

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdvertiseSetting-connectable?: boolean--><!--Device-AdvertiseSetting-connectable?: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: number
```

Minimum slot value for the advertising interval, which is {@code 32} (20 ms)Maximum slot value for the advertising interval, which is {@code 16777215} (10485.759375s)Default slot value for the advertising interval, which is {@code 1600} (1s)

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdvertiseSetting-interval?: int--><!--Device-AdvertiseSetting-interval?: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## isExtended

```TypeScript
isExtended?: boolean
```

Indicates whether the advertisement is extended, default is {@code false}

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AdvertiseSetting-isExtended?: boolean--><!--Device-AdvertiseSetting-isExtended?: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## txPower

```TypeScript
txPower?: number
```

Minimum transmission power level for advertising, which is {@code -127}Maximum transmission power level for advertising, which is {@code 1}Default transmission power level for advertising, which is {@code -7}

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AdvertiseSetting-txPower?: int--><!--Device-AdvertiseSetting-txPower?: int-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

