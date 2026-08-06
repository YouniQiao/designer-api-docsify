# Bluetooth

Provides methods to manage BLE scan.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export default class Bluetooth--><!--Device-unnamed-export default class Bluetooth-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

## startBLEScan

```TypeScript
static startBLEScan(options: StartBLEScanOptions): void
```

Start BLE scan

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static startBLEScan(options: StartBLEScanOptions): void--><!--Device-Bluetooth-static startBLEScan(options: StartBLEScanOptions): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options |

## stopBLEScan

```TypeScript
static stopBLEScan(options: StopBLEScanOptions): void
```

Stop BLE scan

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static stopBLEScan(options: StopBLEScanOptions): void--><!--Device-Bluetooth-static stopBLEScan(options: StopBLEScanOptions): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options |

## subscribeBLEFound

```TypeScript
static subscribeBLEFound(options: SubscribeBLEFoundOptions): void
```

Subscribe BLE found

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static subscribeBLEFound(options: SubscribeBLEFoundOptions): void--><!--Device-Bluetooth-static subscribeBLEFound(options: SubscribeBLEFoundOptions): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options |

## unsubscribeBLEFound

```TypeScript
static unsubscribeBLEFound(): void
```

Stop the subscription of BLE found

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Model restriction:** This API can be used only in the FA model.

<!--Device-Bluetooth-static unsubscribeBLEFound(): void--><!--Device-Bluetooth-static unsubscribeBLEFound(): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Lite

