# getChannelId

## Modules to Import

```TypeScript
import { customConfig } from '@kit.BasicServicesKit';
```

## getChannelId

```TypeScript
function getChannelId(): string
```

Obtains a pre-installed channel ID of this application.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.Customization.CustomConfig

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
import { customConfig } from '@kit.BasicServicesKit';

let channelId: string = customConfig.getChannelId();
console.info('app channelId is ' + channelId);
```
