# reportAVScreenCaptureUserChoice (System API)

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## reportAVScreenCaptureUserChoice

```TypeScript
function reportAVScreenCaptureUserChoice(sessionId: number, choice: string): Promise<void>
```

Reports the user selection result in the screen capture privacy dialog box to the AVScreenCapture server to determine whether to start screen capture. Screen capture starts only when the user touches a button to continue the operation. This API is called by the system application that creates the dialog box.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Media.AVScreenCapture

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |
| choice | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
