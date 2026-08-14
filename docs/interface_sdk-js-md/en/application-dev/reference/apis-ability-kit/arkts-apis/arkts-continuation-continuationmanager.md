# @ohos.continuation.continuationManager

The continuationManager module provides the continuation/collaboration management entry. You can use the APIs of this module to connect to and cancel the continuation/collaboration management service, subscribe to and unsubscribe from device connection events, start the device selection module, and update the device connection state.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 22

**Substitutes:** [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md#@ohos.distributedDeviceManager)

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace continuationManager--><!--Device-unnamed-declare namespace continuationManager-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

## Modules to Import

```TypeScript
import { continuationManager } from 'continuationManager';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [off_deviceConnect](arkts-ability-continuationmanager-offdeviceconnect-f.md#off_deviceConnect) | Unsubscribes from device connection events. This API uses an asynchronous callback to return the result. |
| [off_deviceDisconnect](arkts-ability-continuationmanager-offdevicedisconnect-f.md#off_deviceDisconnect) | Unsubscribes from device disconnection events. This API uses an asynchronous callback to return the result. |
| [off_deviceSelected](arkts-ability-continuationmanager-offdeviceselected-f.md#off_deviceSelected) | Unsubscribes from device connection events. |
| [off_deviceUnselected](arkts-ability-continuationmanager-offdeviceunselected-f.md#off_deviceUnselected) | Unsubscribes from device disconnection events. |
| [on_deviceConnect](arkts-ability-continuationmanager-ondeviceconnect-f.md#on_deviceConnect) | Subscribes to device connection events. This API uses an asynchronous callback to return the result. |
| [on_deviceDisconnect](arkts-ability-continuationmanager-ondevicedisconnect-f.md#on_deviceDisconnect) | Subscribes to device disconnection events. This API uses an asynchronous callback to return the result. |
| [on_deviceSelected](arkts-ability-continuationmanager-ondeviceselected-f.md#on_deviceSelected) | Subscribes to device connection events. This API uses an asynchronous callback to return the result. |
| [on_deviceUnselected](arkts-ability-continuationmanager-ondeviceunselected-f.md#on_deviceUnselected) | Subscribes to device disconnection events. This API uses an asynchronous callback to return the result. |
| [register](arkts-ability-continuationmanager-register-f.md#register) | Registers the continuation management service and obtains a token. This API does not involve any filter parameters and uses an asynchronous callback to return the result. |
| [register](arkts-ability-continuationmanager-register-f.md#register) | Registers the continuation management service and obtains a token. This API uses an asynchronous callback to return the result. |
| [register](arkts-ability-continuationmanager-register-f.md#register) | Registers the continuation management service and obtains a token. This API uses a promise to return the result. |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registerContinuation) | Registers the continuation management service and obtains a token. This API does not involve any filter parameters and uses an asynchronous callback to return the result. |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registerContinuation) | Registers the continuation management service and obtains a token. This API uses an asynchronous callback to return the result. |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registerContinuation) | Registers the continuation management service and obtains a token. This API uses a promise to return the result. |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startContinuationDeviceManager) | Starts the device selection module to show the list of available devices on the network. This API does not involve any filter parameters and uses an asynchronous callback to return the result. |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startContinuationDeviceManager) | Starts the device selection module to show the list of available devices on the network. This API uses an asynchronous callback to return the result. |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startContinuationDeviceManager) | Starts the device selection module to show the list of available devices on the network. This API uses a promise to return the result. |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startDeviceManager) | Starts the device selection module to show the list of available devices on the network. This API does not involve any filter parameters and uses an asynchronous callback to return the result. |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startDeviceManager) | Starts the device selection module to show the list of available devices on the network. This API uses an asynchronous callback to return the result. |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startDeviceManager) | Starts the device selection module to show the list of available devices on the network. This API uses a promise to return the result. |
| [unregister](arkts-ability-continuationmanager-unregister-f.md#unregister) | Unregisters the continuation management service. This API uses an asynchronous callback to return the result. |
| [unregister](arkts-ability-continuationmanager-unregister-f.md#unregister) | Unregisters the continuation management service. This API uses a promise to return the result. |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md#unregisterContinuation) | Unregisters the continuation management service. This API uses an asynchronous callback to return the result. |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md#unregisterContinuation) | Unregisters the continuation management service. This API uses a promise to return the result. |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md#updateConnectStatus) | Instructs the device selection module to update the device connection state. This API uses an asynchronous callback to return the result. |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md#updateConnectStatus) | Instructs the device selection module to update the device connection state. This API uses a promise to return the result. |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md#updateContinuationState) | Instructs the device selection module to update the device connection state. This API uses an asynchronous callback to return the result. |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md#updateContinuationState) | Instructs the device selection module to update the device connection state. This API uses a promise to return the result. |

### Enums

| Name | Description |
| --- | --- |
| [ContinuationMode](arkts-ability-continuationmanager-continuationmode-e.md) | Enumerates the continuation modes provided by the device selection module. |
| [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) | Device connection state. |

### Types

| Name | Description |
| --- | --- |
| [ContinuationExtraParams](arkts-ability-continuationmanager-continuationextraparams-t.md) | Defines the extra parameters required by the device selection module in the continuation management entry. |
| [ContinuationResult](arkts-ability-continuationmanager-continuationresult-t.md) | Defines the device information returned by the continuation management entry. |

