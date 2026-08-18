# PluginComponent

The **PluginComponent** allows an application to display external UI from another application. To implement update through inter-process communication (IPC), see [@ohos.pluginComponent](../../apis-na/arkts-apis/arkts-na-plugincomponentmanager-n.md).

## Child Components Not supported

## PluginComponent

```TypeScript
PluginComponent(options: PluginComponentOptions)
```

Creates a **PluginComponent** to display the UI provided by an external application.

**Since:** 9

<!--Device-PluginComponentInterface-(options: PluginComponentOptions): PluginComponentAttribute--><!--Device-PluginComponentInterface-(options: PluginComponentOptions): PluginComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PluginComponentOptions](arkts-arkui-plugincomponentoptions-i-sys.md) | Yes | Configuration options of the **PluginComponent**. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [PluginComponentOptions](arkts-arkui-plugincomponentoptions-i-sys.md) | Defines options for constructing a **PluginComponent**. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [PluginComponentTemplate](arkts-arkui-plugincomponenttemplate-i-sys.md) | PluginComponentTemplate |
| [PluginErrorData](arkts-arkui-pluginerrordata-i-sys.md) | Data provided when the error occurs. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |

### Types

| Name | Description |
| --- | --- |
| [PluginErrorCallback](arkts-arkui-pluginerrorcallback-t-sys.md) | Callback invoked when an error occurs. |

