# ContinuousAuthParam (System API)

持续认证参数。用于配置订阅持续认证状态时的相关参数，如指定订阅的目标模板。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-companionDeviceAuth-interface ContinuousAuthParam--><!--Device-companionDeviceAuth-interface ContinuousAuthParam-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { companionDeviceAuth } from 'kits/@kit.UserAuthenticationKit';
```

## templateId

```TypeScript
templateId?: Uint8Array
```

模板ID。用于指定订阅的目标模板。若不指定此参数，默认订阅当前用户下全部模板的持续认证状态。指定具体模板ID时，仅订阅该模板的认证状态变化。

**Type:** Uint8Array

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContinuousAuthParam-templateId?: Uint8Array--><!--Device-ContinuousAuthParam-templateId?: Uint8Array-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

