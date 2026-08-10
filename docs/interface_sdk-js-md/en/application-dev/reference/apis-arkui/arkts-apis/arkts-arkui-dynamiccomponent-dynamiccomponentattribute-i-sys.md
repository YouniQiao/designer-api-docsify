# DynamicComponentAttribute (System API)

定义DynamicComponent的属性方法。

**Inheritance/Implementation:** DynamicComponentAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface DynamicComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface DynamicComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onError

```TypeScript
default onError(callback: ErrorCallback<BusinessError> | undefined): this
```

DynamicComponent运行过程中发生异常时触发该回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicComponentAttribute-default onError(callback: ErrorCallback<BusinessError> | undefined): this--><!--Device-DynamicComponentAttribute-default onError(callback: ErrorCallback<BusinessError> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md)&lt;[BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&gt; \| undefined | Yes | 回调函数，入参用于接收异常信息。 &lt;br/&gt;ArkTS-Sta模式下，可传入undefined，表示取消回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setDynamicComponentOptions

```TypeScript
default setDynamicComponentOptions(options: DynamicOptions): this
```

设置动态组件选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicComponentAttribute-default setDynamicComponentOptions(options: DynamicOptions): this--><!--Device-DynamicComponentAttribute-default setDynamicComponentOptions(options: DynamicOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DynamicOptions](../arkts-components/arkts-arkui-dynamicoptions-i-sys.md) | Yes | 选项。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | DynamicComponentAttribute实例 |

