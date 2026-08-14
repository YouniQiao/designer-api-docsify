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

## enableLcdFlash

```TypeScript
enableLcdFlash(enabled: boolean): void
```

Enables or disables the LCD flash. Before the setting, call [isLcdFlashSupported](arkts-camera-camera-flashquery-i-sys.md#isLcdFlashSupported) to check whether the device supports the LCD flash.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-Flash-enableLcdFlash(enabled: boolean): void--><!--Device-Flash-enableLcdFlash(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable or disable the LCD flash. **true** to enable, **false** otherwise. If null or undefined is passed, it is treated as 0 and the LCD flash is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableLcdFlash(session: camera.PhotoSessionForSys | camera.VideoSessionForSys | camera.NightPhotoSession): void {
  try {
    session.enableLcdFlash(true);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The setFlashMode call failed. error code: ${err.code}`);
  }
}
```

