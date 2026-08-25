# CommonTransition

页面转场通用动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## opacity

```TypeScript
opacity(value: double): this
```

设置入场的起点透明度值或者退场的终点透明度值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## scale

```TypeScript
scale(value: ScaleOptions): this
```

设置页面转场时的缩放效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScaleOptions](../arkts-components/arkts-arkui-scaleoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## slide

```TypeScript
slide(value: SlideEffect): this
```

设置页面转场时的滑入滑出效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SlideEffect](arkts-arkui-pagetransition-slideeffect-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |

## translate

```TypeScript
translate(value: TranslateOptions): this
```

设置页面转场时的平移效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [TranslateOptions](../arkts-components/arkts-arkui-translateoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |
