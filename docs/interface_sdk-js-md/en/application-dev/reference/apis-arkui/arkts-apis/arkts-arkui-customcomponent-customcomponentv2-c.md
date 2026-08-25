# CustomComponentV2

Definition of V2 custom component class.

**Inheritance/Implementation:** CustomComponentV2 extends BaseCustomComponent<T_Options>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styles | ((instance: S) = & gt; void) \ | undefined | Yes |
| factory | () = & gt; S | Yes |
| initializers | () = & gt; S_Options | No |
| reuseId | () = & gt; string | No |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styles | ((instance: S) = & gt; void) \ | undefined | Yes |
| factory | () = & gt; S | Yes |
| initializers | () = & gt; S_Options | No |
| reuseId | () = & gt; string | No |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |
| options | [CustomComponentInvokeOptions](arkts-arkui-customcomponent-customcomponentinvokeoptions-i.md) | No |

## aboutToReuse

```TypeScript
aboutToReuse(): void
```

aboutToReuse Method

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetStateVarsOnReuse

```TypeScript
resetStateVarsOnReuse(params?: T_Options): void
```

Reset state variable

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | T_Options | No |
