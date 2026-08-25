# Refresh属性/事件

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：

**继承/实现关系：** RefreshAttribute extends CommonMethod<RefreshAttribute>

**起始版本：** 8

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: Optional<number>)
```

设置最大下拉距离。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distance | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

## maxPullDownDistance

```TypeScript
maxPullDownDistance(distance: number | Resource | undefined)
```

设置最大下拉距离，支持Resource资源类型。未通过该接口设置时，设置最大下拉距离为undefined。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distance | number \| Resource \| undefined | 是 |

## onOffsetChange

```TypeScript
onOffsetChange(callback: Callback<number>)
```

下拉距离发生变化时触发回调。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | Callback & lt;number & gt; | 是 |

## onRefreshing

```TypeScript
onRefreshing(callback: () => void)
```

进入刷新状态时触发回调，等同于onStateChange回调中state为Refresh的情况。若仅需监听刷新启动，使用onRefreshing更简洁；若需跟踪全部刷新状态变化（Inactive、Drag、OverDrag、 Refresh、Done），请使用onStateChange。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () = & gt; void | 是 |

## onStateChange

```TypeScript
onStateChange(callback: (state: RefreshStatus) => void)
```

当前刷新状态变更时，触发回调。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (state: RefreshStatus) = & gt; void | 是 |

## pullDownRatio

```TypeScript
pullDownRatio(ratio: Optional<number>)
```

设置下拉跟手系数。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ratio](../arkts-apis/arkts-arkui-componentutils-getitemsinshapepathparams-i-sys.md) | [Optional](arkts-arkui-optional-t.md)&lt;number&gt; | 是 |

## pullToRefresh

```TypeScript
pullToRefresh(value: boolean)
```

设置当下拉距离超过[refreshOffset](#refreshoffset)时是否能触发刷新。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## pullUpToCancelRefresh

```TypeScript
pullUpToCancelRefresh(enabled: boolean | undefined)
```

设置上滑是否取消刷新。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

## refreshOffset

```TypeScript
refreshOffset(value: number)
```

设置触发刷新的下拉偏移量，当下拉距离小于该属性设置值时离手不会触发刷新。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## refreshOffset

```TypeScript
refreshOffset(value: number | Resource)
```

设置触发刷新的下拉偏移量，当下拉距离小于该属性设置值时离手不会触发刷新，支持Resource资源类型。未通过该接口设置时，当未设置[promptText](arkts-arkui-refreshoptions-i.md)参数时，默认偏移量为64vp；设置了[promptText](arkts-arkui-refreshoptions-i.md)参数时，默认偏移量为96vp。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
