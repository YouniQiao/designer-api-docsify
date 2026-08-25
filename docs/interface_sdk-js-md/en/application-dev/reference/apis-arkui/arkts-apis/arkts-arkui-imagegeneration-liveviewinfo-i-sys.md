# LiveViewInfo (System API)

Information for LiveView in AI image generation.@interface LiveViewInfo

**Since:** 26.0.0

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## getLongTermTaskId

```TypeScript
getLongTermTaskId(): number
```

Get the number-term task ID for LiveView.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getWant

```TypeScript
getWant(): Want
```

Get the Want object for LiveView.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) |

## isLiveViewNeeded

```TypeScript
isLiveViewNeeded(): boolean
```

Check whether LiveView is needed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
