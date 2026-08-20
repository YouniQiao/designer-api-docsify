# RefreshAttribute

支持通用属性外，还支持以下属性：

**继承/实现关系：** RefreshAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface RefreshAttribute--><!--Device-unnamed-export declare interface RefreshAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<RefreshAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-attributeModifier(modifier: AttributeModifier<RefreshAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RefreshAttribute-attributeModifier(modifier: AttributeModifier<RefreshAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RefreshAttribute](arkts-refresh-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-maxPullDownDistance(distance: double | undefined): this--><!--Device-RefreshAttribute-maxPullDownDistance(distance: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-maxPullDownDistance(distance: Resource | undefined): this--><!--Device-RefreshAttribute-maxPullDownDistance(distance: Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onOffsetChange

```TypeScript
onOffsetChange(callback: Callback<double> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-onOffsetChange(callback: Callback<double> | undefined): this--><!--Device-RefreshAttribute-onOffsetChange(callback: Callback<double> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;double&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onRefreshing

```TypeScript
onRefreshing(callback: (() => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-onRefreshing(callback: (() => void) | undefined): this--><!--Device-RefreshAttribute-onRefreshing(callback: (() => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onStateChange

```TypeScript
onStateChange(callback: ((state: RefreshStatus) => void) | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-onStateChange(callback: ((state: RefreshStatus) => void) | undefined): this--><!--Device-RefreshAttribute-onStateChange(callback: ((state: RefreshStatus) => void) | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ((state: RefreshStatus) =&gt; void) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## pullDownRatio

```TypeScript
pullDownRatio(ratio: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-pullDownRatio(ratio: double | undefined): this--><!--Device-RefreshAttribute-pullDownRatio(ratio: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## pullToRefresh

```TypeScript
pullToRefresh(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-pullToRefresh(value: boolean | undefined): this--><!--Device-RefreshAttribute-pullToRefresh(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## pullUpToCancelRefresh

```TypeScript
pullUpToCancelRefresh(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-pullUpToCancelRefresh(enabled: boolean | undefined): this--><!--Device-RefreshAttribute-pullUpToCancelRefresh(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## refreshOffset

```TypeScript
refreshOffset(value: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-refreshOffset(value: double | undefined): this--><!--Device-RefreshAttribute-refreshOffset(value: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## refreshOffset

```TypeScript
refreshOffset(value: Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-refreshOffset(value: Resource | undefined): this--><!--Device-RefreshAttribute-refreshOffset(value: Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setRefreshOptions

```TypeScript
setRefreshOptions(options: RefreshOptions): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-RefreshAttribute-setRefreshOptions(options: RefreshOptions): this--><!--Device-RefreshAttribute-setRefreshOptions(options: RefreshOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RefreshOptions](arkts-refresh-refreshoptions-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置Refresh组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-RefreshAttribute-default--><!--Device-RefreshAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

