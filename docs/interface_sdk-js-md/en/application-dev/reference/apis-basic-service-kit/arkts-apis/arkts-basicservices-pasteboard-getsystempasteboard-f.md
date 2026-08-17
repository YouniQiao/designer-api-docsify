# getSystemPasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'pasteboard';
```

## getSystemPasteboard

```TypeScript
function getSystemPasteboard(): SystemPasteboard
```

Obtains **SystemPasteboard** object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard--><!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i.md) | SystemPasteboard** object. |

**Examples**

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

