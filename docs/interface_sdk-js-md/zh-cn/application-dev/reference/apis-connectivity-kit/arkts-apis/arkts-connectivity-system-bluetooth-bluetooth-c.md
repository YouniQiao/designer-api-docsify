# Bluetooth

Provides methods to manage BLE scan.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export default class Bluetooth--><!--Device-unnamed-export default class Bluetooth-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

## 导入模块

```TypeScript
import { BluetoothDevice, BLEFoundResponse, StopBLEScanOptions, SubscribeBLEFoundOptions, StartBLEScanOptions } from 'kits/@kit.ConnectivityKit';
```

## startBLEScan

```TypeScript
static startBLEScan(options: StartBLEScanOptions): void
```

Start BLE scan

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Bluetooth-static startBLEScan(options: StartBLEScanOptions): void--><!--Device-Bluetooth-static startBLEScan(options: StartBLEScanOptions): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [StartBLEScanOptions](arkts-connectivity-system-bluetooth-startblescanoptions-i.md) | 是 | Options |

## stopBLEScan

```TypeScript
static stopBLEScan(options: StopBLEScanOptions): void
```

Stop BLE scan

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Bluetooth-static stopBLEScan(options: StopBLEScanOptions): void--><!--Device-Bluetooth-static stopBLEScan(options: StopBLEScanOptions): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [StopBLEScanOptions](arkts-connectivity-system-bluetooth-stopblescanoptions-i.md) | 是 | Options |

## subscribeBLEFound

```TypeScript
static subscribeBLEFound(options: SubscribeBLEFoundOptions): void
```

Subscribe BLE found

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Bluetooth-static subscribeBLEFound(options: SubscribeBLEFoundOptions): void--><!--Device-Bluetooth-static subscribeBLEFound(options: SubscribeBLEFoundOptions): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeBLEFoundOptions](arkts-connectivity-system-bluetooth-subscribeblefoundoptions-i.md) | 是 | Options |

## unsubscribeBLEFound

```TypeScript
static unsubscribeBLEFound(): void
```

Stop the subscription of BLE found

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-Bluetooth-static unsubscribeBLEFound(): void--><!--Device-Bluetooth-static unsubscribeBLEFound(): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Lite

