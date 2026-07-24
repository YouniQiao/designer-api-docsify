# IsolatedComponentAttribute (System API)

Only the [width](../arkts-components/arkts-arkui-commonmethod-c.md#width), [height](../arkts-components/arkts-arkui-commonmethod-c.md#height), and [backgroundColor](../arkts-components/arkts-arkui-commonmethod-c.md#backgroundcolor) universal attributes are supported.

The [universal events](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md) are not supported.

Events are asynchronously passed to the restricted Worker thread after coordinate conversion.

The following events are supported:

**Inheritance/Implementation:** IsolatedComponentAttribute extends [CommonMethod<IsolatedComponentAttribute>](CommonMethod<IsolatedComponentAttribute>)

**Since:** 12

<!--Device-unnamed-declare class IsolatedComponentAttribute extends CommonMethod<IsolatedComponentAttribute>--><!--Device-unnamed-declare class IsolatedComponentAttribute extends CommonMethod<IsolatedComponentAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## onError

```TypeScript
onError(
    callback: ErrorCallback
  ): IsolatedComponentAttribute
```

Invoked when an error occurs during the running of the **IsolatedComponent**. You can obtain the error information based on the **code**, **name**, and **message** parameters in the callback and rectify the exception accordingly.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-IsolatedComponentAttribute-onError(    callback: ErrorCallback  ): IsolatedComponentAttribute--><!--Device-IsolatedComponentAttribute-onError(    callback: ErrorCallback  ): IsolatedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-errorcallback-i.md) | Yes | Error information. |

**Return value:**

| Type | Description |
| --- | --- |
| [IsolatedComponentAttribute](arkts-arkui-isolatedcomponentattribute-c-sys.md) | @syscap SystemCapability.ArkUI.ArkUI.Full@systemapi@stagemodelonly |

