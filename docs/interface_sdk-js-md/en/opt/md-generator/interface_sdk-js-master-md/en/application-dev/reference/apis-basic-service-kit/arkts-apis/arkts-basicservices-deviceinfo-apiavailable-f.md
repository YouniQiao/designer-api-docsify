# apiAvailable

## Modules to Import

```TypeScript
```

## apiAvailable

```TypeScript
function apiAvailable(version: string | number): boolean
```

Checks whether a specified API version is available on the current device. This API provides compatibility check across different OpenHarmony/Distribution OS versions. A suitable version check method is automatically selected based on the input format and supported API versions.

**Since:** 26.0.0

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-deviceInfo-function apiAvailable(version: string | number): boolean--><!--Device-deviceInfo-function apiAvailable(version: string | number): boolean-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| version | string \| number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { deviceInfo } from '@kit.BasicServicesKit';

// Check whether the API version is 26.0.0 or later. If true is returned, the API version of the current device meets the requirements.
if (deviceInfo.apiAvailable("26.0.0")) {
   // Method that requires version isolation
}


// Check API 5.0.1 (Distribution OS version, API 26.0.0-)
if (deviceInfo.apiAvailable("5.0.1")) {
   // Method that requires version isolation
}


// Check API 13 (OpenHarmony SDK version, API 26.0.0-)
if (deviceInfo.apiAvailable(13)) {
   // Method that requires version isolation
}
```
