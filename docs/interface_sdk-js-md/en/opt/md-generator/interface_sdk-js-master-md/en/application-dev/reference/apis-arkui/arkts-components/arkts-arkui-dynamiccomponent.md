# DynamicComponent

**DynamicComponent** is designed to support the embedding and display of UIs provided by independent .abc files within the current page, with the displayed content running in a worker thread. It is typically used in modular development scenarios where .abc pages are dynamically loaded.

## Child Components None

## DynamicComponent

```TypeScript
DynamicComponent(options: DynamicOptions)
```

Creates a **DynamicComponent** component to display the .abc UI running in the worker thread.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicComponentInterface-(options: DynamicOptions): DynamicComponentAttribute--><!--Device-DynamicComponentInterface-(options: DynamicOptions): DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DynamicOptions](arkts-arkui-dynamicoptions-i-sys.md) | Yes |

## Summary

- [DynamicOptions](arkts-arkui-dynamicoptions-i-sys.md)
- [ErrorCallback](arkts-arkui-errorcallback-t-sys.md)
- [Worker](arkts-arkui-worker-t-sys.md)
