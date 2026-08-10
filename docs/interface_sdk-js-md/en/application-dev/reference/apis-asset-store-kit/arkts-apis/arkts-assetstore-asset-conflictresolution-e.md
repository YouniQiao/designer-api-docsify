# ConflictResolution

枚举，新增关键资产时的冲突（如：别名相同）处理策略。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-asset-enum ConflictResolution--><!--Device-asset-enum ConflictResolution-End-->

**System capability:** SystemCapability.Security.Asset

## OVERWRITE

```TypeScript
OVERWRITE = 0
```

覆盖原有的关键资产。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ConflictResolution-OVERWRITE = 0--><!--Device-ConflictResolution-OVERWRITE = 0-End-->

**System capability:** SystemCapability.Security.Asset

## THROW_ERROR

```TypeScript
THROW_ERROR = 1
```

抛出异常，由业务进行后续处理。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ConflictResolution-THROW_ERROR = 1--><!--Device-ConflictResolution-THROW_ERROR = 1-End-->

**System capability:** SystemCapability.Security.Asset

