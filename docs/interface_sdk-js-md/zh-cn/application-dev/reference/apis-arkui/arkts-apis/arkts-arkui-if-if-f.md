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

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute--><!--Device-unnamed-export declare function If(  condition: boolean,  content_: CustomBuilder): IfAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | boolean | 是 | 'If'分支对应的条件 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 | 'If'分支需要运行的代码 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IfAttribute](arkts-arkui-if-ifattribute-i.md) |  |


## If

```TypeScript
export declare function If(
    style: CustomBuilderT<IfAttribute>,
    content_: CustomBuilder
): IfAttribute
```

定义If组件。它需要在组件属性设置开始时调用setIfOptions。并且它需要在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute--><!--Device-unnamed-export declare function If(    style: CustomBuilderT<IfAttribute>,    content_: CustomBuilder): IfAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;IfAttribute&gt; | 是 | 回调来设置If的属性 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | 是 | 分支的逻辑代码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IfAttribute](arkts-arkui-if-ifattribute-i.md) | If的属性。 |

