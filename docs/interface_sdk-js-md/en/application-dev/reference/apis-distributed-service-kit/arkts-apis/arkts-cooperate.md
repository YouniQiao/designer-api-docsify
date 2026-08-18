# @ohos.cooperate

The **cooperate** module implements screen hopping for two or more networked devices to share the keyboard and mouse for collaborative operations.

**Since:** 23

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
| [activate](arkts-distributedservice-cooperate-activate-f-sys.md#activate-system-api) | Starts screen hopping. This API uses a promise to return the result. |
| [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate) | Starts screen hopping. This API uses an asynchronous callback to return the result. |
| [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate-system-api) | Starts screen hopping. This API uses a promise to return the result. |
| [activateCooperateWithOptions](arkts-distributedservice-cooperate-activatecooperatewithoptions-f-sys.md#activatecooperatewithoptions) | Starts screen hopping based on the specified options. This API uses a promise to return the result. |
| [deactivate](arkts-distributedservice-cooperate-deactivate-f-sys.md#deactivate) | Stops screen hopping. This API uses an asynchronous callback to return the result. |
| [deactivate](arkts-distributedservice-cooperate-deactivate-f-sys.md#deactivate-system-api) | Stops screen hopping. This API uses a promise to return the result. |
| [deactivateCooperate](arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md#deactivatecooperate) | Stops screen hopping. This API uses an asynchronous callback to return the result. |
| [deactivateCooperate](arkts-distributedservice-cooperate-deactivatecooperate-f-sys.md#deactivatecooperate-system-api) | Stops screen hopping. This API uses a promise to return the result. |
| [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md#getcooperateswitchstate) | Obtains the screen hopping status of the target device. This API uses an asynchronous callback to return the result. |
| [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md#getcooperateswitchstate-system-api) | Obtains the screen hopping status of the target device. This API uses a promise to return the result. |
| [getCrossingSwitchState](arkts-distributedservice-cooperate-getcrossingswitchstate-f-sys.md#getcrossingswitchstate) | Obtains the screen hopping status of the target device. This API uses an asynchronous callback to return the result. |
| [getCrossingSwitchState](arkts-distributedservice-cooperate-getcrossingswitchstate-f-sys.md#getcrossingswitchstate-system-api) | Obtains the screen hopping status of the target device. This API uses a promise to return the result. |
| [offCooperateMessage](arkts-distributedservice-cooperate-offcooperatemessage-f-sys.md#offcooperatemessage) | Disables listening for screen hopping status change events. |
| [offCooperateMouseEvent](arkts-distributedservice-cooperate-offcooperatemouseevent-f-sys.md#offcooperatemouseevent) | Disables listening for mouse pointer position information on the specified device for cooperation. |
| [off_cooperate](arkts-distributedservice-cooperate-offcooperate-f-sys.md#offcooperate) | Disables listening for screen hopping status change events. |
| [off_cooperateMessage](arkts-distributedservice-cooperate-offcooperatemessage-f-sys.md#offcooperatemessage) | Disables listening for screen hopping status change events. |
| [off_cooperateMouse](arkts-distributedservice-cooperate-offcooperatemouse-f-sys.md#offcooperatemouse) | Unregisters the listener for the mouse cursor position of a device. |
| [onCooperateMessage](arkts-distributedservice-cooperate-oncooperatemessage-f-sys.md#oncooperatemessage) | Enables listening for screen hopping status change events. |
| [onCooperateMouseEvent](arkts-distributedservice-cooperate-oncooperatemouseevent-f-sys.md#oncooperatemouseevent) | Enables listening for mouse pointer position information on the specified device for cooperation. |
| [on_cooperate](arkts-distributedservice-cooperate-oncooperate-f-sys.md#oncooperate) | Enables listening for screen hopping status change events. |
| [on_cooperateMessage](arkts-distributedservice-cooperate-oncooperatemessage-f-sys.md#oncooperatemessage) | Enables listening for screen hopping status change events. |
| [on_cooperateMouse](arkts-distributedservice-cooperate-oncooperatemouse-f-sys.md#oncooperatemouse) | Registers a listener for the mouse cursor position of a device. |
| [prepare](arkts-distributedservice-cooperate-prepare-f-sys.md#prepare) | Prepares for screen hopping. This API uses an asynchronous callback to return the result. |
| [prepare](arkts-distributedservice-cooperate-prepare-f-sys.md#prepare-system-api) | Prepares for screen hopping. This API uses a promise to return the result. |
| [prepareCooperate](arkts-distributedservice-cooperate-preparecooperate-f-sys.md#preparecooperate) | Prepares for screen hopping. This API uses an asynchronous callback to return the result. |
| [prepareCooperate](arkts-distributedservice-cooperate-preparecooperate-f-sys.md#preparecooperate-system-api) | Prepares for screen hopping. This API uses a promise to return the result. |
| [unprepare](arkts-distributedservice-cooperate-unprepare-f-sys.md#unprepare) | Cancels the preparation for screen hopping. This API uses an asynchronous callback to return the result. |
| [unprepare](arkts-distributedservice-cooperate-unprepare-f-sys.md#unprepare-system-api) | Cancels the preparation for screen hopping. This API uses a promise to return the result. |
| [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unpreparecooperate) | Cancels the preparation for screen hopping. This API uses an asynchronous callback to return the result. |
| [unprepareCooperate](arkts-distributedservice-cooperate-unpreparecooperate-f-sys.md#unpreparecooperate-system-api) | Cancels the preparation for screen hopping. This API uses a promise to return the result. |
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

