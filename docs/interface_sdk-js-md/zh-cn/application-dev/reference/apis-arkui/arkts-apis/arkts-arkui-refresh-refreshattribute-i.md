# RefreshAttribute

支持通用属性外，还支持以下属性：

**继承/实现关系：** RefreshAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RefreshAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

动态设置Refresh组件的属性方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RefreshAttribute](arkts-arkui-refresh-refreshattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## maxPullDownDistance

```TypeScript
default maxPullDownDistance(distance: double | undefined): this
```

设置最大下拉距离。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distance | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## maxPullDownDistance

```TypeScript
default maxPullDownDistance(distance: Resource | undefined): this
```

设置最大下拉距离，支持Resource资源类型。未通过该接口设置时，设置最大下拉距离为undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distance | [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onOffsetChange

```TypeScript
default onOffsetChange(callback: Callback<double> | undefined): this
```

下拉距离发生变化时触发回调。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;double&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onRefreshing

```TypeScript
default onRefreshing(callback: (() => void) | undefined): this
```

进入刷新状态时触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## onStateChange

```TypeScript
default onStateChange(callback: ((state: RefreshStatus) => void) | undefined): this
```

当前刷新状态变更时，触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((state: RefreshStatus) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## pullDownRatio

```TypeScript
default pullDownRatio(ratio: double | undefined): this
```

设置下拉跟手系数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ratio](arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## pullToRefresh

```TypeScript
default pullToRefresh(value: boolean | undefined): this
```

设置当下拉距离超过refreshOffset时是否能触发刷新。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## pullUpToCancelRefresh

```TypeScript
default pullUpToCancelRefresh(enabled: boolean | undefined): this
```

设置上划是否取消刷新。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## refreshOffset

```TypeScript
default refreshOffset(value: double | undefined): this
```

设置触发刷新的下拉偏移量，当下拉距离小于该属性设置值时离手不会触发刷新。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## refreshOffset

```TypeScript
default refreshOffset(value: Resource | undefined): this
```

设置触发刷新的下拉偏移量，当下拉距离小于该属性设置值时离手不会触发刷新，支持Resource资源类型。未通过该接口设置时，当未设置[promptText](../../../reference/apis-arkui/arkui-ts/ts-container-refresh.md#refreshoptions对象说明)参数 时，默认偏移量为64vp；设置了[promptText](../../../reference/apis-arkui/arkui-ts/ts-container-refresh.md#refreshoptions对象说明)参 数时，默认偏移量为96vp。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Resource](arkts-arkui-resource-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## setRefreshOptions

```TypeScript
default setRefreshOptions(options: RefreshOptions): this
```

设置刷新选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RefreshOptions](arkts-arkui-refresh-refreshoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RefreshAttribute](arkts-arkui-refresh-refreshattribute-i.md) |
