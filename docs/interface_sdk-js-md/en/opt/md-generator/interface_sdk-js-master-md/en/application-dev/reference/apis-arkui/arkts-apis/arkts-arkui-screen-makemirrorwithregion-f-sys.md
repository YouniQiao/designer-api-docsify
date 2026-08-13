# makeMirrorWithRegion (System API)

## Modules to Import

```TypeScript
import { screen } from '@kit.ArkUI';
```

## makeMirrorWithRegion

```TypeScript
function makeMirrorWithRegion(mainScreen: number, mirrorScreen: Array<number>, mainScreenRegion: Rect): Promise<number>
```

Sets a rectangle on the screen to mirror mode. This API uses a promise to return the result. After this API is called, you are advised not to rotate or fold the screen further. Otherwise, the mirrored content may be abnormal.

**Since:** 23

**Deprecated since:** -1

<!--Device-screen-function makeMirrorWithRegion(mainScreen: long, mirrorScreen: Array<long>, mainScreenRegion: Rect): Promise<long>--><!--Device-screen-function makeMirrorWithRegion(mainScreen: long, mirrorScreen: Array<long>, mainScreenRegion: Rect): Promise<long>-End-->

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
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the screen ID using getAllScreens().
let mainScreenId: number = 0; // Main screen ID.
let mirrorScreenIds: Array<number> = [1, 2, 3]; // ID array of mirrored screens.
// Rectangle on the main screen to be mirrored.
let mainScreenRegion: screen.Rect = {
  left : 0,
  top : 0,
  width : 1920,
  height : 1080
};
// Set a rectangle on the screen to mirror mode.
screen.makeMirrorWithRegion(mainScreenId, mirrorScreenIds, mainScreenRegion).then((data: number) => {
  console.info(`Succeeded in setting screen mirroring. Data: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set screen area mirroring. Code: ${err.code}, message: ${err.message}`);
});
```
