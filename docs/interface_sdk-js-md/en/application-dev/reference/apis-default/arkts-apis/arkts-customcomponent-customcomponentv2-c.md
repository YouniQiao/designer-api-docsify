# CustomComponentV2

Definition of V2 custom component class.

**Inheritance/Implementation:** CustomComponentV2 extends BaseCustomComponent<T_Options>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare abstract class CustomComponentV2--><!--Device-unnamed-export declare abstract class CustomComponentV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
@Builder
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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-@Builder  static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder    ): void--><!--Device-CustomComponentV2-@Builder  static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S_Options | No | initial data for all the fields in custom component |
| reuseId | () =&gt; string | No | reuse id for reusable. Only valid if custom component decorated with @ReusableV2 |
| content | [CustomBuilder](arkts-custombuilder-t.md) | No | tail closure for custom component |

## _invokeImpl

```TypeScript
@Builder
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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-@Builder  static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder,        options?: CustomComponentInvokeOptions    ): void--><!--Device-CustomComponentV2-@Builder  static _invokeImpl<S extends CustomComponentV2<S, S_Options>, S_Options>(        @Builder styles: ((instance: S) => void) | undefined,        factory: () => S,        initializers?: () => S_Options,        reuseId?: () => string,        content?: CustomBuilder,        options?: CustomComponentInvokeOptions    ): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styles | ((instance: S) =&gt; void) \| undefined | Yes | styles of custom component |
| factory | () =&gt; S | Yes | factory to create instance of custom component |
| initializers | () =&gt; S_Options | No | initial data for all the fields in custom component |
| reuseId | () =&gt; string | No | reuse id for reusable. Only valid if custom component decorated with @ReusableV2 |
| content | [CustomBuilder](arkts-custombuilder-t.md) | No | tail closure for custom component |
| options | [CustomComponentInvokeOptions](arkts-customcomponent-customcomponentinvokeoptions-i.md) | No | additional invoke options |

## aboutToReuse

```TypeScript
aboutToReuse(): void
```

aboutToReuse Method

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-aboutToReuse(): void--><!--Device-CustomComponentV2-aboutToReuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetStateVarsOnReuse

```TypeScript
resetStateVarsOnReuse(params?: T_Options): void
```

Reset state variable

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentV2-resetStateVarsOnReuse(params?: T_Options): void--><!--Device-CustomComponentV2-resetStateVarsOnReuse(params?: T_Options): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | T_Options | No | data for all the fields in custom component |

