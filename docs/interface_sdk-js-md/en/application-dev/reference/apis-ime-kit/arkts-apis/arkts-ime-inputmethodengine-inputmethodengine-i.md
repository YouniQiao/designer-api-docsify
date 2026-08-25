# InputMethodEngine

In the following API examples, you must first use [getInputMethodEngine](arkts-ime-inputmethodengine-getinputmethodengine-f.md) to obtain an **InputMethodEngine** instance, and then call the APIs using the obtained instance.

**Since:** 8

**Deprecated since:** 23

**Substitutes:** [InputMethodAbility](arkts-ime-inputmethodengine-inputmethodability-i.md)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## off('inputStart')

```TypeScript
off(
      type: 'inputStart',
      callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void
    ): void
```

Disables listening for the input method binding event.

**Since:** 8

**Deprecated since:** 23

**Substitutes:** off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) =&gt; void)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputStart' | Yes |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) = & gt; void | No |

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 23

**Substitutes:** off(type: 'keyboardShow' | 'keyboardHide', callback?: () =&gt; void)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | No |

## off('keyboardShow' | 'keyboardHide')

```TypeScript
off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void
```

Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 23

**Substitutes:** off(type: 'keyboardShow' | 'keyboardHide', callback?: () =&gt; void)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | No |

## on('inputStart')

```TypeScript
on(
      type: 'inputStart',
      callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void
    ): void
```

Enables listening for the input method binding event. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 23

**Substitutes:** on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) =&gt; void)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'inputStart' | Yes |
| callback | (kbController: KeyboardController, textInputClient: TextInputClient) = & gt; void | Yes |

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 23

**Substitutes:** on(type: 'keyboardShow' | 'keyboardHide', callback: () =&gt; void)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | Yes |

## on('keyboardShow' | 'keyboardHide')

```TypeScript
on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void
```

Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 23

**Substitutes:** on(type: 'keyboardShow' | 'keyboardHide', callback: () =&gt; void)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'keyboardShow' \| 'keyboardHide' | Yes |
| callback | () = & gt; void | Yes |
