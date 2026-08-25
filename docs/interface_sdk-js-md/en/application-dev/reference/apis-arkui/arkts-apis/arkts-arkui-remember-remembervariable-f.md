# rememberVariable

## rememberVariable

```TypeScript
export declare function rememberVariable<T>(initialValue: RememberInitialType<T>): MutableVariable<T>
```

Create variable within @Builder functions or build().

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| initialValue | [RememberInitialType](arkts-arkui-rememberinitialtype-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MutableVariable](arkts-arkui-remember-mutablevariable-i.md)&lt;T&gt; |
