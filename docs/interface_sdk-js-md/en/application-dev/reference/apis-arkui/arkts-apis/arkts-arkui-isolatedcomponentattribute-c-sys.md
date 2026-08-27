# IsolatedComponentAttribute (System API)

Only the width, height, and backgroundColor universal attributes are supported.

The universal events are not supported.

Events are asynchronously passed to the restricted Worker thread after coordinate conversion.

The following events are supported:

**Inheritance/Implementation:** IsolatedComponentAttribute extends CommonMethod<IsolatedComponentAttribute>

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## onError

```TypeScript
onError(
    callback: ErrorCallback
  ): IsolatedComponentAttribute
```

Invoked when an error occurs during the running of the **IsolatedComponent**. You can obtain the error information based on the **code**, **name**, and **message** parameters in the callback and rectify the exception accordingly.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](arkts-arkui-errorcallback-t-sys.md) | Yes | Error information. |

**Return value:**

| Type | Description |
| --- | --- |
| [IsolatedComponentAttribute](arkts-arkui-isolatedcomponentattribute-c-sys.md) |  |
