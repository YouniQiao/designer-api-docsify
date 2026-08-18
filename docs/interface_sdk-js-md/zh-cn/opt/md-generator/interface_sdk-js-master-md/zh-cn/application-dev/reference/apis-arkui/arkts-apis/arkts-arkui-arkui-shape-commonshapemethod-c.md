# CommonShapeMethod(形状)

提供形状的偏移、填充和位置设置等通用方法的基类。

**起始版本：** 12

<!--Device-unnamed-declare class CommonShapeMethod--><!--Device-unnamed-declare class CommonShapeMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## fill

```TypeScript
fill(color: ResourceColor): T
```

设置形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonShapeMethod-fill(color: ResourceColor): T--><!--Device-CommonShapeMethod-fill(color: ResourceColor): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## offset

```TypeScript
offset(offset: Position): T
```

设置相对于组件布局位置的坐标偏移。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonShapeMethod-offset(offset: Position): T--><!--Device-CommonShapeMethod-offset(offset: Position): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [offset](#offset) | [Position](../../apis-na/arkts-apis/arkts-na-units-position-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## position

```TypeScript
position(position: Position): T
```

形状的位置坐标。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-CommonShapeMethod-position(position: Position): T--><!--Device-CommonShapeMethod-position(position: Position): T-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [position](#position) | [Position](../../apis-na/arkts-apis/arkts-na-units-position-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |
