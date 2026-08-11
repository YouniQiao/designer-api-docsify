# getMinHeightSync (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'kits/@kit.BasicServicesKit';
```

## getMinHeightSync

```TypeScript
function getMinHeightSync(): int
```

Obtains the minimum height of the wallpaper. in pixels. returns 0 if no wallpaper has been set.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-wallpaper-function getMinHeightSync(): int--><!--Device-wallpaper-function getMinHeightSync(): int-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | the number returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |

## Examples

```TypeScript
try {
  let minHeight = wallpaper.getMinHeightSync();
  console.info(`success to getMinHeightSync: ${JSON.stringify(minHeight)}`);
} catch (error) {
  console.error(`failed to getMinHeightSync. Code: ${error.code}, Message: ${error.message}`);
}
```

