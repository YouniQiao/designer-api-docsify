# RequestResult

模态弹框请求结果，包含结果码ResultCode和请求结果ResultWant。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-dialogRequest-export interface RequestResult--><!--Device-dialogRequest-export interface RequestResult-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## result

```TypeScript
result: ResultCode
```

表示结果码。

**Type:** [ResultCode](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-appaccount-resultcode-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestResult-result: ResultCode--><!--Device-RequestResult-result: ResultCode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## want

```TypeScript
want?: Want
```

表示Want类型信息，如ability名称，包名等。

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestResult-want?: Want--><!--Device-RequestResult-want?: Want-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

