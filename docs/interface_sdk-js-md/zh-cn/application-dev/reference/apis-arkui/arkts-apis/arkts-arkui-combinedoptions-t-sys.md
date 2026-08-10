# CombinedOptions（系统接口）

```TypeScript
type CombinedOptions<T extends ViewModel, Data> = object &
  Options<T, Data> &
  ThisType<T & ViewModel & Data>
```

Used for ide.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-unnamed-type CombinedOptions<T extends ViewModel, Data> = object &  Options<T, Data> &  ThisType<T & ViewModel & Data>--><!--Device-unnamed-type CombinedOptions<T extends ViewModel, Data> = object &  Options<T, Data> &  ThisType<T & ViewModel & Data>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**系统接口：** 此接口为系统接口。

**属性类型：** object &
  Options<T, Data> &
  ThisType<T & ViewModel & Data>

