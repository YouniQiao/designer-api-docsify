# @ohos.FusionConnectivity.ranging(Ranging Module)

Provides APIs for Fusion Connectivity ranging.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

## Modules to Import

```TypeScript
import ranging from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getRangingCapability(Ranging Module)](arkts-connectivity-ranging-getrangingcapability-f.md) | Queries whether the current device supports ranging capability. |
| [isRangingSupported(Ranging Module)](arkts-connectivity-ranging-israngingsupported-f.md) | Checks whether the current device supports the ranging feature. |
| [offRangingStateChange(Ranging Module)](arkts-connectivity-ranging-offrangingstatechange-f.md) | Unsubscribe from ranging state change events. |
| [onRangingStateChange(Ranging Module)](arkts-connectivity-ranging-onrangingstatechange-f.md) | Registers a callback to receive ranging state change notifications.Notifies state changes for both active ranging and passive ranging operations. |
| [startPassiveRanging(Ranging Module)](arkts-connectivity-ranging-startpassiveranging-f.md) | Starts passive ranging mode.Upon successful startup, returns a handle identifier for the passive ranging session and begins broadcasting ranging packets.The returned handle can be used to stop the passive ranging broadcast via stopPassiveRanging. |
| [startRanging(Ranging Module)](arkts-connectivity-ranging-startranging-f.md) | Initiates ranging with a specified device. If the link to the target device is already established, ranging starts directly. If not connected, this interface will: 1. Attempt to establish connection and perform pairing/encryption. 2. Query service to verify the device supports ranging. Initiate ranging upon confirmation. Ranging state updates are notified via onRangingStateChange callback. |
| [stopPassiveRanging(Ranging Module)](arkts-connectivity-ranging-stoppassiveranging-f.md) | Stops passive ranging mode.Stops the passive ranging broadcast and cleans up associated resources based on the specified handle and ranging capability type. |
| [stopRanging(Ranging Module)](arkts-connectivity-ranging-stopranging-f.md) | Stops ongoing ranging operations. If no target device is specified, stops ranging for all devices associated with the callback. If a target device is specified, only stops ranging for that specific device. This method also releases all occupied resources. For proper resource management, stopRanging must be called after startRanging to avoid resource leaks. State changes are notified via the onRangingStateChange callback. |

### Interfaces

| Name | Description |
| --- | --- |
| [RangingCapabilitySupported(Ranging Module)](arkts-connectivity-ranging-rangingcapabilitysupported-i.md) | Describes the contents of the ranging support types. |
| [RangingMeasurement(Ranging Module)](arkts-connectivity-ranging-rangingmeasurement-i.md) | Describes the measurement result. |
| [RangingParams(Ranging Module)](arkts-connectivity-ranging-rangingparams-i.md) | Parameters for ranging operation. |
| [RangingResult(Ranging Module)](arkts-connectivity-ranging-rangingresult-i.md) | Describes the contents of the ranging results. |
| [RangingStateChangeInfo(Ranging Module)](arkts-connectivity-ranging-rangingstatechangeinfo-i.md) | Describes the ranging state change information. |

### Enums

| Name | Description |
| --- | --- |
| [RangingConfidence(Ranging Module)](arkts-connectivity-ranging-rangingconfidence-e.md) | The enum of ranging measurement confidence. |
| [RangingState(Ranging Module)](arkts-connectivity-ranging-rangingstate-e.md) | The enum of ranging state. |
| [RangingStoppedCause(Ranging Module)](arkts-connectivity-ranging-rangingstoppedcause-e.md) | The enum of ranging stopped causes. |
| [RangingTypes(Ranging Module)](arkts-connectivity-ranging-rangingtypes-e.md) | The enumeration of ranging capability types. |
