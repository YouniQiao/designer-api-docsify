# getSystemPasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## getSystemPasteboard

```TypeScript
function getSystemPasteboard(): SystemPasteboard
```

Obtains **SystemPasteboard** object.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard--><!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i.md) |

## Examples

```TypeScript
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```
