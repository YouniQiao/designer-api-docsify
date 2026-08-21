# MediaQuery

Defines the mediaquery interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-declare class MediaQuery--><!--Device-unnamed-declare class MediaQuery-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SystemMediaQuery, MediaQueryEvent, MediaQueryList } from '@kit.ArkUI';
```

## matchMedia

```TypeScript
static matchMedia(condition: string): MediaQueryList
```

Queries a media item and returns a MediaQueryList object.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MediaQuery-static matchMedia(condition: string): MediaQueryList--><!--Device-MediaQuery-static matchMedia(condition: string): MediaQueryList-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [MediaQueryList](arkts-arkui-systemmediaquery-mediaquerylist-i.md) |  |

