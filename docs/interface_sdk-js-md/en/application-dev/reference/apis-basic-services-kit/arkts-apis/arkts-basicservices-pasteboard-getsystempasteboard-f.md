# getSystemPasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## getSystemPasteboard

```TypeScript
function getSystemPasteboard(): SystemPasteboard
```

Obtains a **SystemPasteboard** object and returns a singleton instance of the pasteboard service. After this API is called, the **SystemPasteboard** object can be used to access the read, write, and listening functions of the pasteboard. The same instance is returned each time this API is called. Before calling this API, ensure that the pasteboard service is running properly. Before performing any read or write operation on the pasteboard, you need to call this API to obtain the **SystemPasteboard** object.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard--><!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i.md) | **SystemPasteboard** object. |

**Examples**

```TypeScript
// Obtain the SystemPasteboard object.
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```
