# getAllDisplayPhysicalResolution

## Modules to Import

```TypeScript
```

## getAllDisplayPhysicalResolution

```TypeScript
function getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>
```

Obtains all the display modes supported by the current device, along with the physical screen resolutions for each mode. This API uses a promise to return the result.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-display-function getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>--><!--Device-display-function getAllDisplayPhysicalResolution(): Promise<Array<DisplayPhysicalResolution>>-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[DisplayPhysicalResolution](arkts-arkui-display-displayphysicalresolution-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = display.getAllDisplayPhysicalResolution();
promise.then((resolutionObjects) => {
  console.info('Obtaining physical resolution length: ' + resolutionObjects.length);
  for (let i = 0; i < resolutionObjects.length; i++) {
     console.info(`resolutionObjects[${i}].foldDisplayMode: ${resolutionObjects[i].foldDisplayMode}`);
     console.info(`resolutionObjects[${i}].physicalWidth: ${resolutionObjects[i].physicalWidth}`); 
     console.info(`resolutionObjects[${i}].physicalHeight: ${resolutionObjects[i].physicalHeight}`); 
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain physical resolution. Code: ${err.code}, message: ${err.message}`);
});
```
