# ControlCenterSession (System API)

Control center session object.

**Inheritance/Implementation:** ControlCenterSession extends [Beauty](arkts-camera-camera-beauty-i-sys.md#Beauty-(System-API)), [Aperture](arkts-camera-camera-aperture-i-sys.md#Aperture-(System-API)), [ColorEffect](arkts-camera-camera-coloreffect-i-sys.md#ColorEffect-(System-API))

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ControlCenterSession--><!--Device-camera-interface ControlCenterSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## enableAutoFraming

```TypeScript
enableAutoFraming(enabled: boolean): void
```

Enable auto-framing effect.

**Since:** 24

**Deprecated since:** -1

<!--Device-ControlCenterSession-enableAutoFraming(enabled: boolean): void--><!--Device-ControlCenterSession-enableAutoFraming(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getAutoFramingStatus

```TypeScript
getAutoFramingStatus(): boolean
```

Gets the status of auto-framing effect.

**Since:** 24

**Deprecated since:** -1

<!--Device-ControlCenterSession-getAutoFramingStatus(): boolean--><!--Device-ControlCenterSession-getAutoFramingStatus(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getControlCenterHeight

```TypeScript
getControlCenterHeight(): number
```

Gets the control center height.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ControlCenterSession-getControlCenterHeight(): double--><!--Device-ControlCenterSession-getControlCenterHeight(): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getCurrentDevice

```TypeScript
getCurrentDevice(): CameraDevice
```

Gets the current camera device.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ControlCenterSession-getCurrentDevice(): CameraDevice--><!--Device-ControlCenterSession-getCurrentDevice(): CameraDevice-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [CameraDevice](arkts-camera-camera-cameradevice-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isAutoFramingSupported

```TypeScript
isAutoFramingSupported(): boolean
```

Checks whether auto-framing is supported.

**Since:** 24

**Deprecated since:** -1

<!--Device-ControlCenterSession-isAutoFramingSupported(): boolean--><!--Device-ControlCenterSession-isAutoFramingSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## release

```TypeScript
release(): Promise<void>
```

Release control center session object.

**Since:** 23

**Deprecated since:** -1

<!--Device-ControlCenterSession-release(): Promise<void>--><!--Device-ControlCenterSession-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## usedAsPosition

```TypeScript
usedAsPosition(position: CameraPosition): void
```

Sets the camera to be used as a camera at the specified position.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ControlCenterSession-usedAsPosition(position: CameraPosition): void--><!--Device-ControlCenterSession-usedAsPosition(position: CameraPosition): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400104](../errorcode-camera.md#7400104-session-not-running) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
