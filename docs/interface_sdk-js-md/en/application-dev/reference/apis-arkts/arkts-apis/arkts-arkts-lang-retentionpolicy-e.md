# RetentionPolicy

描述注解类型保留策略的枚举类型。其枚举值和Retention结合使用，以指定注解的生命周期。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

<!--Device-unnamed-export const enum RetentionPolicy--><!--Device-unnamed-export const enum RetentionPolicy-End-->

**System capability:** SystemCapability.Utils.Lang

## SOURCE

```TypeScript
SOURCE = 'source'
```

注解将在编译期被移除。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RetentionPolicy-SOURCE = 'source'--><!--Device-RetentionPolicy-SOURCE = 'source'-End-->

**System capability:** SystemCapability.Utils.Lang

## BYTECODE

```TypeScript
BYTECODE = 'bytecode'
```

注解将保留到编译产物中。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RetentionPolicy-BYTECODE = 'bytecode'--><!--Device-RetentionPolicy-BYTECODE = 'bytecode'-End-->

**System capability:** SystemCapability.Utils.Lang

