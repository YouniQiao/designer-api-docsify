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

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instance | T | Yes |
| propertyGetters | Map&lt;string, [BuilderParameterCallback](arkts-arkui-builderparametercallback-t.md)&gt; | Yes |
| initializer | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;T&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| T |
