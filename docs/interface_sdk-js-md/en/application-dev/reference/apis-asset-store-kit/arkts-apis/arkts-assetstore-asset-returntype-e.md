# ReturnType

枚举，关键资产查询返回的结果类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-asset-enum ReturnType--><!--Device-asset-enum ReturnType-End-->

**System capability:** SystemCapability.Security.Asset

## ALL

```TypeScript
ALL = 0
```

返回关键资产明文及属性。

**说明：** 查询单条关键资产明文时，需设置此类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ReturnType-ALL = 0--><!--Device-ReturnType-ALL = 0-End-->

**System capability:** SystemCapability.Security.Asset

## ATTRIBUTES

```TypeScript
ATTRIBUTES = 1
```

返回关键资产属性，不含关键资产明文。

**说明：** 批量查询关键资产属性时，需设置此类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ReturnType-ATTRIBUTES = 1--><!--Device-ReturnType-ATTRIBUTES = 1-End-->

**System capability:** SystemCapability.Security.Asset

