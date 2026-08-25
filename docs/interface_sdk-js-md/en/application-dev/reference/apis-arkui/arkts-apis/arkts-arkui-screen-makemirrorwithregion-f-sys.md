# makeMirrorWithRegion (System API)

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## makeMirrorWithRegion

```TypeScript
function makeMirrorWithRegion(mainScreen: number, mirrorScreen: Array<number>, mainScreenRegion: Rect): Promise<number>
```

Sets a rectangle on the screen to mirror mode. This API uses a promise to return the result. After this API is called, you are advised not to rotate or fold the screen further. Otherwise, the mirrored content may be abnormal.

**Since:** 19

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mainScreen | number | Yes |
| mirrorScreen | Array & lt;number & gt; | Yes |
| mainScreenRegion | [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
