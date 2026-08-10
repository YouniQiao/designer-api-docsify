# isDesktopLyricSupported

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## isDesktopLyricSupported

```TypeScript
function isDesktopLyricSupported(): Promise<boolean>
```

设备是否支持桌面歌词功能。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avSession-function isDesktopLyricSupported(): Promise<boolean>--><!--Device-avSession-function isDesktopLyricSupported(): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示设备支持桌面歌词功能；返回false表示设备不支持桌面歌词功能。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |

## Examples

```TypeScript
import { avSession } from '@kit.AVSessionKit';

avSession.isDesktopLyricSupported().then((isSupported: boolean) => {
  console.info(`Succeeded in checking desktop lyric supported: ${isSupported}`);
});
```

