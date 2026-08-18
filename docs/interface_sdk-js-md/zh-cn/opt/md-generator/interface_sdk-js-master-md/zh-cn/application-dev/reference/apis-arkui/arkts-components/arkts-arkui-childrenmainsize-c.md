# ChildrenMainSize

维护List组件或ListItemGroup组件的子组件在主轴方向的大小信息，仅支持一对一绑定到List组件或ListItemGroup组件。 > **说明：** > > - 提供的主轴方向大小信息必须与子组件实际在主轴方向的大小一致，子组件在主轴方向大小变化或者增删子组件时都必须通过ChildrenMainSize对象方法通知List组件或ListItemGroup组件。

**起始版本：** 12

<!--Device-unnamed-declare class ChildrenMainSize--><!--Device-unnamed-declare class ChildrenMainSize-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(childDefaultSize: number)
```

ChildrenMainSize有参构造函数。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ChildrenMainSize-constructor(childDefaultSize: number)--><!--Device-ChildrenMainSize-constructor(childDefaultSize: number)-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| childDefaultSize | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## splice

```TypeScript
splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void
```

批量增删改子组件在主轴方向的大小信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ChildrenMainSize-splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void--><!--Device-ChildrenMainSize-splice(start: number, deleteCount?: number, childrenSize?: Array<number>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| deleteCount | number | 否 |
| childrenSize | Array & lt;number & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## update

```TypeScript
update(index: number, childSize: number): void
```

修改指定索引值对应的子组件的主轴方向的大小信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ChildrenMainSize-update(index: number, childSize: number): void--><!--Device-ChildrenMainSize-update(index: number, childSize: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| childSize | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
