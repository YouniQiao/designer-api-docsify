# FactoryResetStrategy (System API)

Represents the factory reset strategy, which contains the **scope** (reset scope) and **strategy** (reset strategy description) fields.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-update-export interface FactoryResetStrategy--><!--Device-update-export interface FactoryResetStrategy-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## scope

```TypeScript
scope: FactoryResetScope
```

Reset scope. The value **DATA** indicates that only data in the user partition is cleared; **DATA\_AND\_OS** indicates that data in both the user partition and OS partition is cleared.

**Type:** FactoryResetScope

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FactoryResetStrategy-scope: FactoryResetScope--><!--Device-FactoryResetStrategy-scope: FactoryResetScope-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## strategy

```TypeScript
strategy: string
```

Reset strategy, which specifies the specific strategy for the reset operation. The value is a string of 0 to 64 characters. The value can contain letters, digits, underscores (\_), hyphens (-), and spaces. An exception is thrown if the value is out of range or contains invalid characters. This parameter describes the reset operation. For example, **quick erase** indicates fast data erasure, and **deep erase** indicates deep erasure.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FactoryResetStrategy-strategy: string--><!--Device-FactoryResetStrategy-strategy: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

