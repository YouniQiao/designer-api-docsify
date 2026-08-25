# StackAttribute

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。@extends CommonMethod @interface StackAttribute

**继承/实现关系：** StackAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pointLight

```TypeScript
default pointLight(value: PointLightStyle | undefined): StackAttribute
```

Sets the point light style.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PointLightStyle](../arkts-components/arkts-arkui-pointlightstyle-i-sys.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [StackAttribute](arkts-arkui-stack-stackattribute-i.md) |
