# getMinHeightSync (System API)

## Modules to Import

```TypeScript
```

## getMinHeightSync

```TypeScript
function getMinHeightSync(): number
```

Obtains the minimum height of the wallpaper. in pixels. returns 0 if no wallpaper has been set.

**Since:** 23

<!--Device-wallpaper-function getMinHeightSync(): int--><!--Device-wallpaper-function getMinHeightSync(): int-End-->

**System capability:** SystemCapability.MiscServices.Wallpaper

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

**Examples**

```TypeScript
try {
  let minHeight = wallpaper.getMinHeightSync();
  console.info(`success to getMinHeightSync: ${JSON.stringify(minHeight)}`);
} catch (error) {
  console.error(`failed to getMinHeightSync. Code: ${error.code}, Message: ${error.message}`);
}
```
