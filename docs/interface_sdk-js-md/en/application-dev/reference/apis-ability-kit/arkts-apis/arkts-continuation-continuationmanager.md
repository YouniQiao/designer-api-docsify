# @ohos.continuation.continuationManager

The continuationManager module provides the continuation/collaboration management entry. You can use the APIs of this module to connect to and cancel the continuation/collaboration management service, subscribe to and unsubscribe from device connection events, start the device selection module, and update the device connection state.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Deprecated since:** 22

**Substitutes:** [distributedDeviceManager](../../apis-distributed-service-kit/arkts-apis/arkts-distributeddevicemanager.md)

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.DistributedAbilityManager

## Modules to Import

```TypeScript
import { continuationManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [off](arkts-ability-continuationmanager-off-f.md#offdeviceselected) |
| [off](arkts-ability-continuationmanager-off-f.md#offdeviceunselected) |
| [off](arkts-ability-continuationmanager-off-f.md#offdeviceconnect) |
| [off](arkts-ability-continuationmanager-off-f.md#offdevicedisconnect) |
| [on](arkts-ability-continuationmanager-on-f.md#ondeviceselected) |
| [on](arkts-ability-continuationmanager-on-f.md#ondeviceunselected) |
| [on](arkts-ability-continuationmanager-on-f.md#ondeviceconnect) |
| [on](arkts-ability-continuationmanager-on-f.md#ondevicedisconnect) |
| [register](arkts-ability-continuationmanager-register-f.md) |
| [register](arkts-ability-continuationmanager-register-f.md) |
| [register](arkts-ability-continuationmanager-register-f.md) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md) |
| [registerContinuation](arkts-ability-continuationmanager-registercontinuation-f.md) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md) |
| [startContinuationDeviceManager](arkts-ability-continuationmanager-startcontinuationdevicemanager-f.md) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md) |
| [startDeviceManager](arkts-ability-continuationmanager-startdevicemanager-f.md) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md) |
| [unregister](arkts-ability-continuationmanager-unregister-f.md) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md) |
| [unregisterContinuation](arkts-ability-continuationmanager-unregistercontinuation-f.md) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md) |
| [updateConnectStatus](arkts-ability-continuationmanager-updateconnectstatus-f.md) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md) |
| [updateContinuationState](arkts-ability-continuationmanager-updatecontinuationstate-f.md) |

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
