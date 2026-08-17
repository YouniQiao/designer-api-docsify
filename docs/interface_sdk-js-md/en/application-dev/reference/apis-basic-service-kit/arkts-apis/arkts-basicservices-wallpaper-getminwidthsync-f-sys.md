# getMinWidthSync (System API)

## Modules to Import

```TypeScript
import { wallpaper } from 'wallpaper';
```

## getMinWidthSync

```TypeScript
function getMinWidthSync(): int
```

Obtains the minimum width of the wallpaper. in pixels. returns 0 if no wallpaper has been set.

**Since:** 23

<!--Device-wallpaper-function getMinWidthSync(): int--><!--Device-wallpaper-function getMinWidthSync(): int-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| int | the number returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | permission verification failed, application which is not a system application uses system API. |

**Examples**

```TypeScript
try {
  let minWidth = wallpaper.getMinWidthSync();
  console.info(`success to getMinWidthSync: ${JSON.stringify(minWidth)}`);
} catch (error) {
  console.error(`failed to getMinWidthSync. Code: ${error.code}, Message: ${error.message}`);
}
```

