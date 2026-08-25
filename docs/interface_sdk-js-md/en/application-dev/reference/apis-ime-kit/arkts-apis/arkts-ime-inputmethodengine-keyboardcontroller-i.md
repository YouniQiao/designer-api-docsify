# KeyboardController

You must first use on('inputStart') to obtain a **KeyboardController** instance, and then use this instance to call the following APIs.

**Since:** 8

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## exitCurrentInputType

```TypeScript
exitCurrentInputType(callback: AsyncCallback<void>): void
```

Exits this input type. This API can be called only by the preconfigured default input method. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) |

## exitCurrentInputType

```TypeScript
exitCurrentInputType(): Promise<void>
```

Exits this input type. This API can be called only by the preconfigured default input method. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) |

## hide

```TypeScript
hide(callback: AsyncCallback<void>): void
```

Hides the keyboard. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## hide

```TypeScript
hide(): Promise<void>
```

Hides the keyboard. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## hideKeyboard

```TypeScript
hideKeyboard(callback: AsyncCallback<void>): void
```

Hides the keyboard. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [hide](#hide)(callback: AsyncCallback&lt;void&gt;)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## hideKeyboard

```TypeScript
hideKeyboard(): Promise<void>
```

Hides the keyboard. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [hide](#hide)()

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
