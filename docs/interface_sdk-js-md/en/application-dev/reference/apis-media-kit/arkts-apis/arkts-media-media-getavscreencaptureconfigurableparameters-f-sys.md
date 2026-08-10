# getAVScreenCaptureConfigurableParameters (System API)

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getAVScreenCaptureConfigurableParameters

```TypeScript
function getAVScreenCaptureConfigurableParameters(sessionId: int): Promise<string>
```

get Configurations which user can changes from AVScreenCapture server

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-media-function getAVScreenCaptureConfigurableParameters(sessionId: int): Promise<string>--><!--Device-media-function getAVScreenCaptureConfigurableParameters(sessionId: int): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | The AVScreenCapture server session ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Returns a configurable configuration item string. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Called from Non-System applications. Return by promise. |
| 5400109 | Sessions not exist. Return by promise. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let sessionId: number = 0; // Use the ID of the session that starts the process.

try {
  let privacyResult: string = await media.getAVScreenCaptureConfigurableParameters(sessionId);
} catch (error: BusinessError) {
  console.error(`getAVScreenCaptureConfigurableParameters error, error message: ${error.message}`);
}
```

