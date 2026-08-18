# isDesktopLyricSupported

## Modules to Import

```TypeScript
```

## isDesktopLyricSupported

```TypeScript
function isDesktopLyricSupported(): Promise<boolean>
```

Whether desktop lyric feature is supported.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function isDesktopLyricSupported(): Promise<boolean>--><!--Device-avSession-function isDesktopLyricSupported(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) |

**Examples**

```TypeScript
import { avSession } from '@kit.AVSessionKit';

avSession.isDesktopLyricSupported().then((isSupported: boolean) => {
  console.info(`Succeeded in checking desktop lyric supported: ${isSupported}`);
});
```
