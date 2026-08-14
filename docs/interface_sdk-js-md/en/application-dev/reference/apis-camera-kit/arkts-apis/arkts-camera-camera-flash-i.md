# Flash

**Flash** inherits from [FlashQuery](arkts-camera-camera-flashquery-i.md#FlashQuery). It provides APIs related to the flash.

**Inheritance/Implementation:** Flash extends [FlashQuery](arkts-camera-camera-flashquery-i.md#FlashQuery)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-camera-interface Flash--><!--Device-camera-interface Flash-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'camera';
```

## getFlashMode

```TypeScript
getFlashMode(): FlashMode
```

Obtains the flash mode in use.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Flash-getFlashMode(): FlashMode--><!--Device-Flash-getFlashMode(): FlashMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| [FlashMode](arkts-camera-camera-flashmode-e.md) | Flash mode obtained. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

## offFlashStateChange

```TypeScript
offFlashStateChange(callback?: Callback<FlashState>): void
```

Unsubscribes from flash light status change events.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Flash-offFlashStateChange(callback?: Callback<FlashState>): void--><!--Device-Flash-offFlashStateChange(callback?: Callback<FlashState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FlashState](arkts-camera-camera-flashstate-e.md)&gt; | No | Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled. |

## onFlashStateChange

```TypeScript
onFlashStateChange(callback: Callback<FlashState>): void
```

Subscribes to flash light status change events.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Flash-onFlashStateChange(callback: Callback<FlashState>): void--><!--Device-Flash-onFlashStateChange(callback: Callback<FlashState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FlashState](arkts-camera-camera-flashstate-e.md)&gt; | Yes | Callback used to return the flash light status. |

## setFlashMode

```TypeScript
setFlashMode(flashMode: FlashMode): void
```

Sets a flash mode. Before the setting, do the following checks: 1. Use [hasFlash](arkts-camera-camera-flashquery-i.md#hasFlash) to check whether the camera device has flash. 2. Use [isFlashModeSupported](arkts-camera-camera-flashquery-i.md#isFlashModeSupported) to check whether the camera device supports the flash mode.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-Flash-setFlashMode(flashMode: FlashMode): void--><!--Device-Flash-setFlashMode(flashMode: FlashMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flashMode | [FlashMode](arkts-camera-camera-flashmode-e.md) | Yes | Flash mode. If the input parameter is null or undefined, it is treated as 0 and the flash is turned off. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |

