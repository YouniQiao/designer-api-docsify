# extendViewModel (System API)

## extendViewModel

```TypeScript
export declare function extendViewModel<T extends ViewModel, Data>(
  options: CombinedOptions<T, Data>
): ViewModel & Data
```

**Since:** 4

**ArkTS mode:** Supports only ArkTS-Dyn, since version 4.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [CombinedOptions](arkts-arkui-combinedoptions-t-sys.md)&lt;T, Data&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ViewModel](arkts-arkui-viewmodel-viewmodel-i.md) & Data |
