# getSeniorModeStateForSelf

## Modules to Import

```TypeScript
import { accessibility } from 'accessibility';
```

## getSeniorModeStateForSelf

```TypeScript
function getSeniorModeStateForSelf(): Promise<boolean>
```

Checks whether the app has "senior mode" enabled. This API uses a promise to return the result. Unlike [accessibility.isSeniorModeEnabled](arkts-accessibility-accessibility-isseniormodeenabled-f.md#isseniormodeenabled), which checks whether the system-level senior mode is enabled, this API only queries the state of the app itself.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function getSeniorModeStateForSelf(): Promise<boolean>--><!--Device-accessibility-function getSeniorModeStateForSelf(): Promise<boolean>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the "senior mode " of the app itself is enabled, and **false** indicates that the "senior mode" of the app itself is disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9300000](../errorcode-accessibility.md#9300000-accessibility-system-service-abnormal) | System abnormality. |

