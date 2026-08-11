# CompleteData

Describes the data returned by the operation of proactive triggering a WantAgent object.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-wantAgent-export interface CompleteData--><!--Device-wantAgent-export interface CompleteData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { WantAgent } from 'kits/@kit.AbilityKit';
```

## extraInfo

```TypeScript
extraInfo?: Record<string, Object>
```

Extra information.

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-extraInfo?: Record<string, Object>--><!--Device-CompleteData-extraInfo?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## finalCode

```TypeScript
finalCode: int
```

Request code that triggers the WantAgent object.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-finalCode: int--><!--Device-CompleteData-finalCode: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## finalData

```TypeScript
finalData: string
```

Final data collected by the common event.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-finalData: string--><!--Device-CompleteData-finalData: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## info

```TypeScript
info: WantAgent
```

WantAgent object that is triggered.

**Type:** [WantAgent](arkts-ability-wantagent-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-info: WantAgent--><!--Device-CompleteData-info: WantAgent-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## want

```TypeScript
want: Want
```

Existing Want that is triggered.

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-want: Want--><!--Device-CompleteData-want: Want-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

