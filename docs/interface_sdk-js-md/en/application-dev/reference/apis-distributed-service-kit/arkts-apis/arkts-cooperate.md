# @ohos.cooperate

The **cooperate** module implements screen hopping for two or more networked devices to share the keyboard and mouse for collaborative operations.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace cooperate--><!--Device-unnamed-declare namespace cooperate-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [activate](arkts-distributedservice-cooperate-activate-f-sys.md#activate) | Starts screen hopping. This API uses an asynchronous callback to return the result. |
| [activate](arkts-distributedservice-cooperate-activate-f-sys.md#activate-(System-API)) | Starts screen hopping. This API uses a promise to return the result. |
| [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activateCooperate) | Starts screen hopping. This API uses an asynchronous callback to return the result. |
| [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activateCooperate-(System-API)) | Starts screen hopping. This API uses a promise to return the result. |
| [activateCooperateWithOptions](arkts-distributedservice-cooperate-activatecooperatewithoptions-f-sys.md#activateCooperateWithOptions) | Starts screen hopping based on the specified options. This API uses a promise to return the result. |
| [deactivate](arkts-distributedservice-cooperate-deactivate-f-sys.md#deactivate) | Stops screen hopping. This API uses an asynchronous callback to return the result. |
| [deactivate](arkts-distributedservice-cooperate-deactivate-f-sys.md#deactivate-(System-API)) | Stops screen hopping. This API uses a promise to return the result. |
| [deactivateCooperate](arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md#deactivateCooperate) | Stops screen hopping. This API uses an asynchronous callback to return the result. |
| [deactivateCooperate](arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md#deactivateCooperate-(System-API)) | Stops screen hopping. This API uses a promise to return the result. |
| [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md#getCooperateSwitchState) | Obtains the screen hopping status of the target device. This API uses an asynchronous callback to return the result. |
| [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md#getCooperateSwitchState-(System-API)) | Obtains the screen hopping status of the target device. This API uses a promise to return the result. |
| [getCrossingSwitchState](arkts-distributedservice-cooperate-getcrossingswitchstate-f-sys.md#getCrossingSwitchState) | Obtains the screen hopping status of the target device. This API uses an asynchronous callback to return the result. |
| [getCrossingSwitchState](arkts-distributedservice-cooperate-getcrossingswitchstate-f-sys.md#getCrossingSwitchState-(System-API)) | Obtains the screen hopping status of the target device. This API uses a promise to return the result. |
| [offCooperateMessage](arkts-distributedservice-cooperate-offcooperatemessage-f-sys.md#offCooperateMessage) | Disables listening for screen hopping status change events. |
| [offCooperateMouseEvent](arkts-distributedservice-cooperate-offcooperatemouseevent-f-sys.md#offCooperateMouseEvent) | Disables listening for mouse pointer position information on the specified device for cooperation. |
| [off_cooperate](arkts-distributedservice-cooperate-offcooperate-f-sys.md#off_cooperate) | Disables listening for screen hopping status change events. |
| off_cooperateMessage | Disables listening for screen hopping status change events. |
| [off_cooperateMouse](arkts-distributedservice-cooperate-offcooperatemouse-f-sys.md#off_cooperateMouse) | Unregisters the listener for the mouse cursor position of a device. |
| [onCooperateMessage](arkts-distributedservice-cooperate-oncooperatemessage-f-sys.md#onCooperateMessage) | Enables listening for screen hopping status change events. |
| [onCooperateMouseEvent](arkts-distributedservice-cooperate-oncooperatemouseevent-f-sys.md#onCooperateMouseEvent) | Enables listening for mouse pointer position information on the specified device for cooperation. |
| [on_cooperate](arkts-distributedservice-cooperate-oncooperate-f-sys.md#on_cooperate) | Enables listening for screen hopping status change events. |
| on_cooperateMessage | Enables listening for screen hopping status change events. |
| [on_cooperateMouse](arkts-distributedservice-cooperate-oncooperatemouse-f-sys.md#on_cooperateMouse) | Registers a listener for the mouse cursor position of a device. |
| [prepare](arkts-distributedservice-cooperate-prepare-f-sys.md#prepare) | Prepares for screen hopping. This API uses an asynchronous callback to return the result. |
| [prepare](arkts-distributedservice-cooperate-prepare-f-sys.md#prepare-(System-API)) | Prepares for screen hopping. This API uses a promise to return the result. |
| [prepareCooperate](arkts-distributedservice-cooperate-preparecooperate-f-sys.md#prepareCooperate) | Prepares for screen hopping. This API uses an asynchronous callback to return the result. |
| [prepareCooperate](arkts-distributedservice-cooperate-preparecooperate-f-sys.md#prepareCooperate-(System-API)) | Prepares for screen hopping. This API uses a promise to return the result. |
| [unprepare](arkts-distributedservice-cooperate-unprepare-f-sys.md#unprepare) | Cancels the preparation for screen hopping. This API uses an asynchronous callback to return the result. |
| [unprepare](arkts-distributedservice-cooperate-unprepare-f-sys.md#unprepare-(System-API)) | Cancels the preparation for screen hopping. This API uses a promise to return the result. |
| [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unprepareCooperate) | Cancels the preparation for screen hopping. This API uses an asynchronous callback to return the result. |
| [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unprepareCooperate-(System-API)) | Cancels the preparation for screen hopping. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [CooperateMessage](arkts-distributedservice-cooperate-cooperatemessage-i-sys.md) | Defines a screen hopping status change event. |
| [CooperateOptions](arkts-distributedservice-cooperate-cooperateoptions-i-sys.md) | Screen hopping options, such as the exit position. |
| [MouseLocation](arkts-distributedservice-cooperate-mouselocation-i-sys.md) | Defines the mouse pointer position for screen hopping. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [CooperateMsg](arkts-distributedservice-cooperate-cooperatemsg-e-sys.md) | Represents a screen hopping message notification. |
| [CooperateState](arkts-distributedservice-cooperate-cooperatestate-e-sys.md) | Enumerates the screen hopping states. |
<!--DelEnd-->

