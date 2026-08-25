# pick

## Modules to Import

```TypeScript
import { screenshot } from 'kits/@kit.ArkUI';
```

## pick

```TypeScript
function pick(): Promise<PickInfo>
```

Obtains this screenshot. Currently, only the screenshot of the display whose ID is **0** can be obtained. (If a screenshot of the extended screen is needed, you can use the [capture](arkts-arkui-screenshot-capture-f.md) API.) This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PickInfo](arkts-arkui-screenshot-pickinfo-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
