# ControlCenterSession (System API)

Control center session object.

**Inheritance/Implementation:** ControlCenterSession extends [Beauty](arkts-camera-camera-beauty-i-sys.md#Beauty-(System-API)), [Aperture](arkts-camera-camera-aperture-i-sys.md#Aperture-(System-API)), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md#ColorEffect-(System-API))

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface ControlCenterSession--><!--Device-camera-interface ControlCenterSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## enableAutoFraming

```TypeScript
enableAutoFraming(enabled: boolean): void
```

Enable auto-framing effect.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-ControlCenterSession-enableAutoFraming(enabled: boolean): void--><!--Device-ControlCenterSession-enableAutoFraming(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | enable auto-framing effect if TRUE. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) | Session not running. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## getAutoFramingStatus

```TypeScript
getAutoFramingStatus(): boolean
```

Gets the status of auto-framing effect.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-ControlCenterSession-getAutoFramingStatus(): boolean--><!--Device-ControlCenterSession-getAutoFramingStatus(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is auto-framing active. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## getControlCenterHeight

```TypeScript
getControlCenterHeight(): double
```

Gets the control center height.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ControlCenterSession-getControlCenterHeight(): double--><!--Device-ControlCenterSession-getControlCenterHeight(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| double | the control center height, in units of vp. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## getCurrentDevice

```TypeScript
getCurrentDevice(): CameraDevice
```

Gets the current camera device.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ControlCenterSession-getCurrentDevice(): CameraDevice--><!--Device-ControlCenterSession-getCurrentDevice(): CameraDevice-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) | the current camera device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) | Session not running. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## isAutoFramingSupported

```TypeScript
isAutoFramingSupported(): boolean
```

Checks whether auto-framing is supported.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

<!--Device-ControlCenterSession-isAutoFramingSupported(): boolean--><!--Device-ControlCenterSession-isAutoFramingSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is auto-framing supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## release

```TypeScript
release(): Promise<void>
```

Release control center session object.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-ControlCenterSession-release(): Promise<void>--><!--Device-ControlCenterSession-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## usedAsPosition

```TypeScript
usedAsPosition(position: CameraPosition): void
```

Sets the camera to be used as a camera at the specified position.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ControlCenterSession-usedAsPosition(position: CameraPosition): void--><!--Device-ControlCenterSession-usedAsPosition(position: CameraPosition): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes | The positon used for the camera. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) | Session not running. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

