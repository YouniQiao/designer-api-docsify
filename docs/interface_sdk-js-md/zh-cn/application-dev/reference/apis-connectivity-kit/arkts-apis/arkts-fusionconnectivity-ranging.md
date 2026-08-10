# @ohos.FusionConnectivity.ranging(Ranging Module)

Provides APIs for Fusion Connectivity ranging.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace ranging--><!--Device-unnamed-declare namespace ranging-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## 导入模块

```TypeScript
import { ranging } from 'kits/@kit.ConnectivityKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [getRangingCapability](arkts-connectivity-ranging-getrangingcapability-f.md#getrangingcapability) | Queries whether the current device supports ranging capability. |
| [isRangingSupported](arkts-connectivity-ranging-israngingsupported-f.md#israngingsupported) | Checks whether the current device supports the ranging feature. |
| [offRangingStateChange](arkts-connectivity-ranging-offrangingstatechange-f.md#offrangingstatechange) | Unsubscribe from ranging state change events. |
| [onRangingStateChange](arkts-connectivity-ranging-onrangingstatechange-f.md#onrangingstatechange) | Registers a callback to receive ranging state change notifications.  Notifies state changes for both active ranging and passive ranging operations. |
| [startPassiveRanging](arkts-connectivity-ranging-startpassiveranging-f.md#startpassiveranging) | Starts passive ranging mode.  Upon successful startup, returns a handle identifier for the passive ranging session and begins broadcasting ranging packets.  The returned handle can be used to stop the passive ranging broadcast via stopPassiveRanging. |
| [startRanging](arkts-connectivity-ranging-startranging-f.md#startranging) | Initiates ranging with a specified device.If the link to the target device is already established, ranging starts directly.If not connected, this interface will: 1. Attempt to establish connection and perform pairing/encryption. 2. Query service to verify the device supports ranging. Initiate ranging upon confirmation.Ranging state updates are notified via onRangingStateChange callback. |
| [stopPassiveRanging](arkts-connectivity-ranging-stoppassiveranging-f.md#stoppassiveranging) | Stops passive ranging mode.  Stops the passive ranging broadcast and cleans up associated resources based on the specified handle and ranging capability type. |
| [stopRanging](arkts-connectivity-ranging-stopranging-f.md#stopranging) | Stops ongoing ranging operations.If no target device is specified, stops ranging for all devices associated with the callback.If a target device is specified, only stops ranging for that specific device.This method also releases all occupied resources. For proper resource management,stopRanging must be called after startRanging to avoid resource leaks.State changes are notified via the onRangingStateChange callback. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [RangingCapabilitySupported](arkts-connectivity-ranging-rangingcapabilitysupported-i.md) | Describes the contents of the ranging support types. |
| [RangingMeasurement](arkts-connectivity-ranging-rangingmeasurement-i.md) | Describes the measurement result. |
| [RangingParams](arkts-connectivity-ranging-rangingparams-i.md) | Parameters for ranging operation. |
| [RangingResult](arkts-connectivity-ranging-rangingresult-i.md) | Describes the contents of the ranging results. |
| [RangingStateChangeInfo](arkts-connectivity-ranging-rangingstatechangeinfo-i.md) | Describes the ranging state change information. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [RangingConfidence](arkts-connectivity-ranging-rangingconfidence-e.md) | The enum of ranging measurement confidence. |
| [RangingState](arkts-connectivity-ranging-rangingstate-e.md) | The enum of ranging state. |
| [RangingStoppedCause](arkts-connectivity-ranging-rangingstoppedcause-e.md) | The enum of ranging stopped causes. |
| [RangingTypes](arkts-connectivity-ranging-rangingtypes-e.md) | The enumeration of ranging capability types. |

