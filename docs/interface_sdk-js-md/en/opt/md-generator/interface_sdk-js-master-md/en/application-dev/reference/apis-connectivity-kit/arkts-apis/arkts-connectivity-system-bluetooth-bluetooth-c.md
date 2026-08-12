# Bluetooth

Provides methods to manage BLE scan.

**Since:** 6

<!--Device-unnamed-export default class Bluetooth--><!--Device-unnamed-export default class Bluetooth-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

## Modules to Import

```TypeScript
import { BluetoothDevice, BLEFoundResponse, StopBLEScanOptions, SubscribeBLEFoundOptions, StartBLEScanOptions } from '@kit.ConnectivityKit';
```

## startBLEScan

```TypeScript
static startBLEScan(options: StartBLEScanOptions): void
```

Start BLE scan

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static startBLEScan(options: StartBLEScanOptions): void--><!--Device-Bluetooth-static startBLEScan(options: StartBLEScanOptions): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [StartBLEScanOptions](arkts-connectivity-system-bluetooth-startblescanoptions-i.md) | Yes |

## stopBLEScan

```TypeScript
static stopBLEScan(options: StopBLEScanOptions): void
```

Stop BLE scan

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static stopBLEScan(options: StopBLEScanOptions): void--><!--Device-Bluetooth-static stopBLEScan(options: StopBLEScanOptions): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [StopBLEScanOptions](arkts-connectivity-system-bluetooth-stopblescanoptions-i.md) | Yes |

## subscribeBLEFound

```TypeScript
static subscribeBLEFound(options: SubscribeBLEFoundOptions): void
```

Subscribe BLE found

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static subscribeBLEFound(options: SubscribeBLEFoundOptions): void--><!--Device-Bluetooth-static subscribeBLEFound(options: SubscribeBLEFoundOptions): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SubscribeBLEFoundOptions](arkts-connectivity-system-bluetooth-subscribeblefoundoptions-i.md) | Yes |

## unsubscribeBLEFound

```TypeScript
static unsubscribeBLEFound(): void
```

Stop the subscription of BLE found

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static unsubscribeBLEFound(): void--><!--Device-Bluetooth-static unsubscribeBLEFound(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite
