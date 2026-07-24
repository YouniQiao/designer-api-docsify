# EmbeddedComponent属性/事件

支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)。

与屏幕坐标相关的事件信息，根据**EmbeddedComponent**的位置、宽高进行转换后，传递给EmbeddedUIExtensionAbility处理。

不支持[点击事件](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)等通用事件。仅支持以下事件。

**继承/实现关系：** EmbeddedComponentAttribute extends [CommonMethod<EmbeddedComponentAttribute>](CommonMethod<EmbeddedComponentAttribute>)

**起始版本：** 12

<!--Device-unnamed-declare class EmbeddedComponentAttribute extends CommonMethod<EmbeddedComponentAttribute>--><!--Device-unnamed-declare class EmbeddedComponentAttribute extends CommonMethod<EmbeddedComponentAttribute>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onDrawReady

```TypeScript
onDrawReady(callback: Callback<void>)
```

EmbeddedUIExtensionAbility绘制首帧时的回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-EmbeddedComponentAttribute-onDrawReady(callback: Callback<void>): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentAttribute-onDrawReady(callback: Callback<void>): EmbeddedComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-i.md)&lt;void&gt; | 是 | 回调函数，在EmbeddedUIExtensionAbility绘制第一帧时触发。 |

## onError

```TypeScript
onError(callback: import('../api/@ohos.base').ErrorCallback)
```

当启动的EmbeddedUIExtensionAbility运行过程中发生错误时调用。通过回调参数中的**code**、**name**和**message**可以获取并处理错误信息。关于错误码的详细信息，请参见[UIExtension错误码](../../../reference/apis-arkui/errorcode-uiextension.md)。
> **说明**  
>  
> 该接口不能在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)内调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-EmbeddedComponentAttribute-onError(callback: import('../api/@ohos.base').ErrorCallback): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentAttribute-onError(callback: import('../api/@ohos.base').ErrorCallback): EmbeddedComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | import('../api/@ohos.base').ErrorCallback | 是 | 用于返回[BusinessError](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-businesserror-i.md)类型错误信息的回调。基于**code**、**name**和**message**参数可以获取并处理错误信息。 |

## onTerminated

```TypeScript
onTerminated(callback: import('../api/@ohos.base').Callback<TerminationInfo>)
```

当启动的EmbeddedUIExtensionAbility通过调用[terminateSelfWithResult](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md#terminateselfwithresult)或[terminateSelf](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md#terminateself)正常退出时回调。
> **说明**  
>  
> 该接口不能在[attributeModifier](arkts-arkui-commonmethod-c.md#attributemodifier)内调用。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-EmbeddedComponentAttribute-onTerminated(callback: import('../api/@ohos.base').Callback<TerminationInfo>): EmbeddedComponentAttribute--><!--Device-EmbeddedComponentAttribute-onTerminated(callback: import('../api/@ohos.base').Callback<TerminationInfo>): EmbeddedComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | import('../api/@ohos.base').Callback&lt;TerminationInfo&gt; | 是 | 用于返回EmbeddedUIExtensionAbility结果的回调。 |

