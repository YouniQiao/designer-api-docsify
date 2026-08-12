# onDeviceOffline (System API)

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## onDeviceOffline

```TypeScript
function onDeviceOffline(callback: Callback<string>): void
```

Register device offline callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-avSession-function onDeviceOffline(callback: Callback<string>): void--><!--Device-avSession-function onDeviceOffline(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | Used to returns the device info |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |

