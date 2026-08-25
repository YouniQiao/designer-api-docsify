# DrawModifier

Defined the draw modifier of node. Provides draw callbacks for the associated Node.

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## drawBehind

```TypeScript
drawBehind?(drawContext: DrawContext): void
```

drawBehind Method. Executed before drawing associated Node.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawContext | [DrawContext](arkts-arkui-drawcontext-t.md) | 是 |

## drawContent

```TypeScript
drawContent?(drawContext: DrawContext): void
```

drawContent Method. Executed when associated Node is drawing, the default drawContent method will be replaced if this method is set.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawContext | [DrawContext](arkts-arkui-drawcontext-t.md) | 是 |

## drawForeground

```TypeScript
drawForeground(drawContext: DrawContext): void
```

前景绘制，在关联节点和其子节点绘制后执行

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawContext | [DrawContext](arkts-arkui-drawcontext-t.md) | 是 |

## drawFront

```TypeScript
drawFront?(drawContext: DrawContext): void
```

drawFront Method. Executed after drawing associated Node.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawContext | [DrawContext](arkts-arkui-drawcontext-t.md) | 是 |

## drawOverlay

```TypeScript
drawOverlay(drawContext: DrawContext): void
```

在关联的Node及其所有子节点绘制完成后，在悬浮层中绘制内容。自定义绘制包含五个层级：内容背景层、内容层、内容前景层、前景层和悬浮层。  
- 前景层和悬浮层在子节点之后绘制。  
- 悬浮层与前景层的区别在于：悬浮层可以在组件的边界范围外进行绘制。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| drawContext | [DrawContext](arkts-arkui-drawcontext-t.md) | 是 |

## invalidate

```TypeScript
invalidate(): void
```

Invalidate the component, which will cause a re-render of the component.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
