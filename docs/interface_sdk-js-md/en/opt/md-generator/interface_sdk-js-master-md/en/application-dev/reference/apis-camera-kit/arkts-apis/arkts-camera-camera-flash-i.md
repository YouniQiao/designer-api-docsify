# Flash

**Flash** inherits from [FlashQuery](arkts-camera-camera-flashquery-i.md).

It provides APIs related to the flash.

**Inheritance/Implementation:** Flash extends [FlashQuery](arkts-camera-camera-flashquery-i.md)

**Since:** 11

<!--Device-camera-interface Flash extends FlashQuery--><!--Device-camera-interface Flash extends FlashQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getFlashMode

```TypeScript
getFlashMode(): FlashMode
```

Obtains the flash mode in use.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Flash-getFlashMode(): FlashMode--><!--Device-Flash-getFlashMode(): FlashMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FlashMode](arkts-camera-camera-flashmode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## offFlashStateChange

```TypeScript
offFlashStateChange(callback?: Callback<FlashState>): void
```

Unsubscribes from flash light status change events.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Flash-offFlashStateChange(callback?: Callback<FlashState>): void--><!--Device-Flash-offFlashStateChange(callback?: Callback<FlashState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FlashState&gt; | No |

## onFlashStateChange

```TypeScript
onFlashStateChange(callback: Callback<FlashState>): void
```

Subscribes to flash light status change events.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Flash-onFlashStateChange(callback: Callback<FlashState>): void--><!--Device-Flash-onFlashStateChange(callback: Callback<FlashState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FlashState&gt; | Yes |

## setFlashMode

```TypeScript
setFlashMode(flashMode: FlashMode): void
```

Sets a flash mode.

Before the setting, do the following checks:

1. Use [hasFlash](arkts-camera-camera-flashquery-i.md#hasflash) to check whether the camera device has flash.2. Use [isFlashModeSupported](arkts-camera-camera-flashquery-i.md#isflashmodesupported) to check whether the camera device supports the flash mode.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Flash-setFlashMode(flashMode: FlashMode): void--><!--Device-Flash-setFlashMode(flashMode: FlashMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
