# FocusQuery

FocusQuery provides APIs to check whether a focus mode is supported.

> **NOTE：**
> 
> - This interface was first introduced in API version 12. In this version, a compatibility change was made that
> preserved the initial version information of inner elements. As a result, you might see outer element's @since
> version number being higher than that of the inner elements. However, this discrepancy does not affect the
> functionality of the interface.

**Since:** 12

<!--Device-camera-interface FocusQuery--><!--Device-camera-interface FocusQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## isFocusAssistSupported

```TypeScript
isFocusAssistSupported(): boolean
```

Checks whether the focus assist is supported.

**Since:** 12

<!--Device-FocusQuery-isFocusAssistSupported(): boolean--><!--Device-FocusQuery-isFocusAssistSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusAssistSupported(professionalPhotoSession: camera.ProfessionalPhotoSession): boolean {
  let status: boolean = false;
  try {
    status = professionalPhotoSession.isFocusAssistSupported();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The isFocusAssistSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```

## isFocusDrivenTypeSupported

```TypeScript
isFocusDrivenTypeSupported(type: FocusDrivenType): boolean
```

Checks whether a focus drive type is supported.

**Since:** 15

<!--Device-FocusQuery-isFocusDrivenTypeSupported(type: FocusDrivenType): boolean--><!--Device-FocusQuery-isFocusDrivenTypeSupported(type: FocusDrivenType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [FocusDrivenType](arkts-camera-camera-focusdriventype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusDrivenTypeSupported(session: camera.VideoSessionForSys, type: camera.FocusDrivenType): boolean {
  let status: boolean = false;
  try {
    status = session.isFocusDrivenTypeSupported(type);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The isFocusDrivenTypeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```

## isFocusRangeTypeSupported

```TypeScript
isFocusRangeTypeSupported(type: FocusRangeType): boolean
```

Checks whether a focus range type is supported.

**Since:** 15

<!--Device-FocusQuery-isFocusRangeTypeSupported(type: FocusRangeType): boolean--><!--Device-FocusQuery-isFocusRangeTypeSupported(type: FocusRangeType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [FocusRangeType](arkts-camera-camera-focusrangetype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusRangeTypeSupported(session: camera.VideoSessionForSys, type: camera.FocusRangeType): boolean {
  let status: boolean = false;
  try {
    status = session.isFocusRangeTypeSupported(type);
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(`The isFocusRangeTypeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```
