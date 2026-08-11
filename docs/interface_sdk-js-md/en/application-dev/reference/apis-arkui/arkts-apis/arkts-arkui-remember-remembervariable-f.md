# rememberVariable

## rememberVariable

```TypeScript
export declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>
```

Create variable within @Builder functions or build().

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>--><!--Device-unnamed-export declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| initialValue | [RememberInitialType](arkts-arkui-rememberinitialtype-t.md)&lt;T&gt; | Yes | directly pass primitives or use callback to pass class, interface and builtins. The callback is only executed once. |

**Return value:**

| Type | Description |
| --- | --- |
| [MutableVariable](arkts-arkui-remember-mutablevariable-i.md)&lt;T&gt; | mutable state variable. |

