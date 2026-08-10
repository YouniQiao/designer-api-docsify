# ProvideOptions

ProvideOptions是\@Provide的选项。允许在同一组件树上通过allowOverride重写同名的\@Provide，适用于子组件需要覆盖父组件同名\@Provide值的场景，提高了跨层级状态管理的灵活性。具体例子可见  
[\@Provide支持allowOverride参数](../../../ui/state-management/arkts-provide-and-consume.md#provide支持allowoverride参数)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface ProvideOptions--><!--Device-unnamed-declare interface ProvideOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowOverride

```TypeScript
allowOverride?: string
```

允许@Provide重写的别名。允许在同一组件树下通过allowOverride重写同名的@Provide。

缺省时表示@Provide不允许重写。若在未设置allowOverride的情况下定义同名@Provide，运行时会报错。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-ProvideOptions-allowOverride?: string--><!--Device-ProvideOptions-allowOverride?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

