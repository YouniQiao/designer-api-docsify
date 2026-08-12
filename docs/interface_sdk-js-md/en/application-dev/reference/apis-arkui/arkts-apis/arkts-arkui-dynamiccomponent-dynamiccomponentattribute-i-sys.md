# DynamicComponentAttribute (System API)

Define the attribute functions of DynamicComponent.

**Inheritance/Implementation:** DynamicComponentAttribute extends [CommonMethod](CommonMethod)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface DynamicComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface DynamicComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onError

```TypeScript
default onError(callback: ErrorCallback<BusinessError> | undefined): this
```

Called when the dynamic component is error.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicComponentAttribute-default onError(callback: ErrorCallback<BusinessError> | undefined): this--><!--Device-DynamicComponentAttribute-default onError(callback: ErrorCallback<BusinessError> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-errorcallback-t.md)&lt;[BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-c.md)&gt; \| undefined | Yes | called when some error occurred&lt;br/&gt; except disconnected from DynamicAbility. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setDynamicComponentOptions

```TypeScript
default setDynamicComponentOptions(options: DynamicOptions): this
```

Sets dynamic component options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicComponentAttribute-default setDynamicComponentOptions(options: DynamicOptions): this--><!--Device-DynamicComponentAttribute-default setDynamicComponentOptions(options: DynamicOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DynamicOptions](arkts-arkui-dynamiccomponent-dynamicoptions-i-sys.md) | Yes | The options |

**Return value:**

| Type | Description |
| --- | --- |
| this | DynamicComponentAttribute instance |

