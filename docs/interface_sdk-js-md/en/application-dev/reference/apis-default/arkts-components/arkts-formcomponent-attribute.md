# FormComponentAttribute (System API)

Define the attribute functions of FormComponent.

@extends CommonMethod @interface FormComponentAttribute

**Inheritance/Implementation:** FormComponentAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface FormComponentAttribute--><!--Device-unnamed-export declare interface FormComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## allowUpdate

```TypeScript
allowUpdate(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-allowUpdate(value: boolean | undefined): this--><!--Device-FormComponentAttribute-allowUpdate(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<FormComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-attributeModifier(modifier: AttributeModifier<FormComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-FormComponentAttribute-attributeModifier(modifier: AttributeModifier<FormComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[FormComponentAttribute](arkts-formcomponent-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## colorMode

```TypeScript
colorMode(value: FormColorMode | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-colorMode(value: FormColorMode | undefined): this--><!--Device-FormComponentAttribute-colorMode(value: FormColorMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FormColorMode](arkts-formcomponent-formcolormode-e-sys.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## dimension

```TypeScript
dimension(value: FormDimension | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-dimension(value: FormDimension | undefined): this--><!--Device-FormComponentAttribute-dimension(value: FormDimension | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FormDimension](arkts-formcomponent-formdimension-e-sys.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## moduleName

```TypeScript
moduleName(value: string | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-moduleName(value: string | undefined): this--><!--Device-FormComponentAttribute-moduleName(value: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onAcquired

```TypeScript
onAcquired(callback: Callback<FormCallbackInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-onAcquired(callback: Callback<FormCallbackInfo> | undefined): this--><!--Device-FormComponentAttribute-onAcquired(callback: Callback<FormCallbackInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[FormCallbackInfo](arkts-formcomponent-formcallbackinfo-i-sys.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onError

```TypeScript
onError(callback: Callback<ErrorInformation> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-onError(callback: Callback<ErrorInformation> | undefined): this--><!--Device-FormComponentAttribute-onError(callback: Callback<ErrorInformation> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[ErrorInformation](arkts-formcomponent-errorinformation-i-sys.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onLoad

```TypeScript
onLoad(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-onLoad(callback: VoidCallback | undefined): this--><!--Device-FormComponentAttribute-onLoad(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onRouter

```TypeScript
onRouter(callback: Callback<RouterCallbackInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-onRouter(callback: Callback<RouterCallbackInfo> | undefined): this--><!--Device-FormComponentAttribute-onRouter(callback: Callback<RouterCallbackInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[RouterCallbackInfo](arkts-formcomponent-routercallbackinfo-i-sys.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onUninstall

```TypeScript
onUninstall(callback: Callback<FormCallbackInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-onUninstall(callback: Callback<FormCallbackInfo> | undefined): this--><!--Device-FormComponentAttribute-onUninstall(callback: Callback<FormCallbackInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[FormCallbackInfo](arkts-formcomponent-formcallbackinfo-i-sys.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onUpdate

```TypeScript
onUpdate(callback: Callback<FormCallbackInfo> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-onUpdate(callback: Callback<FormCallbackInfo> | undefined): this--><!--Device-FormComponentAttribute-onUpdate(callback: Callback<FormCallbackInfo> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[FormCallbackInfo](arkts-formcomponent-formcallbackinfo-i-sys.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## visibility

```TypeScript
visibility(value: Visibility | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-FormComponentAttribute-visibility(value: Visibility | undefined): this--><!--Device-FormComponentAttribute-visibility(value: Visibility | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Visibility](../../apis-arkui/arkts-apis/arkts-arkui-visibility-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
