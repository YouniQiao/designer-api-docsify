# AbstractProperty

Define AbstractProperty&lt;T&gt; interface.

 AbstractProperty can be understood as a handler or an alias  to a property inside LocalStorage / AppStorage singleton  allows to read the value with @see get and to change the  value with @see set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AbstractProperty<T>--><!--Device-unnamed-export declare interface AbstractProperty<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## get

```TypeScript
get(): T
```

读取[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)/  
[LocalStorage](../../../ui/state-management-static/arkts-static-localstorage.md)中所引用属性的数据。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-get(): T--><!--Device-AbstractProperty-get(): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| T | AppStorage/LocalStorage中所引用属性的数据。 |

## info

```TypeScript
default info(): string
```

读取[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)/  
[LocalStorage](../../../ui/state-management-static/arkts-static-localstorage.md)中所引用属性的属性名。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-default info(): string--><!--Device-AbstractProperty-default info(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | AppStorage/LocalStorage中所引用属性的属性名。 |

## onChange

```TypeScript
default onChange(onChangeFunc: OnChangeType<T> | undefined): void
```

注册[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)/  
[LocalStorage](../../../ui/state-management-static/arkts-static-localstorage.md)中所引用属性变化的事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-default onChange(onChangeFunc: OnChangeType<T> | undefined): void--><!--Device-AbstractProperty-default onChange(onChangeFunc: OnChangeType<T> | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onChangeFunc | [OnChangeType](arkts-arkui-onchangetype-t.md)&lt;T&gt; \| undefined | Yes | 属性变化回调函数。&lt;/br&gt;如果传入有效值，则添加到监听属性变化的函数列表中。&lt;/br&gt;如果传入undefined，则清除所有 监听回调。 |

## set

```TypeScript
default set(newValue: T): void
```

更新[AppStorage](../../../ui/state-management-static/arkts-static-appstorage.md)/  
[LocalStorage](../../../ui/state-management-static/arkts-static-localstorage.md)中所引用属性的数据，newValue必须是T类型，可以为null或undefined。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AbstractProperty-default set(newValue: T): void--><!--Device-AbstractProperty-default set(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | 要更新的数据，可以为null或undefined。 |

