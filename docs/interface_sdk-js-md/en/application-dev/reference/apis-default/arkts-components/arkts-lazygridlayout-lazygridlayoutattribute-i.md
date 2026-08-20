# LazyGridLayoutAttribute

The LazyGridLayoutAttribute.

**Inheritance/Implementation:** LazyGridLayoutAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface LazyGridLayoutAttribute--><!--Device-unnamed-export declare interface LazyGridLayoutAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnsGap

```TypeScript
columnsGap(value: LengthMetrics | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-LazyGridLayoutAttribute-columnsGap(value: LengthMetrics | undefined): this--><!--Device-LazyGridLayoutAttribute-columnsGap(value: LengthMetrics | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](../arkts-apis/arkts-graphics-lengthmetrics-c.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## footer

```TypeScript
footer(builder: CustomBuilder | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-LazyGridLayoutAttribute-footer(builder: CustomBuilder | undefined): this--><!--Device-LazyGridLayoutAttribute-footer(builder: CustomBuilder | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## header

```TypeScript
header(builder: CustomBuilder | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-LazyGridLayoutAttribute-header(builder: CustomBuilder | undefined): this--><!--Device-LazyGridLayoutAttribute-header(builder: CustomBuilder | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-LazyGridLayoutAttribute-onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this--><!--Device-LazyGridLayoutAttribute-onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnVisibleIndexesChangeCallback](../../apis-arkui/arkts-components/arkts-arkui-onvisibleindexeschangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## rowsGap

```TypeScript
rowsGap(value: LengthMetrics | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-LazyGridLayoutAttribute-rowsGap(value: LengthMetrics | undefined): this--><!--Device-LazyGridLayoutAttribute-rowsGap(value: LengthMetrics | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](../arkts-apis/arkts-graphics-lengthmetrics-c.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## sticky

```TypeScript
sticky(sticky: StickyStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-LazyGridLayoutAttribute-sticky(sticky: StickyStyle | undefined): this--><!--Device-LazyGridLayoutAttribute-sticky(sticky: StickyStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sticky | [StickyStyle](../../apis-arkui/arkts-components/arkts-arkui-stickystyle-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Triggered when the index of child components in the visible area changes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LazyGridLayoutAttribute-default--><!--Device-LazyGridLayoutAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

