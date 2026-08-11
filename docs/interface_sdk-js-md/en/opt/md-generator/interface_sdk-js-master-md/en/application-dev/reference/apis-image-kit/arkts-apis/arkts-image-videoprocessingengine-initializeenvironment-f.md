# initializeEnvironment

## Modules to Import

```TypeScript
import { videoProcessingEngine } from 'kits/@kit.ImageKit';
```

## initializeEnvironment

```TypeScript
function initializeEnvironment(): Promise<void>
```

Initialize global environment for image processing.

**Since:** 18

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>--><!--Device-videoProcessingEngine-function initializeEnvironment(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.VideoProcessingEngine

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [29200007](../errorcode-videoprocessingengine.md#29200007-insufficient-memory) |
| [29200006](../errorcode-videoprocessingengine.md#29200006-operation-not-allowed) |
| [29200002](../errorcode-videoprocessingengine.md#29200002-initialization-failure) |

## Examples

```TypeScript
import { videoProcessingEngine } from '@kit.ImageKit';

async function initializeEnvironment() {
  videoProcessingEngine.initializeEnvironment();
}
```
