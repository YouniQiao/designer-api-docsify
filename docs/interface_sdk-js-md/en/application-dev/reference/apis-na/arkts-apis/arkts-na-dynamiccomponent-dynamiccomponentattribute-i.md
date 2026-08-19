# DynamicComponentAttribute (System API)

Define the attribute functions of DynamicComponent.

**Inheritance/Implementation:** DynamicComponentAttribute extends CommonMethod

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface DynamicComponentAttribute--><!--Device-unnamed-export declare interface DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onError

```TypeScript
onError(callback: ErrorCallback<BusinessError> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DynamicComponentAttribute-onError(callback: ErrorCallback<BusinessError> | undefined): this--><!--Device-DynamicComponentAttribute-onError(callback: ErrorCallback<BusinessError> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md)&lt;[BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setDynamicComponentOptions

```TypeScript
setDynamicComponentOptions(options: DynamicOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-DynamicComponentAttribute-setDynamicComponentOptions(options: DynamicOptions): this--><!--Device-DynamicComponentAttribute-setDynamicComponentOptions(options: DynamicOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DynamicOptions](arkts-na-dynamiccomponent-dynamicoptions-i-sys.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
