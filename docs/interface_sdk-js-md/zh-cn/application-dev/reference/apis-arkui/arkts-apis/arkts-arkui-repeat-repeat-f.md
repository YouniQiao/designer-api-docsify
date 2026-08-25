# Repeat

## Repeat

```TypeScript
export declare function Repeat<T>(arr: RepeatArray<T>): RepeatAttribute<T>
```

Indicates the type of Repeat.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| arr | [RepeatArray](arkts-arkui-repeatarray-t.md)&lt;T&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RepeatAttribute](arkts-arkui-repeat-repeatattribute-i.md)&lt;T&gt; |


## Repeat

```TypeScript
export declare function Repeat<T>(
     style: CustomBuilderT<RepeatAttribute<T>>
 ): RepeatAttribute<T>
```

定义Repeat组件。需要在组件属性设置开始时调用setRepeatOptions，并在组件属性设置结束时调用applyAttributeFinish。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[RepeatAttribute](arkts-arkui-repeat-repeatattribute-i.md)&lt;T&gt;&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RepeatAttribute](arkts-arkui-repeat-repeatattribute-i.md)&lt;T&gt; |
