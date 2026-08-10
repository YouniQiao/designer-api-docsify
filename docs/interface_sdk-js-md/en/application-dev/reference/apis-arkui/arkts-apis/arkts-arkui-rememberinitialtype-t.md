# RememberInitialType

```TypeScript
type RememberInitialType<T> = (() => T) | T
```

状态变量初始值入参类型。基础类型使用类型T直接传入；复杂类型（interface、class和包含Array、Map、Set和Date的内置类型）使用回调（() => T）初始化能避免重复创建实例，性能更高。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type RememberInitialType<T> = (() => T) | T--><!--Device-unnamed-type RememberInitialType<T> = (() => T) | T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| () =&gt; T) |  |
| T |  |

