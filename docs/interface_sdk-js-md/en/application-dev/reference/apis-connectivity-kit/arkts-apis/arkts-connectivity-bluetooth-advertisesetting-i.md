# AdvertiseSetting

Describes the settings for BLE advertising.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** AdvertiseSetting

<!--Device-bluetooth-interface AdvertiseSetting--><!--Device-bluetooth-interface AdvertiseSetting-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## connectable

```TypeScript
connectable?: boolean
```

Indicates whether the BLE is connectable, default is {@code true}

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** connectable

<!--Device-AdvertiseSetting-connectable?: boolean--><!--Device-AdvertiseSetting-connectable?: boolean-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: number
```

Minimum slot value for the advertising interval, which is {@code 32} (20 ms)Maximum slot value for the advertising interval, which is {@code 16777215} (10485.759375s)Default slot value for the advertising interval, which is {@code 1600} (1s)

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** interval

<!--Device-AdvertiseSetting-interval?: number--><!--Device-AdvertiseSetting-interval?: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

## txPower

```TypeScript
txPower?: number
```

Minimum transmission power level for advertising, which is {@code -127}Maximum transmission power level for advertising, which is {@code 1}Default transmission power level for advertising, which is {@code -7}

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** txPower

<!--Device-AdvertiseSetting-txPower?: number--><!--Device-AdvertiseSetting-txPower?: number-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

