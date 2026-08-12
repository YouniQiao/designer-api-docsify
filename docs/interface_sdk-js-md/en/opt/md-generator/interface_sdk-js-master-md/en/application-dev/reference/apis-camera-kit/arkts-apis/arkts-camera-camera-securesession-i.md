# SecureSession

**SecureSession** inherits from [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash),   
[AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance), [Focus](arkts-camera-camera-focus-i.md#Focus), and [Zoom](arkts-camera-camera-zoom-i.md#Zoom).

It implements a secure session, which provides operations on the flash, exposure, white balance, focus, and zoom.

You can call [createSession](arkts-camera-camera-cameramanager-i.md#createSession) with [SceneMode](arkts-camera-camera-scenemode-e.md#SceneMode) set to **SECURE_PHOTO** to create a session in secure mode. The secure mode is designed for applications with high security requirements, such as facial recognition systems and banking services. It must be used together with the &lt;!--RP1--&gt;security TA&lt;!--RP1End--&gt; to support service scenarios where both standard preview streams and security streams are output.&lt;!--RP2--&gt;

The security TA can verify the signature of data delivered by the server, sign images, parse and assemble TLV logic, and read, create, and operate keys. It applies to image processing.&lt;!--RP2End--&gt;

**Inheritance/Implementation:** SecureSession extends [Session](arkts-camera-camera-session-i.md#Session), [Flash](arkts-camera-camera-flash-i.md#Flash), [AutoExposure](arkts-camera-camera-autoexposure-i.md#AutoExposure), [WhiteBalance](arkts-camera-camera-whitebalance-i.md#WhiteBalance), [Focus](arkts-camera-camera-focus-i.md#Focus), [Zoom](arkts-camera-camera-zoom-i.md#Zoom)

**Since:** 12

<!--Device-camera-interface SecureSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom--><!--Device-camera-interface SecureSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## addSecureOutput

```TypeScript
addSecureOutput(previewOutput: PreviewOutput): void
```

Marks a [PreviewOutput](arkts-camera-camera-previewoutput-i.md#PreviewOutput) stream as secure output.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-SecureSession-addSecureOutput(previewOutput: PreviewOutput): void--><!--Device-SecureSession-addSecureOutput(previewOutput: PreviewOutput): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| previewOutput | [PreviewOutput](arkts-camera-camera-previewoutput-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |

## off('error')

```TypeScript
off(type: 'error', callback?: ErrorCallback): void
```

Unsubscribes from SecureSession error events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-SecureSession-off(type: 'error', callback?: ErrorCallback): void--><!--Device-SecureSession-off(type: 'error', callback?: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | No |

## off('focusStateChange')

```TypeScript
off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void
```

Unsubscribes from focus state change events.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-SecureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void--><!--Device-SecureSession-off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'focusStateChange' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | No |

## on('error')

```TypeScript
on(type: 'error', callback: ErrorCallback): void
```

Subscribes to SecureSession error events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-SecureSession-on(type: 'error', callback: ErrorCallback): void--><!--Device-SecureSession-on(type: 'error', callback: ErrorCallback): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'error' | Yes |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes |

## on('focusStateChange')

```TypeScript
on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void
```

Subscribes to focus state change events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-SecureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void--><!--Device-SecureSession-on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'focusStateChange' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FocusState](arkts-camera-camera-focusstate-e.md)&gt; | Yes |
