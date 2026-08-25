# Refresh properties/events

In addition to the universal attributes, the following attributes are supported.In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** RefreshAttribute extends CommonMethod<RefreshAttribute>

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: Optional<number>)
```

Sets the maximum pull-down distance.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| distance | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: number | Resource | undefined)
```

Sets the maximum pull-down distance. The resource type is supported.If this API is not set, the maximum pull-down distance is **undefined**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| distance | number \| Resource \| undefined | Yes |

## onOffsetChange

```TypeScript
onOffsetChange(callback: Callback<number>)
```

Called when the pull-down distance changes.

> **NOTE：**&gt;
> This API can be called within attributeModifier since API version 20.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;number & gt; | Yes |

## onRefreshing

```TypeScript
onRefreshing(callback: () => void)
```

Called when the component starts refreshing.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | () = & gt; void | Yes |

## onStateChange

```TypeScript
onStateChange(callback: (state: RefreshStatus) => void)
```

Called when the refresh status changes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (state: RefreshStatus) = & gt; void | Yes |

## pullDownRatio

```TypeScript
pullDownRatio(ratio: Optional<number>)
```

Sets the pull-down ratio.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [ratio](../arkts-apis/arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | Yes |

## pullToRefresh

```TypeScript
pullToRefresh(value: boolean)
```

Sets whether to initiate a refresh when the pull-down distance exceeds the value of [refreshOffset](#refreshoffset).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## pullUpToCancelRefresh

```TypeScript
pullUpToCancelRefresh(enabled: boolean | undefined)
```

Sets whether to enable the pull-up-to-cancel gesture for refreshing operations.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

## refreshOffset

```TypeScript
refreshOffset(value: number)
```

Sets the minimum pull-down offset required to trigger a refresh. If the distance pulled down is less than the value specified by this attribute, releasing the gesture does not trigger a refresh.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## refreshOffset

```TypeScript
refreshOffset(value: number | Resource)
```

Sets the pull-down offset that triggers the refresh. When the pull-down distance is less than the value of this attribute, releasing the pull-down gesture does not trigger the refresh. The resource type is supported.If this API and [promptText](arkts-arkui-refreshoptions-i.md) are not set, the default offset is 64 vp. If [promptText](arkts-arkui-refreshoptions-i.md) is set, the default offset is 96 vp.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
