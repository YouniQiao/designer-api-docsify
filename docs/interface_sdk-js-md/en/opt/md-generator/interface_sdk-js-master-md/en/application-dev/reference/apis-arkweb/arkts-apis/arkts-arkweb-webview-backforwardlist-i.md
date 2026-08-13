# BackForwardList

Provides back and forward history list information method. related to [HistoryItem](arkts-arkweb-webview-historyitem-i.md#HistoryItem).

**Since:** 9

**Deprecated since:** -1

<!--Device-webview-interface BackForwardList--><!--Device-webview-interface BackForwardList-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
import { webview } from '@kit.ArkWeb';
```

## getItemAtIndex

```TypeScript
getItemAtIndex(index: number): HistoryItem
```

Get history entry at given index.

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BackForwardList-getItemAtIndex(index: number): HistoryItem--><!--Device-BackForwardList-getItemAtIndex(index: number): HistoryItem-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HistoryItem](arkts-arkweb-webview-historyitem-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## currentIndex

```TypeScript
currentIndex: number
```

Current index in BackForwardList.

**Type:** number

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BackForwardList-currentIndex: number--><!--Device-BackForwardList-currentIndex: number-End-->

**System capability:** SystemCapability.Web.Webview.Core

## size

```TypeScript
size: number
```

Size of in BackForwardList.

**Type:** number

**Since:** 9

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-BackForwardList-size: number--><!--Device-BackForwardList-size: number-End-->

**System capability:** SystemCapability.Web.Webview.Core
