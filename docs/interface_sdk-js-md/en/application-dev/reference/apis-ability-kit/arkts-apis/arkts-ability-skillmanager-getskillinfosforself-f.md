# getSkillInfosForSelf

## Modules to Import

```TypeScript
import { skillManager } from 'kits/@kit.AbilityKit';
```

## getSkillInfosForSelf

```TypeScript
function getSkillInfosForSelf(flags: int): Promise<Array<SkillInfo>>
```

获取本应用的所有技能信息。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-skillManager-function getSkillInfosForSelf(flags: int): Promise<Array<SkillInfo>>--><!--Device-skillManager-function getSkillInfosForSelf(flags: int): Promise<Array<SkillInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flags | int | Yes | { |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;SkillInfo&gt;&gt; | Promise对象，返回调用方所在应用的所有技能信息数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700101 | Bundle manager service is exception. Possible causes: 1. Failed to connect to the system service. 2. IPC data transmission failed. 3. Failed to obtain the object constructor. |

