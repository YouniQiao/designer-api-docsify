# initializeEnvironment

## Modules to Import

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';
```

## initializeEnvironment

```TypeScript
function initializeEnvironment(): Promise<void>
```

Initialize global environment for image processing.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>--><!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | A Promise instance used to return the operation result. If the operation fails, an error message is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function initializeEnvironment can not work correctly &lt;br&gt;due to limited device capabilities. |
| [29200007](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-videoprocessingengine.md#29200007-insufficient-memory) | Out of memory. |
| [29200006](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-videoprocessingengine.md#29200006-operation-not-allowed) | The operation is not permitted. This may be caused by incorrect status. |
| [29200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-image-kit/errorcode-videoprocessingengine.md#29200002-initialization-failure) | The global environment initialization for image processing failed, &lt;br&gt;such as failure to initialize the GPU environment. |

## Examples

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function initializeEnvironment() {
  videoProcessingEngine.initializeEnvironment();
}
```

