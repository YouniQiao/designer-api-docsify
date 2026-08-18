# Session

**Session** implements a session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md#camerainput) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md#cameraoutput) instances required to run the camera and requests the camera to take a photo or record a video.

**Since:** 23

<!--Device-camera-interface Session--><!--Device-camera-interface Session-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
```

## getActiveParameter

```TypeScript
getActiveParameter(key: string): string
```

Gets the active value of the given key in camera metadata.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Session-getActiveParameter(key: string): string--><!--Device-Session-getActiveParameter(key: string): string-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getCameraOutputCapabilities

```TypeScript
getCameraOutputCapabilities(camera: CameraDevice): Array<CameraOutputCapability>
```

Get the supported camera output capability set.

**Since:** 23

<!--Device-Session-getCameraOutputCapabilities(camera: CameraDevice): Array<CameraOutputCapability>--><!--Device-Session-getCameraOutputCapabilities(camera: CameraDevice): Array<CameraOutputCapability>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [camera](arkts-multimedia-camera.md) | [CameraDevice](arkts-camera-camera-cameradevice-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[CameraOutputCapability](arkts-camera-camera-cameraoutputcapability-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getParameters

```TypeScript
getParameters(key: string): Array<string>
```

Gets the values of the given key in camera metadata.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Session-getParameters(key: string): Array<string>--><!--Device-Session-getParameters(key: string): Array<string>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getSupportedKeys

```TypeScript
getSupportedKeys(): Array<string>
```

Gets the supported keys in camera metadata.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Session-getSupportedKeys(): Array<string>--><!--Device-Session-getSupportedKeys(): Array<string>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setParameters

```TypeScript
setParameters(kvpairs: Record<string, string>): void
```

Sets key-value pairs parameters for the session.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-Session-setParameters(kvpairs: Record<string, string>): void--><!--Device-Session-setParameters(kvpairs: Record<string, string>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| kvpairs | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setUsage

```TypeScript
setUsage(usage: UsageType, enabled: boolean): void
```

Set usage for the capture session.

**Since:** 23

<!--Device-Session-setUsage(usage: UsageType, enabled: boolean): void--><!--Device-Session-setUsage(usage: UsageType, enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| usage | [UsageType](arkts-camera-camera-usagetype-e-sys.md) | Yes |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
