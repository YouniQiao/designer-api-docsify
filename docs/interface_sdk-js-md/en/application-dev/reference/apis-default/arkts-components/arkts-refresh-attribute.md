# RefreshAttribute

The RefreshAttribute.

**Inheritance/Implementation:** RefreshAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface RefreshAttribute--><!--Device-unnamed-export declare interface RefreshAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<RefreshAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-attributeModifier(modifier: AttributeModifier<RefreshAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RefreshAttribute-attributeModifier(modifier: AttributeModifier<RefreshAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RefreshAttribute](arkts-refresh-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-maxPullDownDistance(distance: double | undefined): this--><!--Device-RefreshAttribute-maxPullDownDistance(distance: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distance | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: Resource | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-maxPullDownDistance(distance: Resource | undefined): this--><!--Device-RefreshAttribute-maxPullDownDistance(distance: Resource | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distance | [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onOffsetChange

```TypeScript
onOffsetChange(callback: Callback<double> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-onOffsetChange(callback: Callback<double> | undefined): this--><!--Device-RefreshAttribute-onOffsetChange(callback: Callback<double> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;double&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRefreshing

```TypeScript
onRefreshing(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-onRefreshing(callback: (() => void) | undefined): this--><!--Device-RefreshAttribute-onRefreshing(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onStateChange

```TypeScript
onStateChange(callback: ((state: RefreshStatus) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-onStateChange(callback: ((state: RefreshStatus) => void) | undefined): this--><!--Device-RefreshAttribute-onStateChange(callback: ((state: RefreshStatus) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((state: RefreshStatus) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## pullDownRatio

```TypeScript
pullDownRatio(ratio: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-pullDownRatio(ratio: double | undefined): this--><!--Device-RefreshAttribute-pullDownRatio(ratio: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| ratio | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## pullToRefresh

```TypeScript
pullToRefresh(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-pullToRefresh(value: boolean | undefined): this--><!--Device-RefreshAttribute-pullToRefresh(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## pullUpToCancelRefresh

```TypeScript
pullUpToCancelRefresh(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-pullUpToCancelRefresh(enabled: boolean | undefined): this--><!--Device-RefreshAttribute-pullUpToCancelRefresh(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## refreshOffset

```TypeScript
refreshOffset(value: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-refreshOffset(value: double | undefined): this--><!--Device-RefreshAttribute-refreshOffset(value: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## refreshOffset

```TypeScript
refreshOffset(value: Resource | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-refreshOffset(value: Resource | undefined): this--><!--Device-RefreshAttribute-refreshOffset(value: Resource | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setRefreshOptions

```TypeScript
setRefreshOptions(options: RefreshOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-RefreshAttribute-setRefreshOptions(options: RefreshOptions): this--><!--Device-RefreshAttribute-setRefreshOptions(options: RefreshOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RefreshOptions](arkts-refresh-refreshoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Called attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RefreshAttribute-default--><!--Device-RefreshAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

