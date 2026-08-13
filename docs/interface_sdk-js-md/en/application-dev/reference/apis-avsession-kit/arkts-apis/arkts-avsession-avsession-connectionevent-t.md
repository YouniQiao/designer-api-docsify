# ConnectionEvent

```TypeScript
type ConnectionEvent = (state: ConnectionState, device: OutputDeviceInfo) => void
```

The connection event supplied by system to indicate device state and information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-avSession-type ConnectionEvent = (state: ConnectionState, device: OutputDeviceInfo) => void--><!--Device-avSession-type ConnectionEvent = (state: ConnectionState, device: OutputDeviceInfo) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | ConnectionState | Yes | device connection state |
| device | [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) | Yes | device information |

