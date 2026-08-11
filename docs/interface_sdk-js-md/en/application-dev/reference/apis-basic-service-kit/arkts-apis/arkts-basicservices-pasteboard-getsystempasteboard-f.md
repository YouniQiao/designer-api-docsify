# getSystemPasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## getSystemPasteboard

```TypeScript
function getSystemPasteboard(): SystemPasteboard
```

Obtains **SystemPasteboard** object.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard--><!--Device-pasteboard-function getSystemPasteboard(): SystemPasteboard-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

**Return value:**

| Type | Description |
| --- | --- |
| [SystemPasteboard](arkts-basicservices-pasteboard-systempasteboard-i.md) | SystemPasteboard** object. |

## Examples

```TypeScript
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
```

