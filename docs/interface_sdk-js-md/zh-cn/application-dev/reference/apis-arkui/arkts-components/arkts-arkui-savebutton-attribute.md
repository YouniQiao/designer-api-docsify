# SaveButton属性/事件

不支持通用属性，除了继承安全控件通用属性，还支持以下属性。 不支持通用事件，仅支持以下事件。

**继承/实现关系：** SaveButtonAttribute extends SecurityComponentMethod<SaveButtonAttribute>

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## iconBorderRadius

```TypeScript
iconBorderRadius(radius: Dimension | BorderRadiuses)
```

设置保存控件图标的边框圆角半径。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | Dimension \| [BorderRadiuses](../arkts-apis/arkts-arkui-units-borderradiuses-i.md) | 是 |

## iconSize

```TypeScript
iconSize(size: Dimension | SizeOptions)
```

设置保存控件的图标尺寸。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | Dimension \| [SizeOptions](../arkts-apis/arkts-arkui-units-sizeoptions-i.md) | 是 |

## onClick

```TypeScript
onClick(event: SaveButtonCallback)
```

点击保存控件触发该回调。用户首次点击保存控件时会展示授权弹窗，点击允许后授权成功，应用会获取访问媒体库接口的临时授权（授权持续时间见SaveButton构造函数说明）； 点击拒绝或关闭弹窗则授权失败。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [SaveButtonCallback](arkts-arkui-savebuttoncallback-t.md) | 是 |

## setIcon

```TypeScript
setIcon(icon: Resource)
```

设置保存控件的图标。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| icon | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## setText

```TypeScript
setText(text: string | Resource)
```

设置保存控件的文本。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## stateEffect

```TypeScript
stateEffect(enabled: boolean)
```

设置保存控件的按压效果。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

## symbolFontWeight

```TypeScript
symbolFontWeight(fontWeight: number | FontWeight | string | Resource)
```

设置保存控件Symbol图标粗细。  
- 调用本方法前，需先调用[setIcon](#seticon)设置Symbol格式的图标资源（如\$r('sys.symbol.xxx')），本方法才会生效。 - 若未设置Symbol图标，该方法设置的粗细不会生效。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fontWeight | number \| FontWeight \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## symbolIconColor

```TypeScript
symbolIconColor(color: Array<ResourceColor>)
```

设置保存控件Symbol图标颜色。  
- 调用本方法前，需先调用[setIcon](#seticon)设置Symbol格式的图标资源（如\$r('sys.symbol.xxx')），本方法才会生效。 - 若未设置Symbol图标，该方法设置的颜色不会生效。 - 建议与[symbolRenderingStrategy](#symbolrenderingstrategy)配合使用，以实现不同的渲染效果。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | Array & lt;ResourceColor & gt; | 是 |

## symbolRenderingStrategy

```TypeScript
symbolRenderingStrategy(strategy: SymbolRenderingStrategy)
```

设置保存控件Symbol图标渲染策略。  
- 调用本方法前，需先调用[setIcon](#seticon)设置Symbol格式的图标资源（如\$r('sys.symbol.xxx')），本方法才会生效。 - 若未设置Symbol图标，该方法设置的渲染策略不会生效。 - 与[symbolIconColor](#symboliconcolor)配合使用时，渲染策略会影响颜色数组的作用方式。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**需要权限：** ohos.permission.CUSTOMIZE_SAVE_BUTTON

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [SymbolRenderingStrategy](#symbolrenderingstrategy) | 是 |

## userCancelEvent

```TypeScript
userCancelEvent(enabled: boolean)
```

设置接收保存控件的用户取消授权事件。适用于需要区分用户主动取消授权和授权失败的场景，以便进行不同的业务处理，例如记录用户行为、提供重试提示等。

**起始版本：** 21

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为21。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |
