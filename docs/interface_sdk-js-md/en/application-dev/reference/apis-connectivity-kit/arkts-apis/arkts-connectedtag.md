# @ohos.connectedTag

Provides methods to operate or manage Connected Tag.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace connectedTag--><!--Device-unnamed-declare namespace connectedTag-End-->

**System capability:** SystemCapability.Communication.ConnectedTag

## Modules to Import

```TypeScript
import { connectedTag } from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [init](arkts-connectivity-connectedtag-init-f.md#init) | Initializes Connected Tag. |
| [initialize](arkts-connectivity-connectedtag-initialize-f.md#initialize) | Initializes the connected NFC tag. |
| [off_notify](arkts-connectivity-connectedtag-offnotify-f.md#off_notify) | Unsubscribes NFC RF status change events. &lt;p&gt;All callback functions will be unregistered If there is no specific callback parameter.&lt;/p&gt; |
| [on_notify](arkts-connectivity-connectedtag-onnotify-f.md#on_notify) | Subscribes NFC RF status change events. |
| [read](arkts-connectivity-connectedtag-read-f.md#read) | Reads the NDEF data from the connected NFC tag. |
| [read](arkts-connectivity-connectedtag-read-f.md#read) | Reads the NDEF data from the connected NFC tag. |
| [readNdefTag](arkts-connectivity-connectedtag-readndeftag-f.md#readNdefTag) | Reads the NDEF Data. |
| [readNdefTag](arkts-connectivity-connectedtag-readndeftag-f.md#readNdefTag) | Reads the NDEF Data. |
| [uninit](arkts-connectivity-connectedtag-uninit-f.md#uninit) | UnInitializes Connected Tag. |
| [uninitialize](arkts-connectivity-connectedtag-uninitialize-f.md#uninitialize) | Uninitializes the connected NFC tag. |
| [write](arkts-connectivity-connectedtag-write-f.md#write) | Writes the NDEF data to the connected NFC tag. |
| [write](arkts-connectivity-connectedtag-write-f.md#write) | Writes the NDEF data to the connected NFC tag. |
| [writeNdefTag](arkts-connectivity-connectedtag-writendeftag-f.md#writeNdefTag) | Writes the NDEF Data. |
| [writeNdefTag](arkts-connectivity-connectedtag-writendeftag-f.md#writeNdefTag) | Writes the NDEF Data. |

### Enums

| Name | Description |
| --- | --- |
| [NfcRfType](arkts-connectivity-connectedtag-nfcrftype-e.md) | Describes the NFC RF type. |

