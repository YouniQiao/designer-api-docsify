# GridItem属性/事件

**继承/实现关系：** GridItemAttribute extends CommonMethod<GridItemAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## columnEnd

```TypeScript
columnEnd(value: number)
```

设置当前元素终点列号。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## columnStart

```TypeScript
columnStart(value: number)
```

设置当前元素起始列号。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## forceRebuild

```TypeScript
forceRebuild(value: boolean)
```

设置在触发组件build时是否重新创建此节点。

> **说明：**&gt;
> 从API version 7开始支持，从API version 9开始废弃。GridItem会根据自身属性和子组件变化自行决定是否需要重新创建，无需设置。

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## onSelect

```TypeScript
onSelect(event: (isSelected: boolean) => void)
```

GridItem元素被鼠标框选的状态改变时触发回调。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (isSelected: boolean) = & gt; void | 是 |

## rowEnd

```TypeScript
rowEnd(value: number)
```

设置当前元素终点行号。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## rowStart

```TypeScript
rowStart(value: number)
```

设置当前元素起始行号。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## selectable

```TypeScript
selectable(value: boolean)
```

设置当前GridItem元素是否可以被鼠标框选。外层Grid容器的鼠标框选开启时，GridItem的框选才生效。该属性需要在设置多态样式前使用才能生效选中态样式。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## selected

```TypeScript
selected(value: boolean)
```

设置当前GridItem选中状态。该属性支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。该属性需要在设置多态样式前使用才能生效选中态样式。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |
