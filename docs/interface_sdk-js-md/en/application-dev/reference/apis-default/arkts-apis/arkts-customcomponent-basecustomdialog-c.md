# BaseCustomDialog

Definition of base custom dialog class.

**Inheritance/Implementation:** BaseCustomDialog extends [ExtendableComponent](arkts-extendablecomponent-extendablecomponent-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare abstract class BaseCustomDialog--><!--Device-unnamed-export declare abstract class BaseCustomDialog-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
@Builder
  static _invokeImpl<S extends BaseCustomDialog<S, S_Options>, S_Options>(
        factory: () => S,
        initializers?: () => S_Options,
        content?: CustomBuilder
    ): void
```

Implementation for creating a custom dialog

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseCustomDialog-@Builder  static _invokeImpl<S extends BaseCustomDialog<S, S_Options>, S_Options>(        factory: () => S,        initializers?: () => S_Options,        content?: CustomBuilder    ): void--><!--Device-BaseCustomDialog-@Builder  static _invokeImpl<S extends BaseCustomDialog<S, S_Options>, S_Options>(        factory: () => S,        initializers?: () => S_Options,        content?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; S | Yes | factory to create instance of custom dialog |
| initializers | () =&gt; S_Options | No | initial data for all the fields in custom dialog |
| content | [CustomBuilder](arkts-custombuilder-t.md) | No | tail closure for custom dialog |

## constructor

```TypeScript
constructor(useSharedStorage?: boolean, storage?: LocalStorage)
```

Constructor to use to create a custom dialog instance.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaseCustomDialog-constructor(useSharedStorage?: boolean, storage?: LocalStorage)--><!--Device-BaseCustomDialog-constructor(useSharedStorage?: boolean, storage?: LocalStorage)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| useSharedStorage | boolean | No | determine whether to use the LocalStorage instance object returned by UIContext.getSharedLocalStorage() interface. |
| storage | LocalStorage | No | localStorage instance. |

