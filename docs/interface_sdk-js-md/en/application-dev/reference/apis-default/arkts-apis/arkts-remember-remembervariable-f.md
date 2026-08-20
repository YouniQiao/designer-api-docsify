# rememberVariable

## rememberVariable

```TypeScript
@Builder
export declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>
```

Create variable within @Builder functions or build().

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>--><!--Device-unnamed-@Builderexport declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| initialValue | [RememberInitialType](arkts-rememberinitialtype-t.md)&lt;T&gt; | Yes | directly pass primitives or use callback to pass class, interface and builtins. The callback is only executed once. |

**Return value:**

| Type | Description |
| --- | --- |
| [MutableVariable](arkts-remember-mutablevariable-i.md)&lt;T&gt; | mutable state variable. |

