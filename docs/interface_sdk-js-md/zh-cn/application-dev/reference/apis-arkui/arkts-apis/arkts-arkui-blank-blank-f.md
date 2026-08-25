# Blank

## Blank

```TypeScript
export declare function Blank(
    min?: double | string,
): BlankAttribute
```

空白填充组件，在容器主轴方向上，空白填充组件具有自动填充容器空余部分的能力。 仅当父组件为Row/ Column/ Flex时生效。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| min | double \| string | 否 |

**返回值：**

| 类型 |
| --- |
| [BlankAttribute](arkts-arkui-blank-blankattribute-i.md) |


## Blank

```TypeScript
export declare function Blank(
    style: CustomBuilderT<BlankAttribute>
): BlankAttribute
```

Defines Blank Component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[BlankAttribute](arkts-arkui-blank-blankattribute-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [BlankAttribute](arkts-arkui-blank-blankattribute-i.md) |
