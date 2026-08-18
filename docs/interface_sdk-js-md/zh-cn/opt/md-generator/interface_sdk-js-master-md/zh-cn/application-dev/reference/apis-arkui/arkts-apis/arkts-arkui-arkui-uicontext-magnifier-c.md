# Magnifier

提供控制放大镜的显示与隐藏的能力，放大镜会对组件内容进行放大显示，便于查看组件细节。适用于非文本类组件（如图片）需要查看细节的场景。 > **说明：**> > - 以下API需先使用UIContext中的[getMagnifier()](arkts-arkui-arkui-uicontext-uicontext-c.md#getmagnifier)方法获取Magnifier实例，再通过此实例调用对应方法。 > > - 与文本类组件自带的放大镜能力互不影响，文本类组件推荐使用自带的放大镜能力。

**起始版本：** 22

<!--Device-unnamed-export class Magnifier--><!--Device-unnamed-export class Magnifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## bind

```TypeScript
bind(id: string): void
```

绑定放大镜与指定id的组件。 > **说明：**> > 使用前需先通过UIContext中的getMagnifier()方法获取Magnifier实例。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Magnifier-bind(id: string): void--><!--Device-Magnifier-bind(id: string): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | string | 是 |

## show

```TypeScript
show(x: number, y: number): void
```

设置放大镜显示的组件内容相对于组件左上角的位置，设置成功后放大镜会对以该坐标点为中心的区域内容进行放大显示。 > **说明：**> > - 使用前需先通过UIContext中的getMagnifier()方法获取Magnifier实例。 > > - 调用此方法前，需先调用[bind](#bind)方法绑定目标组件。 > > - 当与放大镜绑定的组件自身内容发生变化时，放大镜显示内容不会自动更新，需要主动调用show接口对放大镜显示内容进行更新。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Magnifier-show(x: number, y: number): void--><!--Device-Magnifier-show(x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

## unbind

```TypeScript
unbind(): void
```

解除放大镜与当前组件的绑定。使用前需先通过UIContext中的getMagnifier()方法获取Magnifier实例。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Magnifier-unbind(): void--><!--Device-Magnifier-unbind(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
