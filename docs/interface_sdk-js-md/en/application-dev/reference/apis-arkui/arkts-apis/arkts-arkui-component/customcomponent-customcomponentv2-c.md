# CustomComponentV2

Definition of V2 custom component class.

**Inheritance/Implementation:** CustomComponentV2 extends [BaseCustomComponent<T_Options>](BaseCustomComponent<T_Options>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare abstract class CustomComponentV2<T extends CustomComponentV2<T, T_Options>, T_Options> extends BaseCustomComponent<T_Options>--><!--Device-unnamed-export declare abstract class CustomComponentV2<T extends CustomComponentV2<T, T_Options>, T_Options> extends BaseCustomComponent<T_Options>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(
        @Builder styles: ((instance: S) => void) | undefined,
        factory: () => S,
        initializers?: () => S_Options,
        reuseId?: () => string,
        content?: CustomBuilder
    ): void
```

Implementation for creating a v2 custom component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder    ): void--><!--Device-CustomComponentV2-static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S\_Options | No | initial data for all the fields in custom component |
| reuseId | () =&gt; string | No | reuse id for reusable. Only valid if custom component decorated with @ReusableV2 |
| content | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | tail closure for custom component |

## _invokeImpl

```TypeScript
static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(
        @Builder styles: ((instance: S) => void) | undefined,
        factory: () => S,
        initializers?: () => S_Options,
        reuseId?: () => string,
        content?: CustomBuilder,
        options?: CustomComponentInvokeOptions
    ): void
```

Implementation for creating a v2 custom component

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder,        options?: CustomComponentInvokeOptions    ): void--><!--Device-CustomComponentV2-static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder,        options?: CustomComponentInvokeOptions    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S\_Options | No | initial data for all the fields in custom component |
| reuseId | () =&gt; string | No | reuse id for reusable. Only valid if custom component decorated with @ReusableV2 |
| content | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | tail closure for custom component |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | additional invoke options |

## aboutToReuse

```TypeScript
aboutToReuse(): void
```

aboutToReuse Method

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-aboutToReuse(): void--><!--Device-CustomComponentV2-aboutToReuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetStateVarsOnReuse

```TypeScript
resetStateVarsOnReuse(params?: T_Options): void
```

Reset state variable

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-resetStateVarsOnReuse(params?: T_Options): void--><!--Device-CustomComponentV2-resetStateVarsOnReuse(params?: T_Options): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | T\_Options | No | data for all the fields in custom component |

