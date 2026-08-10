# onDeviceAvailable (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## onDeviceAvailable

```TypeScript
function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void
```

Register device discovery callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void--><!--Device-avSession-function onDeviceAvailable(callback: Callback<OutputDeviceInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;OutputDeviceInfo&gt; | Yes | Used to returns the device info |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not System App. |

