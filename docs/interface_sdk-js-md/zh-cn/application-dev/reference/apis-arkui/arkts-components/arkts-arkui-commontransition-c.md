# CommonTransition

页面转场通用动效。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

转场通用动效的构造函数。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
opacity(value: number): T
```

设置入场的起点透明度值或者退场的终点透明度值。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## scale

```TypeScript
scale(value: ScaleOptions): T
```

设置页面转场时的缩放效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScaleOptions](arkts-arkui-scaleoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## slide

```TypeScript
slide(value: SlideEffect): T
```

设置页面转场时的滑入滑出效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SlideEffect](arkts-arkui-slideeffect-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |

## translate

```TypeScript
translate(value: TranslateOptions): T
```

设置页面转场时的平移效果。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TranslateOptions](arkts-arkui-translateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T |
