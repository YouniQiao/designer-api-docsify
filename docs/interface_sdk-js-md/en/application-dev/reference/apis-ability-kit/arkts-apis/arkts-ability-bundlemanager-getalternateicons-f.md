# getAlternateIcons

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAlternateIcons

```TypeScript
function getAlternateIcons(): Promise<Array<AlternateIconInfo>>
```

Queries the alternate icon information configured in the alternateIcons in the app.json5 of the current application. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;AlternateIconInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 17700311 |
