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

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function makeBuilderParameterProxy<T>(    instance: T,    propertyGetters: Map<string, BuilderParameterCallback>,    initializer?: Callback<T>): T--><!--Device-unnamed-export declare function makeBuilderParameterProxy<T>(    instance: T,    propertyGetters: Map<string, BuilderParameterCallback>,    initializer?: Callback<T>): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| instance | T | Yes | Builder parameter instance |
| propertyGetters | Map&lt;string, [BuilderParameterCallback](arkts-na-builderparametercallback-t.md)&gt; | Yes | getter callbacks for each property name |
| initializer | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;T&gt; | No | optional callback to initialize proxied instance |

**Return value:**

| Type | Description |
| --- | --- |
| T | proxied parameter instance |

