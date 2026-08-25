# getAllDisplayPhysicalResolution

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplayPhysicalResolution

```TypeScript
function getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>
```

Obtains all the display modes supported by the current device, along with the physical screen resolutions for each mode. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[DisplayPhysicalResolution](arkts-arkui-display-displayphysicalresolution-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
