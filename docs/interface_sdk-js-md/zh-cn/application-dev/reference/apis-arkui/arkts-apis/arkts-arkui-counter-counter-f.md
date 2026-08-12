# Counter

## Counter

```TypeScript
export declare function Counter(
    content_?: CustomBuilder
): CounterAttribute
```

创建计数器组件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Counter(    content_?: CustomBuilder): CounterAttribute--><!--Device-unnamed-export declare function Counter(    content_?: CustomBuilder): CounterAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CounterAttribute](arkts-arkui-counter-counterattribute-i.md) | The attribute of the Counter. |


## Counter

```TypeScript
export declare function Counter(
    style: CustomBuilderT<CounterAttribute>,
    content_?: CustomBuilder,
): CounterAttribute
```

定义Counter组件。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**装饰器类型：** @Builder

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export declare function Counter(    style: CustomBuilderT<CounterAttribute>,    content_?: CustomBuilder,): CounterAttribute--><!--Device-unnamed-export declare function Counter(    style: CustomBuilderT<CounterAttribute>,    content_?: CustomBuilder,): CounterAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[CounterAttribute](arkts-arkui-counter-counterattribute-i.md)&gt; | 是 | Counter属性实例。 |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | 否 | 子组件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CounterAttribute](arkts-arkui-counter-counterattribute-i.md) |  |

