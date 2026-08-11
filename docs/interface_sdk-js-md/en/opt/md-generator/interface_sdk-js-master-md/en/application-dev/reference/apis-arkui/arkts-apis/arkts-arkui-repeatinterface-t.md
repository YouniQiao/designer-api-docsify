# RepeatInterface

```TypeScript
declare type RepeatInterface = <T>(arr: RepeatArray<T>) => RepeatAttribute<T>
```

Indicates the type of Repeat.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-unnamed-declare type RepeatInterface = <T>(arr: RepeatArray<T>) => RepeatAttribute<T>--><!--Device-unnamed-declare type RepeatInterface = <T>(arr: RepeatArray<T>) => RepeatAttribute<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arr | [RepeatArray](arkts-arkui-repeatarray-t.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RepeatAttribute](arkts-arkui-repeatattribute-c.md)&lt;T&gt; |
