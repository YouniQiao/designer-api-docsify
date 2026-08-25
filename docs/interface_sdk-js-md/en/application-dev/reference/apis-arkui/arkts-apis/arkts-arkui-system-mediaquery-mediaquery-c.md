# MediaQuery

Defines the MediaQuery API.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn since version 3; ArkTS-Sta since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SystemMediaQuery, MediaQueryEvent, MediaQueryList } from '@kit.ArkUI';
```

## matchMedia

```TypeScript
static matchMedia(condition: string): MediaQueryList
```

Creates a **MediaQueryList** object based on the query condition.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn since version 3; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| condition | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaQueryList](arkts-arkui-system-mediaquery-mediaquerylist-i.md) |

**Examples**

```TypeScript
let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');
```
