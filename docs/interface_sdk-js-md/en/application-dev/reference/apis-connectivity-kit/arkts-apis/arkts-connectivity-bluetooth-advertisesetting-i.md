# AdvertiseSetting

Describes the settings for BLE advertising.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [AdvertiseSetting](arkts-connectivity-bluetoothmanager-advertisesetting-i.md)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## Modules to Import

```TypeScript
import bas from '@kit.ConnectivityKit.bas';
import common from '@kit.ConnectivityKit.common';
import bluetooth from '@kit.ConnectivityKit';
import map from '@kit.ConnectivityKit.map';
import pan from '@kit.ConnectivityKit.pan';
import pbap from '@kit.ConnectivityKit.pbap';
import opp from '@kit.ConnectivityKit.opp';
import socket from '@kit.ConnectivityKit.socket';
import wearDetection from '@kit.ConnectivityKit.wearDetection';
import bluetoothManager from '@kit.ConnectivityKitManager';
```

## connectable

```TypeScript
connectable?: boolean
```

Indicates whether the BLE is connectable, default is {@code true}

**Type:** boolean

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [connectable](arkts-connectivity-bluetoothmanager-advertisesetting-i.md#connectable)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## interval

```TypeScript
interval?: number
```

Minimum slot value for the advertising interval, which is {@code 32} (20 ms) Maximum slot value for the advertising interval, which is {@code 16777215} (10485.759375s) Default slot value for the advertising interval, which is {@code 1600} (1s)

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [interval](arkts-connectivity-bluetoothmanager-advertisesetting-i.md#interval)

**System capability:** SystemCapability.Communication.Bluetooth.Core

## txPower

```TypeScript
txPower?: number
```

Minimum transmission power level for advertising, which is {@code -127} Maximum transmission power level for advertising, which is {@code 1} Default transmission power level for advertising, which is {@code -7}

**Type:** number

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [txPower](arkts-connectivity-bluetoothmanager-advertisesetting-i.md#txpower)

**System capability:** SystemCapability.Communication.Bluetooth.Core
