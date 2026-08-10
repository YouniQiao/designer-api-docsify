# UnionMode (System API)

融合效果枚举。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-unnamed-declare enum UnionMode--><!--Device-unnamed-declare enum UnionMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## SMOOTH_UNION

```TypeScript
SMOOTH_UNION = 0
```

平滑的融合形变效果。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnionMode-SMOOTH_UNION = 0--><!--Device-UnionMode-SMOOTH_UNION = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## GRAVITY_UNION

```TypeScript
GRAVITY_UNION = 1
```

引力作用下的融合形变效果。

**说明：**

设置该类型时，需要结合  
[useUnionEffect](../arkts-apis/arkts-arkui-common-commonmethod-i-sys.md/arkts-arkui-common-commonmethod-i-sys.md#useunioneffect)并设置  
[GravityCenterOptions](../arkts-apis/arkts-arkui-common-gravitycenteroptions-i-sys.md/arkts-arkui-common-gravitycenteroptions-i-sys.md)的gravityCenter为true才能生效。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UnionMode-GRAVITY_UNION = 1--><!--Device-UnionMode-GRAVITY_UNION = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

