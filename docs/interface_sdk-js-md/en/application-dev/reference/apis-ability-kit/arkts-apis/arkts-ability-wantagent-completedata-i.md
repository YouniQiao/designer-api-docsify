# CompleteData

Describes the data returned by the operation of proactive triggering a WantAgent object.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-wantAgent-export interface CompleteData--><!--Device-wantAgent-export interface CompleteData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { WantAgent } from 'WantAgent';
```

## extraInfo

```TypeScript
extraInfo?: Record<string, RecordData>
```

Extra information.

**Type:** Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-CompleteData-extraInfo?: Record<string, RecordData>--><!--Device-CompleteData-extraInfo?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## finalCode

```TypeScript
finalCode: int
```

Request code that triggers the WantAgent object.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-finalCode: int--><!--Device-CompleteData-finalCode: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## finalData

```TypeScript
finalData: string
```

Final data collected by the common event.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-finalData: string--><!--Device-CompleteData-finalData: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## info

```TypeScript
info: WantAgent
```

WantAgent object that is triggered.

**Type:** [WantAgent](arkts-ability-wantagent-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-info: WantAgent--><!--Device-CompleteData-info: WantAgent-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## want

```TypeScript
want: Want
```

Existing Want that is triggered.

**Type:** [Want](arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompleteData-want: Want--><!--Device-CompleteData-want: Want-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

