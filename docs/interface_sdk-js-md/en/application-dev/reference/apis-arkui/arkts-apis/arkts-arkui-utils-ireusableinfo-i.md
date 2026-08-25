# IReusableInfo

IReusableInfo is a reuse pool information interface for custom component.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
readonly count: int
```

Current number of @Reuseable/V2 component instances in pool. count is usually &lt;= maxCount. It is allowed to be larger for short time because pool clean happens asynchronously.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxCount

```TypeScript
maxCount: int
```

Maximum number of permissible @Reusable/V2 component instances. The default is 100. The maximal value is 200.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuseId

```TypeScript
readonly reuseId? : string
```

Reuse id.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
