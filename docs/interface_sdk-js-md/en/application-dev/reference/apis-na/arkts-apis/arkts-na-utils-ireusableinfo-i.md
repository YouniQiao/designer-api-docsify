# IReusableInfo

IReusableInfo is a reuse pool information interface for custom component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface IReusableInfo--><!--Device-unnamed-export declare interface IReusableInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## count

```TypeScript
readonly count: int
```

Current number of @Reuseable/V2 component instances in pool. count is usually <= maxCount. It is allowed to be larger for short time because pool clean happens asynchronously.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IReusableInfo-readonly count: int--><!--Device-IReusableInfo-readonly count: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxCount

```TypeScript
maxCount: int
```

Maximum number of permissible @Reusable/V2 component instances. The default is 100. The maximal value is 200.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IReusableInfo-maxCount: int--><!--Device-IReusableInfo-maxCount: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reuseId

```TypeScript
readonly reuseId? : string
```

Reuse id.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IReusableInfo-readonly reuseId? : string--><!--Device-IReusableInfo-readonly reuseId? : string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

