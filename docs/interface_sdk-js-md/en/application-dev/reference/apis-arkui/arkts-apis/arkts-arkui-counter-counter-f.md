# Counter

## Counter

```TypeScript
export declare function Counter(
    content_?: CustomBuilder
): CounterAttribute
```

Defines the Counter component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Counter(    content_?: CustomBuilder): CounterAttribute--><!--Device-unnamed-export declare function Counter(    content_?: CustomBuilder): CounterAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [CounterAttribute](arkts-arkui-counter-counterattribute-i.md) | The attribute of the Counter. |


## Counter

```TypeScript
export declare function Counter(
    style: CustomBuilderT<CounterAttribute>,
    content_?: CustomBuilder,
): CounterAttribute
```

Defines Counter Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Counter(    style: CustomBuilderT<CounterAttribute>,    content_?: CustomBuilder,): CounterAttribute--><!--Device-unnamed-export declare function Counter(    style: CustomBuilderT<CounterAttribute>,    content_?: CustomBuilder,): CounterAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;CounterAttribute&gt; | Yes | Counter attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| [CounterAttribute](arkts-arkui-counter-counterattribute-i.md) |  |

