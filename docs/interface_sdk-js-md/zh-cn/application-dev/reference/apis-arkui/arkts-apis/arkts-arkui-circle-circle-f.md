# Circle

## Circle

```TypeScript
export declare function Circle(
    options?: CircleOptions
): CircleAttribute
```

用于绘制圆形的构造函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [CircleOptions](arkts-arkui-circle-circleoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [CircleAttribute](arkts-arkui-circle-circleattribute-i.md) |


## Circle

```TypeScript
export declare function Circle(
    style: CustomBuilderT<CircleAttribute>
): CircleAttribute
```

定义Circle组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[CircleAttribute](arkts-arkui-circle-circleattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [CircleAttribute](arkts-arkui-circle-circleattribute-i.md) |
