# OnChangeType

```TypeScript
export type OnChangeType<T> = (propertyName: string, newValue: T) => void
```

注册[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)/  
[LocalStorage](../../../ui/state-management-static/arkts-static-localstorage.md)中所引用属性变化事件的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnChangeType<T> = (propertyName: string, newValue: T) => void--><!--Device-unnamed-export type OnChangeType<T> = (propertyName: string, newValue: T) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propertyName | string | Yes | property name |
| newValue | T | Yes | the new value of state variable |

