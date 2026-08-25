# GestureInterface

定义Gesture接口。

**起始版本：** 11

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## allowedTypes

```TypeScript
allowedTypes(types: Array<SourceTool>): T
```

设置手势响应的输入类型。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## tag

```TypeScript
tag(tag: string): T
```

设置手势的标志。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [tag](#tag) | string | 是 |

**返回值：**

| 类型 |
| --- |
| T |
