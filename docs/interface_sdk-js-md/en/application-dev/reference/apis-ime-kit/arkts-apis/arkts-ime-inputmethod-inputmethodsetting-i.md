# InputMethodSetting

In the following API examples, you must first use [getSetting](arkts-ime-inputmethod-getsetting-f.md) to obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance.

**Since:** 8

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## displayOptionalInputMethod

```TypeScript
displayOptionalInputMethod(callback: AsyncCallback<void>): void
```

Displays a dialog box for selecting an input method. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## displayOptionalInputMethod

```TypeScript
displayOptionalInputMethod(): Promise<void>
```

Displays a dialog box for selecting an input method. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## getAllInputMethods

```TypeScript
getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void
```

Obtains a list of all input methods. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## getAllInputMethods

```TypeScript
getAllInputMethods(): Promise<Array<InputMethodProperty>>
```

Obtains a list of all input methods. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## getAllInputMethodsSync

```TypeScript
getAllInputMethodsSync(): Array<InputMethodProperty>
```

Obtains a list of all input methods. This API returns the result synchronously.

**Since:** 11

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## getInputMethods

```TypeScript
getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void
```

Obtains a list of activated or deactivated input methods. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> An activated input method refers to an input method that is enabled. The default input method is enabled by default. Other input methods can be enabled or disabled as needed.
   
> 
   
> The list of activated input methods includes the default input method and enabled input methods. The list of deactivated input methods includes all installed input methods except the enabled ones.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## getInputMethods

```TypeScript
getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>
```

Obtains a list of activated or deactivated input methods. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> An activated input method refers to an input method that is enabled. The default input method is enabled by default. Other input methods can be enabled or disabled as needed.
   
> 
   
> The list of activated input methods includes the default input method and enabled input methods. The list of deactivated input methods includes all installed input methods except the enabled ones.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## getInputMethodsSync

```TypeScript
getInputMethodsSync(enable: boolean): Array<InputMethodProperty>
```

Obtains a list of activated or deactivated input methods. This API returns the result synchronously.   
> **NOTE：**
   
> 
   
> An activated input method refers to an input method that is enabled. The default input method is enabled by default. Other input methods can be enabled or disabled as needed.
   
> 
   
> The list of activated input methods includes the default input method and enabled input methods. The list of deactivated input methods includes all installed input methods except the enabled ones.

**Since:** 11

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## getInputMethodState

```TypeScript
getInputMethodState(): Promise<EnabledState>
```

Obtains the input method state. This API uses a promise to return the result.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EnabledState](arkts-ime-inputmethod-enabledstate-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800004](../errorcode-inputmethod-framework.md#12800004-not-an-input-method) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## listCurrentInputMethodSubtype

```TypeScript
listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void
```

Obtains all subtypes of this input method. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## listCurrentInputMethodSubtype

```TypeScript
listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>
```

Obtains all subtypes of this input method. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## listInputMethod

```TypeScript
listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void
```

Obtains a list of installed input methods. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getInputMethods](#getinputmethods)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; | Yes |

## listInputMethod

```TypeScript
listInputMethod(): Promise<Array<InputMethodProperty>>
```

Obtains a list of installed input methods. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getInputMethods](#getinputmethods)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md)&gt;&gt; |

## listInputMethodSubtype

```TypeScript
listInputMethodSubtype(
      inputMethodProperty: InputMethodProperty,
      callback: AsyncCallback<Array<InputMethodSubtype>>
    ): void
```

Obtains all subtypes of a specified input method. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## listInputMethodSubtype

```TypeScript
listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>
```

Obtains all subtypes of a specified input method. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](arkts-ime-inputmethod-inputmethodproperty-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[InputMethodSubtype](arkts-ime-inputmethodsubtype-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800001](../errorcode-inputmethod-framework.md#12800001-package-manager-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## off('imeChange')

```TypeScript
off(
      type: 'imeChange',
      callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
    ): void
```

Disables listening for the input method and subtype change event. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeChange' | Yes |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) = & gt; void | No |

## on('imeChange')

```TypeScript
on(
      type: 'imeChange',
      callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void
    ): void
```

Enables listening for the input method and subtype change event. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'imeChange' | Yes |
| callback | (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) = & gt; void | Yes |

## showOptionalInputMethods

```TypeScript
showOptionalInputMethods(callback: AsyncCallback<boolean>): void
```

Displays a dialog box for selecting an input method. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## showOptionalInputMethods

```TypeScript
showOptionalInputMethods(): Promise<boolean>
```

Displays a dialog box for selecting an input method. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [inputMethodList/InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
