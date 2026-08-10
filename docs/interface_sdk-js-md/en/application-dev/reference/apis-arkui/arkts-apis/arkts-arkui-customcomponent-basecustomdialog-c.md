# BaseCustomDialog

Definition of base custom dialog class.

**Inheritance/Implementation:** BaseCustomDialog extends [ExtendableComponent](arkts-arkui-extendablecomponent-extendablecomponent-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class BaseCustomDialog<T extends BaseCustomDialog<T, T_Options>, T_Options> extends ExtendableComponent--><!--Device-unnamed-export declare abstract class BaseCustomDialog<T extends BaseCustomDialog<T, T_Options>, T_Options> extends ExtendableComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
static _invokeImpl<S extends BaseCustomDialog<S, S_Options>, S_Options>(
        factory: () => S,
        initializers?: () => S_Options,
        content?: CustomBuilder
    ): void
```

创建自定义对话框的实现

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseCustomDialog-static _invokeImpl<S extends BaseCustomDialog<S, S_Options>, S_Options>(        factory: () => S,        initializers?: () => S_Options,        content?: CustomBuilder    ): void--><!--Device-BaseCustomDialog-static _invokeImpl<S extends BaseCustomDialog<S, S_Options>, S_Options>(        factory: () => S,        initializers?: () => S_Options,        content?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; S | Yes | 用于创建自定义对话框实例的工厂 |
| initializers | () =&gt; S_Options | No | 自定义对话框中所有字段的初始数据 |
| content | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 自定义对话框的尾随闭包 |

## constructor

```TypeScript
constructor(useSharedStorage?: boolean, storage?: LocalStorage)
```

Constructor to use to create a custom dialog instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseCustomDialog-constructor(useSharedStorage?: boolean, storage?: LocalStorage)--><!--Device-BaseCustomDialog-constructor(useSharedStorage?: boolean, storage?: LocalStorage)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| useSharedStorage | boolean | No | determine whether to use the LocalStorage instance object returned by UIContext.getSharedLocalStorage() interface. |
| storage | [LocalStorage](arkts-arkui-localstorage-c.md) | No | localStorage instance. |

