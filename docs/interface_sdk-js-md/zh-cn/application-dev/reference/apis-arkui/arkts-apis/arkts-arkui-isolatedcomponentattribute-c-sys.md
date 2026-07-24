# IsolatedComponentAttribute（系统接口）

仅支持[width](../arkts-components/arkts-arkui-commonmethod-c.md#width)、[height](../arkts-components/arkts-arkui-commonmethod-c.md#height)和[backgroundColor](../arkts-components/arkts-arkui-commonmethod-c.md#backgroundcolor)通用属性。

不支持[通用事件](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)。

事件经过坐标转换后异步传递给受限Worker线程处理。不支持线程之间的事件冒泡，线程之间的UI交互存在事件冲突现象。

**继承/实现关系：** IsolatedComponentAttribute extends [CommonMethod<IsolatedComponentAttribute>](CommonMethod<IsolatedComponentAttribute>)

**起始版本：** 12

<!--Device-unnamed-declare class IsolatedComponentAttribute extends CommonMethod<IsolatedComponentAttribute>--><!--Device-unnamed-declare class IsolatedComponentAttribute extends CommonMethod<IsolatedComponentAttribute>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## onError

```TypeScript
onError(
    callback: ErrorCallback
  ): IsolatedComponentAttribute
```

IsolatedComponent加载的Abc（以Ability扩展形式运行）在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-IsolatedComponentAttribute-onError(    callback: ErrorCallback  ): IsolatedComponentAttribute--><!--Device-IsolatedComponentAttribute-onError(    callback: ErrorCallback  ): IsolatedComponentAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | 是 | 异常发生时的错误回调，可通过回调参数获取code、name和message错误信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IsolatedComponentAttribute](arkts-arkui-isolatedcomponentattribute-c-sys.md) | @syscap SystemCapability.ArkUI.ArkUI.Full@systemapi@stagemodelonly |

