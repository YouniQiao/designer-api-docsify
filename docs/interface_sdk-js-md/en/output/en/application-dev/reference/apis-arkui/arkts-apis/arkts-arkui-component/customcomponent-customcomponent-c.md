# CustomComponent

Definition of custom component class.

**Inheritance/Implementation:** CustomComponent extends [BaseCustomComponent<T_Options>](BaseCustomComponent<T_Options>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class CustomComponent<T extends CustomComponent<T, T_Options>, T_Options> extends BaseCustomComponent<T_Options>--><!--Device-unnamed-export declare abstract class CustomComponent<T extends CustomComponent<T, T_Options>, T_Options> extends BaseCustomComponent<T_Options>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(factory: () => S,
        initializers?: () => S_Options,
        reuseId?: string,
        content?: CustomBuilder
    ): void
```

Implementation for creating a custom component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder    ): void--><!--Device-CustomComponent-static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S\_Options | No | initial data for all the fields in custom component |
| reuseId | string | No | reuse id for reusable. Only valid if custom component decorated with @Reusable |
| content | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | tail closure for custom component |

## _invokeImpl

```TypeScript
static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(factory: () => S,
        initializers?: () => S_Options,
        reuseId?: string,
        content?: CustomBuilder,
        options?: CustomComponentV1InvokeOptions
    ): void
```

Implementation for creating a custom component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder,        options?: CustomComponentV1InvokeOptions    ): void--><!--Device-CustomComponent-static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder,        options?: CustomComponentV1InvokeOptions    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S\_Options | No | initial data for all the fields in custom component |
| reuseId | string | No | reuse id for reusable. Only valid if custom component decorated with @Reusable |
| content | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | tail closure for custom component |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | additional invoke options |

## aboutToReuse

```TypeScript
aboutToReuse(params: ReuseObject): void
```

aboutToReuse Method

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-aboutToReuse(params: ReuseObject): void--><!--Device-CustomComponent-aboutToReuse(params: ReuseObject): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Custom component init params. |

## constructor

```TypeScript
constructor(useSharedStorage?: boolean, storage?: LocalStorage)
```

Constructor to use to create a customComponent instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-constructor(useSharedStorage?: boolean, storage?: LocalStorage)--><!--Device-CustomComponent-constructor(useSharedStorage?: boolean, storage?: LocalStorage)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| useSharedStorage | boolean | No | determine whether to use the LocalStorage instance object returned by UIContext.getSharedLocalStorage() interface. |
| storage | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | localStorage instance. |

