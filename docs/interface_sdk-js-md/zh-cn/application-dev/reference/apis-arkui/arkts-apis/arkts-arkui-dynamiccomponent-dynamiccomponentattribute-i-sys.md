# DynamicComponentAttribute（系统接口）

定义DynamicComponent的属性方法。

**继承/实现关系：** DynamicComponentAttribute extends CommonMethod

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## onError

```TypeScript
default onError(callback: ErrorCallback<BusinessError> | undefined): this
```

DynamicComponent运行过程中发生异常时触发该回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md)&lt;[BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DynamicComponentAttribute](arkts-arkui-dynamiccomponent-dynamiccomponentattribute-i-sys.md) |

## setDynamicComponentOptions

```TypeScript
default setDynamicComponentOptions(options: DynamicOptions): this
```

设置动态组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [DynamicOptions](arkts-arkui-dynamiccomponent-dynamicoptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| this |
