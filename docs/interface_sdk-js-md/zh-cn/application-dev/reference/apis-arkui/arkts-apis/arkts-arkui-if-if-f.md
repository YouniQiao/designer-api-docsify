# If

## If

```TypeScript
export declare function If(
  condition: boolean,
  content_: CustomBuilder
): IfAttribute
```

定义If组件

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | boolean | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [IfAttribute](arkts-arkui-if-ifattribute-i.md) |


## If

```TypeScript
export declare function If(
    style: CustomBuilderT<IfAttribute>,
    content_: CustomBuilder
): IfAttribute
```

定义If组件。它需要在组件属性设置开始时调用setIfOptions。 并且它需要在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[IfAttribute](arkts-arkui-if-ifattribute-i.md)&gt; | 是 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [IfAttribute](arkts-arkui-if-ifattribute-i.md) |
