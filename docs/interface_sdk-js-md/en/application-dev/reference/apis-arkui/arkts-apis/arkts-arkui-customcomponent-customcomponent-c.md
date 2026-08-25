# CustomComponent

Definition of custom component class.

**Inheritance/Implementation:** CustomComponent extends BaseCustomComponent<T_Options>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## _invokeImpl

```TypeScript
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

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styles | ((instance: S) = & gt; void) \ | undefined | Yes |
| factory | () = & gt; S | Yes |
| initializers | () = & gt; S_Options | No |
| reuseId | string | No |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |

## _invokeImpl

```TypeScript
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

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| styles | ((instance: S) = & gt; void) \ | undefined | Yes |
| factory | () = & gt; S | Yes |
| initializers | () = & gt; S_Options | No |
| reuseId | string | No |
| content | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |
| options | [CustomComponentV1InvokeOptions](arkts-arkui-customcomponent-customcomponentv1invokeoptions-i.md) | No |

## aboutToReuse

```TypeScript
aboutToReuse(params: ReuseObject): void
```

aboutToReuse Method

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [ReuseObject](arkts-arkui-customcomponent-reuseobject-c.md) | Yes |

## constructor

```TypeScript
constructor(useSharedStorage?: boolean, storage?: LocalStorage)
```

Constructor to use to create a customComponent instance.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| useSharedStorage | boolean | No |
| storage | [LocalStorage](arkts-arkui-localstorage-localstorage-c.md) | No |
