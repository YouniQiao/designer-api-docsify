# matchMediaSync

## Modules to Import

```TypeScript
```

## matchMediaSync

```TypeScript
function matchMediaSync(condition: string): MediaQueryListener
```

Sets the media query condition. This API returns the corresponding media query listener. > **NOTE：**> > - This API is supported since API version 7 and deprecated since API version 18. You are advised to use > [matchMediaSync](arkts-arkui-arkui-uicontext-mediaquery-c.md#matchmediasync) instead. Before calling this API, you > need to obtain the [MediaQuery](arkts-arkui-arkui-uicontext-mediaquery-c.md#mediaquery) object using the > [getMediaQuery](arkts-arkui-arkui-uicontext-uicontext-c.md#getmediaquery) method in > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext). > > - Since API version 10, you can use the > [getMediaQuery](arkts-arkui-arkui-uicontext-uicontext-c.md#getmediaquery) API in > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#uicontext) to obtain the > [MediaQuery](arkts-arkui-arkui-uicontext-mediaquery-c.md#mediaquery) object associated with the current UI context.

**Since:** 7

**Deprecated since:** 18

**Substitutes:** matchMediaSync

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-mediaquery-function matchMediaSync(condition: string): MediaQueryListener--><!--Device-mediaquery-function matchMediaSync(condition: string): MediaQueryListener-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaQueryListener](arkts-arkui-mediaquery-mediaquerylistener-i.md) |

**Examples**

```TypeScript
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // Listen for landscape events.
```
