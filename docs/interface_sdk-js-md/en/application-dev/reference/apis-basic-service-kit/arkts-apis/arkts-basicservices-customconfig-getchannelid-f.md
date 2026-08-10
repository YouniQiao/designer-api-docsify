# getChannelId

## Modules to Import

```TypeScript
import { customConfig } from 'kits/@kit.BasicServicesKit';
```

## getChannelId

```TypeScript
function getChannelId(): string
```

获取应用的预装渠道号。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-customConfig-function getChannelId(): string--><!--Device-customConfig-function getChannelId(): string-End-->

**System capability:** SystemCapability.Customization.CustomConfig

**Return value:**

| Type | Description |
| --- | --- |
| string | 渠道号 |

## Examples

```TypeScript
import { customConfig } from '@kit.BasicServicesKit';

let channelId: string = customConfig.getChannelId();
console.info('app channelId is ' + channelId);
```

