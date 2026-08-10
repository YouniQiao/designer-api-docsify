# Retention

系统提供的API注解能力，可用于指定自定义注解的生命周期。此注解只能标注在其他注解声明上。在自定义注解上标注Retention注解后，根据policy的不同取值，编译器会对自定义注解执行不同的保留策略。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

<!--Device-unnamed-export @interface Retention--><!--Device-unnamed-export @interface Retention-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { Retention, RetentionPolicy } from 'kits/@kit.ArkTS';
```

## policy

```TypeScript
policy: RetentionPolicy
```

注解的保留策略。

**Type:** [RetentionPolicy](arkts-arkts-lang-retentionpolicy-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Retention-policy: RetentionPolicy--><!--Device-Retention-policy: RetentionPolicy-End-->

**System capability:** SystemCapability.Utils.Lang

