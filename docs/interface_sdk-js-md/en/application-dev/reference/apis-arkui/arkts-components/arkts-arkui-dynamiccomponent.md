# DynamicComponent

**DynamicComponent** is designed to support the embedding and display of UIs provided by independent .abc files within the current page, with the displayed content running in a worker thread. It is typically used in modular development scenarios where .abc pages are dynamically loaded.

## Child Components None

## DynamicComponent

```TypeScript
DynamicComponent(options: DynamicOptions)
```

Creates a **DynamicComponent** component to display the .abc UI running in the worker thread.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicComponentInterface-(options: DynamicOptions): DynamicComponentAttribute--><!--Device-DynamicComponentInterface-(options: DynamicOptions): DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DynamicOptions](arkts-arkui-dynamicoptions-i-sys.md) | Yes | Configuration parameters for constructing a **DynamicComponent**, which are used to configure the entry of the .abc page to be loaded, worker thread to run, and display options. |

## Summary

- [DynamicOptions](arkts-arkui-dynamicoptions-i-sys.md)
- [ErrorCallback](arkts-arkui-errorcallback-t-sys.md)
- [Worker](arkts-arkui-worker-t-sys.md)
