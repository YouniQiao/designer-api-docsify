# Counter

## Counter

```TypeScript
@ComponentBuilder
export declare function Counter(
    content_?: CustomBuilder
): CounterAttribute
```

Defines the Counter component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Counter(    content_?: CustomBuilder): CounterAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Counter(    content_?: CustomBuilder): CounterAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [CounterAttribute](arkts-counter-attribute.md) | The attribute of the Counter. |


## Counter

```TypeScript
@Builder
export declare function Counter(
    style: CustomBuilderT<CounterAttribute>,
    content_?: CustomBuilder,
): CounterAttribute
```

Defines Counter Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Counter(    style: CustomBuilderT<CounterAttribute>,    content_?: CustomBuilder,): CounterAttribute--><!--Device-unnamed-@Builderexport declare function Counter(    style: CustomBuilderT<CounterAttribute>,    content_?: CustomBuilder,): CounterAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[CounterAttribute](arkts-counter-attribute.md)&gt; | Yes | Counter attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| [CounterAttribute](arkts-counter-attribute.md) |  |

