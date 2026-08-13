# BackForwardList

Provides back and forward history list information method. related to [HistoryItem](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-historyitem-i.md#HistoryItem).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-webview-interface BackForwardList--><!--Device-webview-interface BackForwardList-End-->

**System capability:** SystemCapability.Web.Webview.Core

## getItemAtIndex

```TypeScript
getItemAtIndex(index: int): HistoryItem
```

Get history entry at given index.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BackForwardList-getItemAtIndex(index: int): HistoryItem--><!--Device-BackForwardList-getItemAtIndex(index: int): HistoryItem-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of back forward list entry. |

**Return value:**

| Type | Description |
| --- | --- |
| [HistoryItem](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-historyitem-i.md) | HistoryItem at given index in back forward list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. 3.Parameter verification failed. |

## currentIndex

```TypeScript
currentIndex: int
```

Current index in BackForwardList.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BackForwardList-currentIndex: int--><!--Device-BackForwardList-currentIndex: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## size

```TypeScript
size: int
```

Size of in BackForwardList.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-BackForwardList-size: int--><!--Device-BackForwardList-size: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

