# DynamicComponentAttribute（系统接口）

定义DynamicComponent的属性方法。

**继承/实现关系：** DynamicComponentAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare interface DynamicComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface DynamicComponentAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## onError

```TypeScript
default onError(callback: ErrorCallback<BusinessError> | undefined): this
```

DynamicComponent运行过程中发生异常时触发该回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DynamicComponentAttribute-default onError(callback: ErrorCallback<BusinessError> | undefined): this--><!--Device-DynamicComponentAttribute-default onError(callback: ErrorCallback<BusinessError> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md)&lt;[BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&gt; \| undefined | 是 | 回调函数，入参用于接收异常信息。 &lt;br/&gt;ArkTS-Sta模式下，可传入undefined，表示取消回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## setDynamicComponentOptions

```TypeScript
default setDynamicComponentOptions(options: DynamicOptions): this
```

设置动态组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DynamicComponentAttribute-default setDynamicComponentOptions(options: DynamicOptions): this--><!--Device-DynamicComponentAttribute-default setDynamicComponentOptions(options: DynamicOptions): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DynamicOptions](../arkts-components/arkts-arkui-dynamicoptions-i-sys.md) | 是 | 选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this | DynamicComponentAttribute实例 |

