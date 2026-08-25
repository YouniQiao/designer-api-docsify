# IReusePool

`IReusePool` 接口提供自定义组件上的全局复用池的相关功能。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getReusableInfo

```TypeScript
getReusableInfo(componentConstructor : Class, 
    reuseId?: string): IReusableInfo[] | IReusableInfo | undefined
```

检索此复用池中给定可复用组件类型的回收实例信息。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| componentConstructor | [Class](../../apis-arkts/arkts-apis/arkts-arkts-class-c.md) | 是 |
| reuseId | string | 否 |

**返回值：**

| 类型 |
| --- |
| [IReusableInfo](arkts-arkui-utils-ireusableinfo-i.md)[] \| [IReusableInfo](arkts-arkui-utils-ireusableinfo-i.md) \| undefined |

## preRender

```TypeScript
preRender(builder: WrappedBuilder<CustomBuilder>, times: int): Promise<void>
```

预创建@Reusable/@ReusableV2组件并将它们放入此复用池中。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | [WrappedBuilder](arkts-arkui-builder-wrappedbuilder-c.md)&lt;[CustomBuilder](arkts-arkui-custombuilder-t.md)&gt; | 是 |
| times | int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
