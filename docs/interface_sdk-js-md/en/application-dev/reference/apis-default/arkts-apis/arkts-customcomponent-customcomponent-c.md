# CustomComponent

Definition of custom component class.

**Inheritance/Implementation:** CustomComponent extends BaseCustomComponent<T_Options>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare abstract class CustomComponent--><!--Device-unnamed-export declare abstract class CustomComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
@Builder
  static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(
        @Builder styles: ((instance: S) => void) | undefined,
        factory: () => S,
        initializers?: () => S_Options,
        reuseId?: string,
        content?: CustomBuilder
    ): void
```

Implementation for creating a custom component

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-@Builder  static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder    ): void--><!--Device-CustomComponent-@Builder  static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S_Options | No | initial data for all the fields in custom component |
| reuseId | string | No | reuse id for reusable. Only valid if custom component decorated with @Reusable |
| content | [CustomBuilder](arkts-custombuilder-t.md) | No | tail closure for custom component |

## _invokeImpl

```TypeScript
@Builder
    static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(
        @Builder styles: ((instance: S) => void) | undefined,
        factory: () => S,
        initializers?: () => S_Options,
        reuseId?: string,
        content?: CustomBuilder,
        options?: CustomComponentV1InvokeOptions
    ): void
```

Implementation for creating a custom component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-@Builder    static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder,        options?: CustomComponentV1InvokeOptions    ): void--><!--Device-CustomComponent-@Builder    static _invokeImpl<S extends CustomComponent<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: string,        content?: CustomBuilder,        options?: CustomComponentV1InvokeOptions    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S_Options | No | initial data for all the fields in custom component |
| reuseId | string | No | reuse id for reusable. Only valid if custom component decorated with @Reusable |
| content | [CustomBuilder](arkts-custombuilder-t.md) | No | tail closure for custom component |
| options | [CustomComponentV1InvokeOptions](arkts-customcomponent-customcomponentv1invokeoptions-i.md) | No | additional invoke options |

## aboutToReuse

```TypeScript
aboutToReuse(params: ReuseObject): void
```

aboutToReuse Method

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-aboutToReuse(params: ReuseObject): void--><!--Device-CustomComponent-aboutToReuse(params: ReuseObject): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [ReuseObject](arkts-customcomponent-reuseobject-c.md) | Yes | Custom component init params. |

## constructor

```TypeScript
constructor(useSharedStorage?: boolean, storage?: LocalStorage)
```

Constructor to use to create a customComponent instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponent-constructor(useSharedStorage?: boolean, storage?: LocalStorage)--><!--Device-CustomComponent-constructor(useSharedStorage?: boolean, storage?: LocalStorage)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| useSharedStorage | boolean | No | determine whether to use the LocalStorage instance object returned by UIContext.getSharedLocalStorage() interface. |
| storage | LocalStorage | No | localStorage instance. |

