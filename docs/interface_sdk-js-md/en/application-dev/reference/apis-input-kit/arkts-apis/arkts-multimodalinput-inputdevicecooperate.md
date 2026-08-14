# @ohos.multimodalInput.inputDeviceCooperate

The **inputDeviceCooperate** module implements screen hopping for two or more networked devices to share the keyboard and mouse for collaborative operations.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Substitutes:** [cooperate/cooperate](../../apis-distributed-service-kit/arkts-apis/arkts-cooperate.md#@ohos.cooperate)

<!--Device-unnamed-declare namespace inputDeviceCooperate--><!--Device-unnamed-declare namespace inputDeviceCooperate-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

## Modules to Import

```TypeScript
import { inputDeviceCooperate } from 'inputDeviceCooperate';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [enable](arkts-input-inputdevicecooperate-enable-f-sys.md#enable) | Enables or disables screen hopping. This API uses an asynchronous callback to return the result. |
| [enable](arkts-input-inputdevicecooperate-enable-f-sys.md#enable-(System-API)) | Specifies whether to enable screen hopping. This API uses a promise to return the result. |
| [getState](arkts-input-inputdevicecooperate-getstate-f-sys.md#getState) | Obtains the state of the screen hopping switch. This API uses an asynchronous callback to return the result. |
| [getState](arkts-input-inputdevicecooperate-getstate-f-sys.md#getState-(System-API)) | Checks whether screen hopping is enabled. This API uses a promise to return the result. |
| [off_cooperation](arkts-input-inputdevicecooperate-offcooperation-f-sys.md#off_cooperation) | Deregisters the listener for screen hopping status changes. This API uses an asynchronous callback to return the result. |
| [on_cooperation](arkts-input-inputdevicecooperate-oncooperation-f-sys.md#on_cooperation) | Registers a listener for screen hopping state changes. This API uses an asynchronous callback to return the result. |
| [start](arkts-input-inputdevicecooperate-start-f-sys.md#start) | Starts screen hopping. This API uses an asynchronous callback to return the result. |
| [start](arkts-input-inputdevicecooperate-start-f-sys.md#start-(System-API)) | Starts screen hopping. This API uses a promise to return the result. |
| [stop](arkts-input-inputdevicecooperate-stop-f-sys.md#stop) | Stops screen hopping. This API uses an asynchronous callback to return the result. |
| [stop](arkts-input-inputdevicecooperate-stop-f-sys.md#stop-(System-API)) | Stops screen hopping. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [EventMsg](arkts-input-inputdevicecooperate-eventmsg-e-sys.md) | Enumerates screen hopping events. |
<!--DelEnd-->

