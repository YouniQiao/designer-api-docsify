# Skill

skill标签对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Skill--><!--Device-unnamed-export interface Skill-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## actions

```TypeScript
readonly actions: Array<string>
```

Skill接收的[Action集合](arkts-ability-wantconstant-action-depr-e.md)。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Skill-readonly actions: Array<string>--><!--Device-Skill-readonly actions: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## domainVerify

```TypeScript
readonly domainVerify: boolean
```

Skill接收的DomainVerify值，仅在AbilityInfo中存在，表示是否开启域名校验，取值为true表示开启域名校验，取值为false表示未开启域名校验。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Skill-readonly domainVerify: boolean--><!--Device-Skill-readonly domainVerify: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## entities

```TypeScript
readonly entities: Array<string>
```

Skill接收的[Entity集合](arkts-ability-wantconstant-entity-depr-e.md)。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Skill-readonly entities: Array<string>--><!--Device-Skill-readonly entities: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

## uris

```TypeScript
readonly uris: Array<SkillUri>
```

Want匹配的Uri集合。

**Type:** Array&lt;SkillUri&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Skill-readonly uris: Array<SkillUri>--><!--Device-Skill-readonly uris: Array<SkillUri>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

