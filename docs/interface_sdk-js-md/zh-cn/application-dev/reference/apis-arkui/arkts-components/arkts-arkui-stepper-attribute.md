# Stepper属性/事件

无@extends CommonMethod&lt;StepperAttribute&gt;

**继承/实现关系：** StepperAttribute extends CommonMethod<StepperAttribute>

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 22

**替代接口：** SwiperAttribute

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## onChange

```TypeScript
onChange(callback: (prevIndex: number, index: number) => void)
```

Callback when the change label is clicked.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 22

**替代接口：** onChange

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (prevIndex: number, index: number) = & gt; void | 是 |

## onFinish

```TypeScript
onFinish(callback: () => void)
```

Callback when the finish label is clicked.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 22

**替代接口：** onChange

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () = & gt; void | 是 |

## onNext

```TypeScript
onNext(callback: (index: number, pendingIndex: number) => void)
```

Callback when the next label is clicked.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 22

**替代接口：** onChange

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (index: number, pendingIndex: number) = & gt; void | 是 |

## onPrevious

```TypeScript
onPrevious(callback: (index: number, pendingIndex: number) => void)
```

Callback when the previous label is clicked.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 22

**替代接口：** onChange

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (index: number, pendingIndex: number) = & gt; void | 是 |

## onSkip

```TypeScript
onSkip(callback: () => void)
```

Callback when the skip label is clicked.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 22

**替代接口：** onChange

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | () = & gt; void | 是 |
