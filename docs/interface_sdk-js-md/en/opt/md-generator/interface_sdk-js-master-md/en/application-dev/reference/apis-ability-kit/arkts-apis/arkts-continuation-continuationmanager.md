# @ohos.continuation.continuationManager

The continuationManager module provides the continuation/collaboration management entry. You can use the APIs of this module to connect to and cancel the continuation/collaboration management service, subscribe to and unsubscribe from device connection events, start the device selection module, and update the device connection state.

**Since:** 8

**Deprecated since:** 22

**Substitutes:** [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md#@ohos.distributedDeviceManager)

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace continuationManager--><!--Device-unnamed-declare namespace continuationManager-End-->

**System capability:** SystemCapability.Ability.DistributedAbilityManager

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off_deviceConnect](arkts-ability-continuationmanager-offdeviceconnect-f.md#off_deviceConnect) |
| [off_deviceDisconnect](arkts-ability-continuationmanager-offdevicedisconnect-f.md#off_deviceDisconnect) |
| [off_deviceSelected](arkts-ability-continuationmanager-offdeviceselected-f.md#off_deviceSelected) |
| [off_deviceUnselected](arkts-ability-continuationmanager-offdeviceunselected-f.md#off_deviceUnselected) |
| [on_deviceConnect](arkts-ability-continuationmanager-ondeviceconnect-f.md#on_deviceConnect) |
| [on_deviceDisconnect](arkts-ability-continuationmanager-ondevicedisconnect-f.md#on_deviceDisconnect) |
| [on_deviceSelected](arkts-ability-continuationmanager-ondeviceselected-f.md#on_deviceSelected) |
| [on_deviceUnselected](arkts-ability-continuationmanager-ondeviceunselected-f.md#on_deviceUnselected) |
| [register](arkts-ability-continuationmanager-register-f.md#register) |
| [register](arkts-ability-continuationmanager-register-f.md#register) |
| [register](arkts-ability-continuationmanager-register-f.md#register) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registerContinuation) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registerContinuation) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md#registerContinuation) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startContinuationDeviceManager) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startContinuationDeviceManager) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md#startContinuationDeviceManager) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startDeviceManager) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startDeviceManager) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md#startDeviceManager) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md#unregister) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md#unregister) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md#unregisterContinuation) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md#unregisterContinuation) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md#updateConnectStatus) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md#updateConnectStatus) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md#updateContinuationState) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md#updateContinuationState) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContinuationMode](arkts-ability-continuationmanager-continuationmode-e.md) |
| [DeviceConnectState](arkts-ability-continuationmanager-deviceconnectstate-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContinuationExtraParams](arkts-ability-continuationmanager-continuationextraparams-t.md) |
| [ContinuationResult](arkts-ability-continuationmanager-continuationresult-t.md) |
