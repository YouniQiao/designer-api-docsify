# WantAgentInfo

Defines the information required for triggering a WantAgent object. The information can be used as an input parameter in getWantAgent to obtain a specified WantAgent object.

**Since:** 23

<!--Device-unnamed-export interface WantAgentInfo--><!--Device-unnamed-export interface WantAgentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## actionFlags

```TypeScript
actionFlags?: Array<abilityWantAgent.WantAgentFlags>
```

Array of flags for using the WantAgent object.

**Type:** Array&lt;abilityWantAgent.WantAgentFlags&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WantAgentInfo-actionFlags?: Array<abilityWantAgent.WantAgentFlags>--><!--Device-WantAgentInfo-actionFlags?: Array<abilityWantAgent.WantAgentFlags>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## actionType

```TypeScript
actionType?: abilityWantAgent.OperationType
```

Operation type.

**Type:** abilityWantAgent.OperationType

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WantAgentInfo-actionType?: abilityWantAgent.OperationType--><!--Device-WantAgentInfo-actionType?: abilityWantAgent.OperationType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfo

```TypeScript
extraInfo?: Record<string, RecordData>
```

Extra information about how the Want starts an ability. If there is no extra information to set, this constant can be left empty.

**Type:** Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

<!--Device-WantAgentInfo-extraInfo?: Record<string, RecordData>--><!--Device-WantAgentInfo-extraInfo?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfos

```TypeScript
extraInfos?: Record<string, RecordData>
```

Extra information about how the Want starts an ability. If there is no extra information to set, this constant can be left empty. The ability of this property is same as extraInfo. If both are set, this property will be used.

**Type:** Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

<!--Device-WantAgentInfo-extraInfos?: Record<string, RecordData>--><!--Device-WantAgentInfo-extraInfos?: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## operationType

```TypeScript
operationType?: wantAgent.OperationType
```

Operation type.This attribute is supported since API version 7 and deprecated since API version 11. You are advised to use actionType&lt;sup&gt;11+&lt;/sup&gt; instead.

**Type:** wantAgent.OperationType

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [actionType](#actiontype)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WantAgentInfo-operationType?: wantAgent.OperationType--><!--Device-WantAgentInfo-operationType?: wantAgent.OperationType-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## requestCode

```TypeScript
requestCode: int
```

Custom request code, which is used to identify the operation to execute.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WantAgentInfo-requestCode: int--><!--Device-WantAgentInfo-requestCode: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## wantAgentFlags

```TypeScript
wantAgentFlags?: Array<wantAgent.WantAgentFlags>
```

Array of flags for using the WantAgent object.This attribute is supported since API version 7 and deprecated since API version 11. You are advised to use actionFlags&lt;sup&gt;11+&lt;/sup&gt; instead.

**Type:** Array&lt;wantAgent.WantAgentFlags&gt;

**Since:** 7

**Deprecated since:** 11

**Substitutes:** [actionFlags](#actionflags)

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WantAgentInfo-wantAgentFlags?: Array<wantAgent.WantAgentFlags>--><!--Device-WantAgentInfo-wantAgentFlags?: Array<wantAgent.WantAgentFlags>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## wants

```TypeScript
wants: Array<Want>
```

Array of all Want objects. Currently, only one Want is supported. The array is reserved for future capability expansion. If multiple values are passed in, only the first member in the array is used.

**Type:** Array&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WantAgentInfo-wants: Array<Want>--><!--Device-WantAgentInfo-wants: Array<Want>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

