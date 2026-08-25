# makeBuilderParameterProxy

## makeBuilderParameterProxy

```TypeScript
export declare function makeBuilderParameterProxy<T>(
    instance: T,
    propertyGetters: Map<string, BuilderParameterCallback>,
    initializer?: Callback<T>
): T
```

Make Proxy for Builder parameter.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| instance | T | 是 |
| propertyGetters | Map&lt;string, [BuilderParameterCallback](arkts-arkui-builderparametercallback-t.md)&gt; | 是 |
| initializer | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;T&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| T |
