# RawInputEventWrapper

原始输入事件包装器类。提供统一的接口来访问不同类型的输入事件，确保类型安全和向后兼容性。此类封装了原始的MouseEvent、TouchEvent或KeyEvent对象，并通过类型安全的方法访问。此类为抽象类，开发者无法自行创建实例。系统会在触发输入事件监听器时自动创建实例并传递回调函数。

> **说明：**&gt;
> 由于监听器在事件派发给具体组件之前执行，事件中的一些字段将无法提供有效值：如触发对象[target](arkts-arkui-eventtarget-i.md)、相对于组件的坐标
> [x](arkts-arkui-mouseevent-i.md#x)和[y](arkts-arkui-mouseevent-i.md#y)、[getCurrentLocalPosition](arkts-arkui-touchobject-i.md#getcurrentlocalposition)和
> [stopPropagation](arkts-arkui-touchevent-i.md#stoppropagation)方法、TouchEvent的[preventDefault](arkts-arkui-touchevent-i.md#preventdefault)和
> [getHistoricalPoints](arkts-arkui-touchevent-i.md#gethistoricalpoints)方法以及KeyEvent的[metaKey](arkts-arkui-keyevent-i.md#metakey)属性和
> [getModifierKeyState](arkts-arkui-keyevent-i.md#getmodifierkeystate)方法。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## asKeyEvent

```TypeScript
asKeyEvent(): KeyEvent | null
```

获取按键事件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [KeyEvent](arkts-arkui-keyevent-i.md) \| null |

## asMouseEvent

```TypeScript
asMouseEvent(): MouseEvent | null
```

获取鼠标事件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [MouseEvent](arkts-arkui-mouseevent-i.md) \| null |

## asTouchEvent

```TypeScript
asTouchEvent(): TouchEvent | null
```

获取触摸事件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [TouchEvent](arkts-arkui-touchevent-i.md) \| null |

## isKeyEvent

```TypeScript
isKeyEvent(): boolean
```

判断是否为按键事件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isMouseEvent

```TypeScript
isMouseEvent(): boolean
```

判断是否为鼠标事件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |

## isTouchEvent

```TypeScript
isTouchEvent(): boolean
```

判断是否为触摸事件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| boolean |
